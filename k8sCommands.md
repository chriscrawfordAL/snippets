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

Create role, clusterrole
```
k create clusterrole gianna-additional --verb=create --resource=pods --resource=deployments
```

Assign the clusterrole to the security namespace for user gianna
```
k -n security create rolebinding gianna-additional --clusterrole=gianna-additional --user=gianna
```
