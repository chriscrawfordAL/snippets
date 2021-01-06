Here is the full example with creating admin user and getting token:

Decode ca.crt from kubeconfig and store in ~/tmp/ca.crt

Creating a admin / service account user called k8sadmin
```
kubectl create serviceaccount k8sadmin -n kube-system
```
Give the user admin privileges
```
kubectl create clusterrolebinding k8sadmin --clusterrole=cluster-admin --serviceaccount=kube-system:k8sadmin
```
Get the token
```
kubectl -n kube-system describe secret $(sudo kubectl -n kube-system get secret | (grep k8sadmin || echo "$_") | awk '{print $1}') | grep token: | awk '{print $2}'
```
Run a curl command:
```
curl -k https://ip-10-20-1-36.us-west-2.compute.internal:10000/apis/storage.k8s.io/v1/storageclasses --header "Authorization: Bearer $TOKEN" --cacert ~/tmp/ca.crt
```
