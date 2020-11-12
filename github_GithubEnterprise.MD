### Set up RSA Key

Use ssh-gen to create id_rsa and id_rsa.pub.  Follow guide here if you don't already have these key.  Check your ~/.ssh directory first
https://www.freecodecamp.org/news/git-ssh-how-to/

### Create a git repo and load the key

* In your repo, goto settings and choose "Deploy Keys"
* Click "Add Deploy Key"
* Choose if you want to write files

### Check your login:

```
ssh -T git@github.hpe.com
```

### Clone your Repo
```
git clone git@github.hpe.com:chris-crawford/enterpriseFeaturesDemo.git
```

### Normal git operations :)
