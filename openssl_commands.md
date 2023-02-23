
#### Generate a Private Key and Public Cert
```
openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
```

#### Check to see if a cert is good
```
openssl x509 -noout -text -in minica.pem 
```

#### Check when a certificate expires
```
openssl x509  -noout -text -in /etc/kubernetes/pki/etcd/server.crt | grep Validity -A2
```

#### How to use minica to generate certs for Splunk
[Using minica with Splunk](https://idelta.co.uk/minica-easily-generate-certificates/)
