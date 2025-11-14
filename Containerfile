FROM docker.io/apache/superset:6.0.0rc2

USER root
RUN apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
 && rm -rf /var/lib/apt/lists/*

RUN uv pip install -U pip \
 && uv pip install --no-cache-dir mysqlclient
USER superset
