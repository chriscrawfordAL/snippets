Set StorageClass as default:

```
kubectl patch storageclass <storageclass name> -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}
```
