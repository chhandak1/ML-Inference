## Setup

To run this repository, follow the following steps:

### Installation Step 1: Install Docker

Install Docker Desktop and ensure that Docker is running on your computer.

[Install Docker Desktop Here](https://www.docker.com/products/docker-desktop)

Now, open the root folder of this repository in the command line.

### Installation Step 2: Build Project Container

Run command `sudo docker-compose build`

## Running the Application

### Start Application

Run the command `docker run -p 5000:5000 ml_inference_team_20`  

## Sending image to run inference

To run inference, the image needs to be placed in the `images` folder.
Run the command, `python send_request.py <image filename>` to run inference. For eg., `python send_request.py cat.png`

## Automated testing

For automated testing run `./run_inference.sh` to run a shell script that builds the Docker image, runs the Flask app and send an image to the server for inference.

## Link to Docker image on Google Drive:  
https://drive.google.com/file/d/15YYmHstMYjPZfnMgMSvYgHlpvXL0hbc6/view?usp=sharing
