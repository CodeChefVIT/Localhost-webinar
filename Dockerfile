FROM ubuntu:latest

# Set a directory for the app
WORKDIR /app

# Install packages
RUN apt-get update -y
RUN apt install -y python3-pip python3

# Set up the timezone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Copy all the files to the directory
COPY . /app

# Install dependencies
RUN pip3 install -r requirements.txt

# define the port number the container should expose
EXPOSE 8000

# run the command
CMD ["uvicorn","app:app","--port","8000","--host","0.0.0.0"]

