## Install required packages:
```
yum install sssd realmd oddjob oddjob-mkhomedir adcli samba-common samba-common-tools krb5-workstation openldap-clients policycoreutils-python
```

## Modify /etc/hosts file and add AD server:
```
<IP> <FQDN> adserver
```

## Connect to AD Server:
```
realm join --user=Administrator <FQDN of AD Server> 
<Enter Administrator or Bind password>
```
