## hostNetwork: true
```
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 4 # Update the replicas from 2 to 4
  template:
    metadata:
      labels:
        app: nginx
    spec:
      hostNetwork: true
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```
This only work on the host where the pod is running, but exposes the port

```
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 4 # Update the replicas from 2 to 4
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
          hostPort: 8080
```
```
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 4 # Update the replicas from 2 to 4
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```
```
apiVersion: v1
kind: Service
metadata:
  name: nginx-deployment
  namespace: default
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: nginx
  sessionAffinity: None
  type: NodePort
status:
  loadBalancer: {}
```

kubectl get svc

 
## Expose Service:

kubectl -n k8shacktenant expose pod/splunk-s1-standalone-0 --type="NodePort" --port 8000

## Port Forward:

kubectl port-forward splunk-s1-standalone-0 8000

## Match the service to the label
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world-example
spec:
  selector:
    matchLabels:
      run: hello-example
  replicas: 2
  template:
    metadata:
      labels:
        run: hello-example
    spec:
      containers:
        - name: hello-world-example
          image: gcr.io/google-samples/node-hello:1.0
          ports:
            - containerPort: 8080
              protocol: TCP
---
apiVersion: v1
kind: Service
metadata:
  name: hello-world-service-example
spec:
  selector:
    run: hello-example
  ports:
  - name: http-hello
    protocol: TCP
    port: 8080
    targetPort: 8080
  type: NodePort
```

