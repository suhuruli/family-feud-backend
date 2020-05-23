FROM alpine:latest

# Update
RUN apk add --update python3 py-pip 

# Bundle app source
COPY . .

# Install app dependencies
RUN pip3 install -r requirements.txt

EXPOSE 5555 

CMD ["python3", "runserver.py"]