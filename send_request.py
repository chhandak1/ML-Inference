#!/usr/bin/python3
import requests
import sys

#send request to server with image file name
filename=sys.argv[1]
response = requests.post("http://localhost:5000/run_inference",files={"file": open('./images/'+filename,'rb')})

print(response.json())
