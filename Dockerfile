FROM python:3.13-slim-trixie AS dev
COPY . /workspaces/gufo_traceroute
WORKDIR /workspaces/gufo_traceroute
RUN \
    set -x \
    && apt-get update \
    && apt-get -y dist-upgrade \
    && apt-get -y autoremove\     
    && apt-get install -y --no-install-recommends\
    git\
    && pip install --upgrade pip\
    && pip install --upgrade build\
    && pip install -e .[test,lint,docs,ipython]
