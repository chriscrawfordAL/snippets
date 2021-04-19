
#### Check to see if a cert is good
```
openssl x509 -noout -text -in minica.pem 
```

#### Check when a certificate expires
```
openssl x509  -noout -text -in /etc/kubernetes/pki/etcd/server.crt | grep Validity -A2
```
