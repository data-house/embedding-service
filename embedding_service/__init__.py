import os

from flask import Flask, request
from sentence_transformers import SentenceTransformer


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.model = SentenceTransformer(
        os.environ.get("MODEL_NAME", "T-Systems-onsite/cross-en-de-roberta-sentence-transformer"))
    app.tokenizer = app.model.tokenizer
    app.strict_mode = os.environ.get("STRICT_MODE", "false").lower() == "true"

    @app.route("/embed", methods=["GET"])
    def endpoint1():
        return {"embedding_size": app.model.get_sentence_embedding_dimension()}

    @app.route("/embed", methods=["POST"])
    def endpoint2():
        if not request.json or "corpus" not in request.json:
            return {"error": "Missing corpus in json body"}, 422
        if app.strict_mode:
            if len(app.tokenizer.tokenize(request.json["corpus"])) > app.model.max_seq_length:
                return {"error": "Corpus too long"}, 422
        corpus = request.json["corpus"].lower()
        return {"embedding": app.model.encode(corpus).tolist()}

    return app
