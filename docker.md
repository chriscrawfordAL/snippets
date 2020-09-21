## Configure Docker to use Proxy
modify /etc/systemd/system/docker.service.d/docker-proxy.conf
add:
```
[Service]
Environment="HTTP_PROXY=http://web-proxy.corp.hpecorp.net:8080"
Environment="HTTPS_PROXY=http://web-proxy.corp.hpecorp.net:8080"
```

## Configure Docker to authenticate
