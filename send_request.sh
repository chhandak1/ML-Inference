#!/bin/bash

#wait till docker container has started, server is active
until $(curl --output /dev/null --silent --head --fail http://0.0.0.0:5000); do
    printf '.'
    sleep 5
done

#run python script to send request
# python send_request.py shopping-street.jpg
chmod +x send_request.py
./send_request.py shopping-street.jpg
