# embedding-service

# PRE-REQUISITES

## Local-environment

Before running the project, you need to have installed Python > 3.8.0 and pip.

Install all the required dependencies

```
pip install -r requirements.txt
```

## Docker-environment

Before running the project, you need to have installed Docker and Docker-compose.

# Running the project

## Local-environment

To run the project, just run the following command:

```
 python.exe -m flask --app embedding_service run
```

## Docker-environment

A [docker-compose.yaml](docker-compose.yaml)docker-compose file is provided to run the project in a docker environment.

# Configuration

## Environment variables
The following environment variables can be set to configure the project:

- MODEL_NAME: Name of the model to use. Every SentenceTransformer models published on HF is valid. Default: "T-Systems-onsite/cross-en-de-roberta-sentence-transformer"
- STRICT_MODE: Whenever to return an error if the text to embed is longer than the maximum context length of the model. Default: False

# Usage
The following endpoints are available:
- GET /embed: Return a JSON with 'embedding_size' conaining the size of the embeddings.
- POST /embed: Expect a body with the text to embed under the 'corpus' filed. Return a JSON with 'embedding' containing the embedding of the text provided.