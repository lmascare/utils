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
- Install kubectl from [here](http://kubernetes.io)
    - OS-X (brew install kubectl)
    - Verify 'kubectl version'
- Install minikube from [here](http://github.com/kubernetes/minikube/releases)
    - OS-X (brew cask install minikube)
    - Verify 'minikube version'
    
#### 'minikube' Commands

Command | Description
--- | ---
minikube start | Start minikube
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































