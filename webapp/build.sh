#!/bin/bash

docker build --tag=webapp . && \
docker run -p 1337:1337 --rm --name=webapp -it webapp