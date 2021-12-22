#!/bin/bash

#build docker image
DOCKER_BUILD_RESPONSE=$(docker-compose build)
BUILD_SUCCESS_STRING="Successfully built "

#build container and run application
if [[ "$DOCKER_BUILD_RESPONSE" == *"$BUILD_SUCCESS_STRING"* ]]; then
    docker run -p 5000:5000 ml_inference_team_20
fi
