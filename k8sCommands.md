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

#### Security
Create role, clusterrole
```
k create clusterrole gianna-additional --verb=create --resource=pods --resource=deployments
```

Assign the clusterrole to the security namespace for user gianna
```
k -n security create rolebinding gianna-additional --clusterrole=gianna-additional --user=gianna
```

#### ETCDD
Take Snapshot:
```
ETCDCTL_API=3 etcdctl snapshot save /etc/etcd-snapshot.db \
--cacert /etc/kubernetes/pki/etcd/ca.crt \
--cert /etc/kubernetes/pki/etcd/server.crt \
--key /etc/kubernetes/pki/etcd/server.key
```

#### Shorthand commands

```
alias do='-o yaml --dry-run=client'
k run p2-pod --image=nginx:1.17-alpine $do > p2.yaml
```
```
k -n project-hamster expose pod p2-pod --name p2-service --port 3000 --target-port 80
````

#### Look at CPU and MEM Usage in a Namespace
```
kubectl -n <namespace> get pods -o custom-columns=NAME:metadata.name,MEM_LIMIT:spec.containers[*].resources.limits.memory,MEM_REQUEST:spec.containers[*].resources.requests.memory,CPU_LIMIT:spec.containers[*].resources.limits.cpu,CPU_REQUEST:spec.containers[*].resources.requests.cpu
```
