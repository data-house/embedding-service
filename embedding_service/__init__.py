import os

from flask import Flask, request
from sentence_transformers import SentenceTransformer


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.model = SentenceTransformer(
        os.environ.get("MODEL_NAME", "T-Systems-onsite/cross-en-de-roberta-sentence-transformer"))

    @app.route("/embed", methods=["GET"])
    def endpoint1():
        return {"embedding_size": app.model.get_sentence_embedding_dimension()}

    @app.route("/embed", methods=["POST"])
    def endpoint2():
        corpus = request.json["corpus"]
        return {"embedding": app.model.encode(corpus).tolist()}

    return app
