# Embedding service for Data House

The embedding service transform text to a vector representation. This can be useful, for example, for semantic textual similarity or semantic search.

An [embedding](https://developers.google.com/machine-learning/crash-course/embeddings/video-lecture) captures some of the semantics of the input by placing semantically similar inputs close together in the embedding space. 

The service can use sentence transformers models available on [Hugging Face](https://huggingface.co/).

The default model is 
[`T-Systems-onsite/cross-en-de-roberta-sentence-transformer`](https://huggingface.co/T-Systems-onsite/cross-en-de-roberta-sentence-transformer) 
which supports English and German.


## Getting started

The Embedding service is available as a Docker image.

```bash
docker pull ghcr.io/data-house/embedding-service:main
```

The model is downloaded at startup time, so depending on the model size the first start can take several minutes. We suggest to mount a persistent volume to cache the downloaded models (folder: `/root/.cache/torch/sentence_transformers`).

A sample [`docker-compose.yaml` file](./docker-compose.yaml) is available within the repository.




> Please refer to [Releases](https://github.com/data-house/embedding-service/releases) and [Packages](https://github.com/data-house/embedding-service/pkgs/container/embedding-service) for the available tags.


**Available environment variables**

| variable | default | description |
|------|---------|-------------|
| `MODEL_NAME` | `T-Systems-onsite/cross-en-de-roberta-sentence-transformer` | The name of a sentence transformer model published on Hugging Face |
| `STRICT_MODE` | `false` | Whenever to return an error if the text to embed is longer than the maximum context length of the model |
| `WORKERS` | 2 | The number of [Gunicorn](https://docs.gunicorn.org/en/latest/settings.html#worker-class) sync workers |
| `WORKERS_TIMEOUT` | 600 | The timeout, in seconds, of each worker |


## Usage

The Embedding service expose a web application on port `5000`. The available API receive the text and return the vector representation as a JSON response.

The exposed service is unauthenticated therefore consider exposing it only within a trusted network. If you plan to make it available publicly consider adding a reverse proxy with authentication in front.

### Embed endpoint

```
POST /embed
```

The `/embed` endpoint accepts a `POST` request with the following input as a `json` body:

- `corpus` the text to transform

It returns an JSON with the following fields:

- `embedding` the array representing the embedding of the given text


> **warning** The processing is performed synchronously

### Embed maximum size endpoint

```
GET /embed
```

To obtain the maximum embedding size, the `/embed` endpoint accepts a `GET` request with no parameters.

It returns an JSON with the following fields:

- `embedding_size` the maximum length of the embedding


### Error handling

The service can return the following errors

| code | message | description |
|------|---------|-------------|
| `422` | Missing corpus in json body | In case no text is passed to the API |
| `422` | Corpus too long | In case the text to embed is too long for the model, when STRICT_MODE is enabled  |


The body of the response can contain a JSON with the following fields:

- `error` the error description

```json
{
  "error": "Missing corpus in json body",
}
```

## Development

The Embedding service is built using [Flask](https://flask.palletsprojects.com/) on Python 3.9.

Given the selected stack the development requires:

- [Python 3.9](https://www.python.org/) with PIP
- [Docker](https://www.docker.com/) (optional) to test the build


Install all the required dependencies:

```bash
pip install -r requirements.txt
```

Run the local development application using:

```bash
python -m flask --app embedding_service run
```

### Testing

_to be documented_


## Contributing

Thank you for considering contributing to the Embedding service! The contribution guide can be found in the [CONTRIBUTING.md](./.github/CONTRIBUTING.md) file.


## Supporters

The project is supported by [OneOff-Tech (UG)](https://oneofftech.de) and [Oaks S.r.l](https://www.oaks.cloud/).

<p align="left"><a href="https://oneofftech.de" target="_blank"><img src="https://raw.githubusercontent.com/OneOffTech/.github/main/art/oneofftech-logo.svg" width="200"></a></p>

<p align="left"><a href="https://www.oaks.cloud" target="_blank"><img src="https://raw.githubusercontent.com/data-house/embedding-service/main/.github/art/oaks-logo.svg" width="200"></a></p>


## Security Vulnerabilities

If you discover a security vulnerability within Embedding service, please send an e-mail to OneOff-Tech team via [security@oneofftech.xyz](mailto:security@oneofftech.xyz). All security vulnerabilities will be promptly addressed.

