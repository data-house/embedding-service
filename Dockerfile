FROM python:3.9-slim-bullseye as build-image

WORKDIR /app

# download pretrained model
RUN apt-get update &&\
	apt-get -y upgrade &&\
	rm -rf /var/lib/apt/lists/*

# install requirements
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN python -m venv --copies /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim-bullseye AS runtime-image

# securty update
RUN apt-get update &&\
	apt-get -y upgrade &&\
	rm -rf /var/lib/apt/lists/*

# switch to app workdir
WORKDIR /app

# copy dependency form build-image
COPY --from=build-image /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY embedding_service/ embedding_service/
COPY gunicorn.sh ./

RUN chmod +x ./gunicorn.sh

ENTRYPOINT ["./gunicorn.sh"]