#!/bin/bash

# run shell scrpits to build docker container and send post request to server for prediction
bash build_and_run_docker_image.sh &
bash send_request.sh
