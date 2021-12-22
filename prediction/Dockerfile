#base image -> python 3.7
FROM python:3.7
# RUN apt−get −y update
# RUN apt−get install −y pip3 build−essential

# create ./app as the working directory, copy contents of current folder in the system to ./app
WORKDIR /app
COPY ./ /app

#install python libraries
RUN pip install --upgrade pip 
RUN pip --no-cache-dir install -r requirements.txt

#expose port to send request to server from local system
EXPOSE 5000

#start server
ENTRYPOINT ["python", "./app.py"]