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

#### Increase Image Pull Timeout

Option 1: Update kube-apiserver.yaml
The kube-apiserver.yaml file doesn’t have a flag for directly setting the image-pull-progress-deadline.
However, there is a requestion timeout option
 
--request-timeout duration     Default: 1m0s

An optional field indicating the duration a handler must keep a request open before timing it out. This is the default request timeout for requests but may be overridden by flags such as --min-request-timeout for specific types of requests.
 
Bumped up to 5m0s

Option 2:
Modify /etc/sysconfig/kubelet on the host where the offending pod is scheduled
edit the KUBELET_EXTRA_ARGS line to read:
     KUBELET_EXTRA_ARGS=--image-pull-progress-deadline=30m0s

