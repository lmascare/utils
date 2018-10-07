# Download / Install / Configure Docker

### Download docker [here](http://docs.docker.com/install)  
 - Select Stable Version
 - It also installs __docker toolbox__
 - Setup a Docker [Hub](http://hub.docker.com) account
 
### Docker CLI  

Docker cli | Description |
--- | ---  
docker      | Lists help of all docker commands  
docker commit container_id repo_name:tag | Save changes in a docker container's FS to a new image
docker build -t <taglist> PATH  | Build a docker image
docker exec -it <container_id> <command> | Run a command in a running container
docker images | Lists docker images 
docker info | Details of the docker installation
docker inspect <container_id> | Details of a container
docker logs <container_id> | Displays Container Logs
docker login --username=<username> | Login to docker Hub
docker ps   | Lists docker containers
docker rmi <image> | Remove local copy of the image
docker run  | Run a command in a container
docker run -it --rm busybox | Will drop you into a 'sh' inside busybox
docker run --name <docker_name <image> | Name your container
docker run -d | Runs docker detached (daemon mode)  
docker run -it --rm -p <host_port>:<container_port>  
docker tag <image_id> docker_hub/repo | Tag an image **Avoid the _latest_ tag**  
docker-machine ls | State of the Docker container  


 
####Registries  
 - Location where Docker Images are stored
 - You can host your own or use Docker's public registry called DockerHub
 
#### Repositories
 - A collection of different docker images with the same name, but different tags.

#### Docker Image Layers
 - Base Layer
 - Writable Layer

    ##### Dockerfile
    - Text file that contains instructions to assemble an image
    - Each instruction will create a new image layer
    - Name **Dockerfile**
    - CHAIN RUN commands to reduce layers
    - Sort Multiline arguments
    - CMD  - Command to run when container starts (default bash)
    - COPY - Copies new files or directories from source dir
    - ADD  - Copy files, download & copy to container, Unpack compressed files.
    
    ##### Building a Docker Image
    - Commit changes made in a Docker container
    - Write a Dockerfile

    #### Docker Cache
    - Uses existing layer if it doesn't change.
    - Can use --no-cache=true

 
### Working with Docker
 - From the Hub download busybox repository (it is a tiny version of Linux)
```commandline
# To download the busybox repository and run it
# Without a :<tag> it will download the latest
docker run -it --rm busybox
docker run busybox echo "Hello World"

# To push an image to Docker HUB
# Tag the image with your DOCKER_NAMESPACE/image
docker tag <image_id> lmascare/debian:1.2
docker login --username=<username>
docker push lmascare/debian:1.2
```
