# Kubernetes

### Concepts
 - **Deployments** are high level constructs that define an application
 - **Pods** are instances of a container in a deployment
 - **Services** are endpoints that export ports to the outside world

#### Installation
#####Pre-requisite
- Virtualizaton technology like
    - Virtualbox
    - VMware Fusion
    - Hyper-V
- Install kubectl from [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
    - OS-X
        - brew install kubectl
    - Ubuntu
        ```text
        sudo apt-get update && sudo apt-get install -y apt-transport-https
        curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
        echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
        sudo apt-get update
        sudo apt-get install -y kubectl
        ```
    - CentOS or RHEL
        ```text
        cat <<EOF > /etc/yum.repos.d/kubernetes.repo
        [kubernetes]
        name=Kubernetes
        baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
        enabled=1
        gpgcheck=1
        repo_gpgcheck=1
        gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
        EOF
        yum install -y kubectl
          ```
    - For use as a single node cluster install minikube
        - [minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
        ```text
        curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
        chmod +x minikube
        sudo cp minikube /usr/local/bin && rm minikube
        ```
    - Verify 'kubectl version'
- Install minikube from [here](http://github.com/kubernetes/minikube/releases)
    - OS-X (brew cask install minikube)
    - Verify 'minikube version'
    
#### 'minikube' Commands

Command | Description
--- | ---
minikube dashboard | Access the kubernetes dashboard
minikube start | Start minikube
minikube status | Status of the Kubernetes Cluster
minikube stop  | Stop minikube
kubectl apply -f deployment.yaml | Deploy the Kubernetes YAML file
kubectl create (_run_ is deprecated) | Deploy a sample Kubernetes "deployment"
kubectl describe pod <pod_name> | Provides details of the deployment pod
kubectl exec [-it] <pod_name> [-c CONTAINER] COMMAND [args...] | Execute a command within a container 
kubectl expose deployment <deployment>| Expose the deployment to an external network
kubectl get pod | List the "pods"
kubectl delete | Delete the deployment
kubectl port-forward <pod name> [LOCALPORT]:{REMOTE_PORT]

```commandline
kubectl run hello-minikube --image=gcr.io/google_containers/echoserver:1.4 --port=8080
kubectl expose deployment hello-minikube --type=NodePort
kubectl get pod
curl $(minikube service hello-minikube --url)
kubectl delete deployment hello-minikube
minikube stop
```

### Tomcat Deployment

[Github Demo](https://github.com/jleetutorial/kubernetes-demo)
```commandline
minikube start
kubectl apply -f ./deployment.yaml
kubectl expose deployment tomcat-deployment --type=NodePort
minikube service tomcat-deployment --url
```































