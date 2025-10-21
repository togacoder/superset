#!/bin/bash
CONTAINER_NAME='superset'

#podman exec -it ${CONTAINER_NAME} superset db upgrade

podman exec -it ${CONTAINER_NAME} superset fab create-admin \
    --username admin \
    --firstname admin \
    --lastname user \
    --email admin@fab.org \
    --password admin

podman exec -it ${CONTAINER_NAME} superset load-examples

podman exec -it ${CONTAINER_NAME} superset init
