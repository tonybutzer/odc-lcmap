# jupyterhub

## references

## prerequisites

### kubernetes
### kops
### kubctl
### awscli

## installing

follow the tutorial here:
- https://github.com/kubernetes/kops/blob/master/docs/aws.md

> Or
here:
- https://www.youtube.com/watch?v=TXGmHzELQ5A
- https://github.com/advithdevopsworld/kubernetes/blob/master/KOPS%20installation%20in%20aws


## example

### 1. Console create ec2 instance/server with 12 gig disk
- from jose rdp firefox
- aws url = 
- aws account
- 2factor google authenticator tablet


```bash
 curl -LO https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64
    2  chmod +x kops-linux-amd64
    3  apt-get update
    4  apt-get install -y python3-pip
    5  pip3 install awscli
```

https://github.com/tonybutzer/ga-aws-butzer/blob/3e3d32ecc8735ba906288125cb10d7c5dc2b120b/deploy/bucket/create-OPT-bucket.sh

### install kops

- see Linux secsion from https://github.com/kubernetes/kops

#### install kubctl

## issues

apt - says use dpkg to fix


