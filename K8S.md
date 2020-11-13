#### Remove all Taints
```
kubectl taint nodes --all node-role.kubernetes.io/master-
```

#### Set StorageClass as default:

```
kubectl patch storageclass <storageclass name> -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}
```

#### Curl Command to API Server
```
curl --cert userbob.pem --key userBob-key.pem \  
--cacert /path/to/ca.pem \   
https://k8sServer:6443/api/v1/pods 
```

Provides the CURL command of any kubectl command
```
kubectl -v=10 <commands, i.e. get pods>
```

#### Kubetl Auth
```
$ kubectl auth can-i
```

#### Simple Pod
```
apiVersion: v1
kind: Pod
metadata:
    name: firstpod
spec:
    containers:
    - image: nginx
      name: stan
```
