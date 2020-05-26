Get cluster info
```
kubectl cluster-info
```

To view all pods running
```
kubectl get po -A
```

Example sorting pods by nodeName:
```
kubectl get pods -o wide --sort-by="{.spec.nodeName}"
```

Minikube
```
minikube start
minikube stop
```
Launch Dashboard
```
minikube dashboard
```

Increase mem of VB to 4GiB
```
minikube config set memory 4096
```
