FROM python:3.7

ENV PIPENV_TIMEOUT=36000 

COPY Pipfile Pipfile.lock ./
ENV PIP_NO_CACHE_DIR=false
RUN pip3 install pipenv==2018.11.26
RUN pipenv install --system

VOLUME /workspace
WORKDIR /workspace