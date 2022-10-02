# Download / Install / Configure Docker

### Download docker [here](http://docs.docker.com/install)  
 - Select Stable Version
 - It also installs __docker toolbox__
 - Setup a Docker [Hub](http://hub.docker.com) account

### Docker Ports
Port Number | Description
--- | ---
2376 | Docker Daemon
2377 | Docker Swarm Manager
4789 UDP | Container Ingress Network
7956 TCP/UDP | Container Network Discovery 

### Linux Installation
### IMPORTANT - Docker Security
 - Manage docker as a non-root user  
   https://docs.docker.com/engine/install/linux-postinstall/
 
 - Docker Daemon Attack Surface
   https://docs.docker.com/engine/security/#docker-daemon-attack-surface

### Centos
Download [here](http://docs.docker.com/install)
 - yum install -y yum-utils
 - yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
 - yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin
 - systemctl start docker
 - docker run hello-world
 - systemctl enable docker.service
 - systemctl enable containerd.service

#### Ubuntu
 - sudo apt-get update
 - sudo apt-get install apt-transport-https \
 ca-certificates, curl, software-properties-common 
 - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
 - sudo apt-key fingerprint 0EBFCD88
 - sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
 - sudo apt-get update
 - sudo apt-get install docker-ce
 - sudo docker run hello-world (Confirm installation)
 - sudo usermod -aG docker $USER (so that the user can run docker)
 - Install docker-compose
    * curl -L https://github.com/docker/compose/releases/download/1.23.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    * chmod +x /usr/local/bin/docker-compose
 - Install docker-machine
    * curl -L https://github.com/docker/machine/releases/tag/v0.16.0/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine
    * sudo install /tmp/docker-machine /usr/local/bin/docker-machine
 - #####*Install bash completion scripts*
    
    ```text
    base=https://raw.githubusercontent.com/docker/machine/v0.16.0    
    for i in docker-machine-prompt.bash docker-machine-wrapper.bash docker-machine.bash
    do
        sudo wget "$base/contrib/completion/bash/${i}" -P /etc/bash_completion.d
    done
```
### Docker CLI  
Docker cli | Description |
--- | ---  
docker      | Lists help of all docker commands  
docker commit container_id repo_name:tag | Save changes in a docker container's FS to a new image
docker build -t <taglist> PATH  | Build a docker image
docker container ls -a | List all containers
docker container rm <container_id> | Remove a container
docker container stop <container_id> | Stop a container
docker exec -it <container_id> <command> | Run a command in a running container
docker images | Lists docker images 
docker info | Details of the docker installation
docker inspect <container_id> | Details of a container
docker logs <container_id> | Displays Container Logs
docker login --username=<username> | Login to docker Hub
docker ps   | Lists docker containers
docker rmi <image> | Remove local copy of the image
docker run  | Run a command in a container
docker run -it --rm busybox | Will drop you into a 'sh' inside busybox. --rm removes container after exit
docker run --name <docker_name <image> | Name your container
docker run -d | Runs docker detached (daemon mode)  
docker run -it --rm -p <host_port>:<container_port>  
docker run -d -p <host_port>:<container_port> --link <dest_container> | Container Links 
docker tag <image_id> docker_hub/repo | Tag an image **Avoid the _latest_ tag**  
docker-compose up | Build services from docker-compose.yml9
docker-compose <build, ps, logs, logs -s, logs <container_id> | Docker-compose Services
docker-compose <start, stop> | Start / Stop containers
docker-compose rm | Removes ALL containers
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
### Setting DNS for docker daemon
```markdown
/etc/docker/daemon.json
{
  "dns": ["your_dns_address", "8.8.8.8"]
}
sudo service docker restart
```

### Running python from a Docker image
```text
https://hub.docker.com/_/python

Dockerfile
----------
FROM python:3
WORKDIR /home/lmascare/misc/gitwork/utils/python/admin
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /u/admin/logs
COPY . .
CMD ["python", "./mp_ping.py"]

docker build -t "python_app" .
docker run python_app

Run a Python script against the docker image
docker run -it --rm -v "$PWD":/home/lmascare/misc/gitwork/utils/python/admin \
-w /home/lmascare/misc/gitwork/utils/python/admin python_app python mp_v1.py
```

### Publish an image to Docker Hub
```markdown
Configure credential-store
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

docker build -t friendlyhello .
docker tag friendlyhello lmascare/get-started:part2
docker login
docker push lmascare/get-started:part2
docker run -p 4000:80 lmascare/get-started:part2
```

### Scaling services in Docker (SWARM)
A _docker_compose.yaml_ file defines how Docker Containers behave in Production
```yaml
version: "3"
services:
  web:
    image: lmascare/get-started:part2
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
      restart_policy:
        condition: on-failure
    ports:
      - "4000:80"
    networks:
      - webnet
networks:
  webnet:
```
```commandline
docker swarm init
docker stack deploy -c docker-compose.yaml getstartedlab
docker service ls

# To scale the APP, update the number of replicas. then run
docker stack deploy -c docker-compose.yaml getstartedlab
docker stack ps getstartedlab

# Take down the app
docker stack rm getstartedlab

# docker swarm leave --force
```

### Creating a SWARM of Docker Nodes
```text
docker-machine create -d virtualbox myvm1 (eg IP 192.168.99.100)
docker-machine create -d virtualbox myvm2 (eg IP 192.168.99.101)
docker-machine ls

# Note the directives to add a worker & another master
docker-machine ssh myvm1 "docker swarm init --advertise-addr 192.168.99.100"

# To add a worker
docker-machine ssh myvm2 "docker swarm join \
--token <token-id> 192.168.99.100:2377"

# To view the nodes in the swarm
docker-machine ssh myvm1 "docker node ls"

# Only swarm Managers execute Docker Commands. Others are workers for capacity


# These settings tell docker-machine to connect to the swarm manager
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/home/<username>/.docker/machine/machines/myvm1"
export DOCKER_MACHINE_NAME="myvm1"

# Run this command to configure your shell: 
eval $(docker-machine env myvm1)

# Unconfigure the shell
eval $(docker-machine env -u)

# Deploy the app to the swarm
docker stack deploy -c docker-compose.yaml getstartedlab
docker stack ps getstartedlab

# Start and Stop Docker Nodes
docker-machine ls
docker-machine start <docker-node>

docker stack deploy -c docker-compose.yaml getstartedlab

# Store data on the host FS. Review docker-compose.yaml
docker-machine ssh myvm1 "mkdir ./data"
```


















