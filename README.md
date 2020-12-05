# Doomsday

## What do I need to run this?

All you need is Docker.

## What is Docker?

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.

## Why Docker?

1. I just learned Docker and I already had this script so I wanted to put what I learned into practice.

2. Not everyone has Python on their machine so this allows you to execute the script without having Python on your machine

## How do I run this?

1. Install Docker using the following link:
   - [Get Docker](https://docs.docker.com/get-docker/)

2. Run `docker build -t doomsday:latest .`
   - This command will build the image locally using the Dockerfile in this repository.

3. Execute the command: `docker run -i doomsday`
   - The `i` flag will run the image in interactive mode. You will need this because the script requires input from the user.

## What do you mean by image? Like a picture image?

Not a picture image. A Docker image includes everything needed to run an application.