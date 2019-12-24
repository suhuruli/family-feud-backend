FROM alpine:latest

# Update
RUN apk add --update python py-pip 

# Bundle app source
COPY . /src/

# Install app dependencies
RUN pip install -r /src/requirements.txt

EXPOSE  8000
CMD ["python", "/src/runserver.py", "-p 8000"]
Breakdown of the Dockerfile