# Kubernetes

### Concepts
 - **Control Plane** The Control plane co-ordinates all activities in the cluster such as scheduling, maintaining, 
 desired state, scaling applications and rolling out updates.
 - **Nodes** A Kubernetes cluster consists of a set of worker machines called ***nodes***. that run containerized 
 applications. Every cluster has at least 1 worker node. Each node has a ***kubelet*** agent for managing the node and
 communicating with the control plane.  
 A Production cluster must have at least 3-worker nodes because if one node goes down, both an ***etcd*** member and a
 ***control plane*** instance are lost. Mitigate by adding more control planes.
 

 - **Deployments** are high level constructs that define an application
 - **Pods** are instances of a container in a deployment
 - **Services** are endpoints that export ports to the outside world

### Kubenetes HOME
 - https://kubernetes.io/docs/home/
 - [Tutorial](https://kubernetes.io/docs/tutorials/)
#### Installation
#####Pre-requisite
- Virtualizaton technology like
    - Virtualbox
    - VMware Fusion
    - Hyper-V
- Install kind 
    - curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
    - chmod +x kind
    - cp kind /usr/local/bin/kind
- Install kubectl from [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
    - OS-X
        - brew install kubectl
    - Ubuntu
        ```text
        # 2023-09-17. Updated
        # Location --> https://kubernetes.io/docs/tasks/tools/
        curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
        echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
        apt update
        apt upgrade -y kubectl
        #
        # 2020 version
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
    - Just the binary
    ```text
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
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
- 
#### 'minikube' Commands

Command | Description
--- | ---
kind create cluster --name <string> | Creates a cluster. Default name kind
kind delete cluster | Deletes a cluster. Default name kind
kubectl apply -f deployment.yaml | Deploy the Kubernetes YAML file
kubectl create (_run_ is deprecated) | Deploy a sample Kubernetes "deployment"
kubectl describe pod <pod_name> | Provides details of the deployment pod
kubectl exec [-it] <pod_name> [-c CONTAINER] COMMAND [args...] | Execute a command within a container 
kubectl expose deployment <deployment>| Expose the deployment to an external network
kubectl get pod | List the "pods"
kubectl get nodes -o wide | List the "nodes" with additional details
kubectl delete | Delete the deployment
kubectl port-forward <pod name> [LOCALPORT]:{REMOTE_PORT] | Port forwarding
kubectl version | Displays kubectl version
minikube dashboard | Access the kubernetes dashboard
minikube start | Starts a local K8s cluster
minikube start --nodes 2 -p nginx-demo | Starts 2 nodes  
minikube status -p nginx-demo | Status of the nodes
minikube status | Status of the Kubernetes Cluster
minikube stop  | Stop minikube

```
# Run a stateless application (nginx)
# Create 2 Nodes
minikube start --nodes 2 -p nginx-demo

# Get the status of the nodes
minikube status -p nginx-demo
***
nginx-demo
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

nginx-demo-m02
type: Worker
host: Running
kubelet: Running
***

kubectl get nodes -o wide
***
NAME             STATUS   ROLES           AGE     VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION       CONTAINER-RUNTIME
nginx-demo       Ready    control-plane   5m6s    v1.27.4   192.168.49.2   <none>        Ubuntu 22.04.2 LTS   4.15.0-213-generic   docker://24.0.4
nginx-demo-m02   Ready    <none>          4m40s   v1.27.4   192.168.49.3   <none>        Ubuntu 22.04.2 LTS   4.15.0-213-generic   docker://24.0.4
***

# Create a YAML configuration file in <gitroot>/utils/k8s/apps/nginx.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2 # tells deployment to run 2 pods matching the template
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.24.0
        ports:
        - containerPort: 80

# Deploy the application
kubectl apply -f <gitroot>/utils/k8s/apps/nginx.yaml
# output --> deployment.apps/nginx-deployment created

# Query the rollout status
kubectl rollout status deployment.apps/nginx-deployment created

# Additionally query the status of the PODs
# It transitions from ContainerCreating -> Running
kubectl get pod

# List services exposed
minikube service list -p nginx-demo
***
|-------------|------------|--------------|-----|
|  NAMESPACE  |    NAME    | TARGET PORT  | URL |
|-------------|------------|--------------|-----|
| default     | kubernetes | No node port |     |
| kube-system | kube-dns   | No node port |     |
|-------------|------------|--------------|-----|
***

# Create 2 additional services 
# hello-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello
spec:
  replicas: 2
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 100%
  selector:
    matchLabels:
      app: hello
  template:
    metadata:
      labels:
        app: hello
    spec:
      affinity:
        # ⬇⬇⬇ This ensures pods will land on separate hosts
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions: [{ key: app, operator: In, values: [hello] }]
              topologyKey: "kubernetes.io/hostname"
      containers:
        - name: hello-from
          image: pbitty/hello-from:latest
          ports:
            - name: http
              containerPort: 80
      terminationGracePeriodSeconds: 1

# hello-svc.yaml
apiVersion: v1
kind: Service
metadata:
  name: hello
spec:
  type: NodePort
  selector:
    app: hello
  ports:
    - protocol: TCP
      nodePort: 31000
      port: 80
      targetPort: http

# Apply the deployments
kubectl apply -f /u/k8s/apps/hello-deployment.yaml
# Output --> deployment.apps/hello created

kubectl apply -f /u/k8s/apps/hello-svc.yaml
# Output --> service/hello created

# Verify the service is running
minikube service list -o wide
|-------------|------------|--------------|---------------------------|
|  NAMESPACE  |    NAME    | TARGET PORT  |            URL            |
|-------------|------------|--------------|---------------------------|
| default     | hello      |           80 | http://192.168.58.2:31000 |
| default     | kubernetes | No node port |                           |
| kube-system | kube-dns   | No node port |                           |
|-------------|------------|--------------|---------------------------|

# Get the IP addresses of the Nodes (192.168.58.2 & 192.168.58.3)
kubectl get nodes -o wide

# Get the names of the running PODs 
kubectl get pod
NAME                               READY   STATUS    RESTARTS   AGE
hello-66cff8ff7b-7j5f9             1/1     Running   0          103s
hello-66cff8ff7b-kwhrm             1/1     Running   0          103s
nginx-deployment-b55dcc56f-4x2q2   1/1     Running   0          14m
nginx-deployment-b55dcc56f-q59gn   1/1     Running   0          14m

# Test the deployment
curl http://192.168.58.2:31000
# output --> Hello from hello-66cff8ff7b-7j5f9

# Running it a few more times gets you from the other pod
curl http://192.168.58.2:31000
Hello from hello-66cff8ff7b-7j5f9 (10.244.1.3)

curl http://192.168.58.2:31000
Hello from hello-66cff8ff7b-kwhrm (10.244.0.4)


```

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































