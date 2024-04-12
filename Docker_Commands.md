# Docker Commands

## To build an docker image

    `docker build -t <any_name> .`

    Example:

    `docker build -t my_python_flask .`

## To run the container

    `docker run -d -p 8000:8000 -e OPENAI_API_KEY={Code} --name <container_name> <image_name>`

    Ex:\
    `docker run -d -p 8000:8000 --name test_flask_app my_python_flask`

## To push it to your Docker Hub Repo

1. Tag your image\
    `docker tag <image_name> <docker_username>/<docker_image_name>:<any_tag or 'latest'>`

   example:\
    `docker tag my_python_flask varma1909/my_python_flask:latest`

2. Push it to Docker Hub using the following command\
   `docker push <docker_username>/<image_name>:<tag>`

   ex:\
    `docker push varma1909/my_python_flask:latest`
