#!/bin/sh
gunicorn "embedding_service:create_app()" -w "${WORKERS:-1}" --timeout "${WORKERS_TIMEOUT:-600}" -b 0.0.0.0:5000