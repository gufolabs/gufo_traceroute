FROM python:3.11-slim-bullseye AS dev
COPY . /workspaces/gufo_traceroute
WORKDIR /workspaces/gufo_traceroute
RUN \
    set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends\
    git\
    && pip install --upgrade pip\
    && pip install --upgrade build\
    && pip install -e .[test,lint,docs,ipython]
