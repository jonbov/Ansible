Ubuntu version 22.04.2 LTS installed
-4 vCPU
-8GB RAM (8196)
-32GB or bigger disk (thin)
Partition should be minimum 32GB
sudo fdisk -l
Device     Start       End   Sectors Size Type
/dev/sda1   2048      4095      2048   1M BIOS boot
/dev/sda2   4096 100661247 100657152  48G Linux filesystem

netnordic@no-awx-205:~/ansible_sros$  lsb_release -a
  No LSB modules are available.
  Distributor ID: Ubuntu
  Description:    Ubuntu 22.04.2 LTS
  Release:        22.04
  Codename:       jammy

******************************************************************************
Install Ansible and virtual environment:

sudo apt install python3.10-venv
python3 -m venv .venv
source .venv/bin/activate
apt install ansible
ansible-galaxy collection install ansible.netcommon
ansible-galaxy collection install nokia.sros
pip install paramiko
sudo apt-get install -y python3-paramiko
apt install make

copy Ansible files to /home/netnordic/...

verify playbook run on SROS device
(.venv) netnordic@no-awx-205:~/ansible_sros$ ansible-playbook playbooks/sros_show_info_200.yml 

    PLAY [10.14.34.200] ****************

    TASK [get system information] ******
    ok: [10.14.34.200]

deactivate
(to get out of venv)

********************************************************************************
install Kubernetes k3s

https://www.youtube.com/watch?v=OLIktAb9-FY

install to /opt
ensure sufficient disk space for additional EEs.
Partition should be minimum 32GB
sudo fdisk -l
Device     Start       End   Sectors Size Type
/dev/sda1   2048      4095      2048   1M BIOS boot
/dev/sda2   4096 100661247 100657152  48G Linux filesystem

1: Install Kubernetes (k3s)
sudo -i 
(root@awx)
cd /opt

apt update
apt upgrade
apt install make
apt install jq

curl -sfL https://get.k3s.io   | sh -
kubectl version
  Client Version: v1.32.5+k3s1
  Kustomize Version: v5.5.0
  Server Version: v1.32.5+k3s1

********************************************************************************
install AWX

https://ansible.readthedocs.io/projects/awx-operator/en/latest/installation/basic-install.html

git clone https://github.com/ansible/awx-operator.git
#(sudo chmod 644 /etc/rancher/k3s/k3s.yaml)



cd awx-operator
export NAMESPACE=awx
kubectl create ns ${NAMESPACE}
sudo kubectl config set-context --current --namespace=awx

  !Command locks: RELEASE_TAG='curl -s https://api.github.com/repos/ansible/awx-operator/releases/latest | grep tag_name | cut -d '"' -f 4'
curl -s https://api.github.com/repos/ansible/awx-operator/releases/latest | grep tag_name | cut -d '"' -f 4
  2.19.1

git checkout 2.19.1
make deploy

create file "awx.yaml"
nano "awx.yaml" with content:
https://ansible.readthedocs.io/projects/awx-operator/en/latest/user-guide/advanced-configuration/containers-resource-requirements.html
---
apiVersion: awx.ansible.com/v1beta1
kind: AWX
metadata:
  name: awx-lab
spec:
  service_type: nodeport
  nodeport_port: 30080
  task_resource_requirements:
    requests:
      cpu: 100m
      memory: 128Mi
      ephemeral-storage: 100M
    limits:
      cpu: 2000m
      memory: 4Gi
      ephemeral-storage: 500M
  web_resource_requirements:
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 1000m
      memory: 4Gi
  ee_resource_requirements:
    requests:
      cpu: 100m
      memory: 64Mi
    limits:
      cpu: 1000m
      memory: 4Gi
  redis_resource_requirements:
    requests:
      cpu: 50m
      memory: 64Mi
    limits:
      cpu: 1000m
      memory: 4Gi
  rsyslog_resource_requirements:
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 1000m
      memory: 2Gi
  init_container_resource_requirements:
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 1000m
      memory: 2Gi

kubectl apply -f awx.yaml
    awx.awx.ansible.com/awx-lab created


***verify pods starting. some minutes**************

kubectl get pods -n awx
  NAME                                               READY   STATUS              RESTARTS   AGE
  awx-lab-postgres-15-0                             1/1     Running             0          3m28s
  awx-lab-task-7d46bbb4c8-f9bjx                     0/4     Init:0/2            0          100s
  awx-lab-web-5c7584fb64-c2tch                      0/3     ContainerCreating   0          105s
  awx-operator-controller-manager-58b7c97f4b-mm55z   2/2     Running             0          14m
(above startup takes some minutes)

kubectl get service -n awx
  NAME                                              TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
  awx-lab-postgres-15                              ClusterIP   None           <none>        5432/TCP       4m45s
  awx-lab-service                                  NodePort    10.43.43.163   <none>        80:31250/TCP   3m8s
  awx-operator-controller-manager-metrics-service   ClusterIP   10.43.36.118   <none>        8443/TCP       38h

kubectl get secret awx-lab-admin-password -o jsonpath="{.data.password}" | base64 --decode ; echo
7adDuUOUbWMQ6b1w7a8ZMNMFyIIG2SkI

http://awx.nrslab.eu:31250
admin / 7adDuUOUbWMQ6b1w7a8ZMNMFyIIG2SkI
admin / a4068becs

(https://galaxy.ansible.com/ui/token/)
  API token
  Use this token to authenticate the ansible-galaxy client.

  WARNING copy this token now. This is the only time you will ever see it.
  45e7440f5c837a0b6e024d1092f783d6a6223ce7


no-awx-204:
root@no-awx-204:~/awx-operator# kubectl get pods -n awx
NAME                                               READY   STATUS              RESTARTS   AGE
awx-lab-postgres-15-0                              1/1     Running             0          2m1s
awx-lab-task-6569979ccc-wnq7l                      0/4     Init:0/2            0          50s
awx-lab-web-674cd6bc69-hgg2x                       0/3     ContainerCreating   0          53s
awx-operator-controller-manager-58b7c97f4b-mpnp8   2/2     Running             0          3m29s

root@no-awx-204:~/awx-operator# kubectl get service -n awx
NAME                                              TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
awx-lab-postgres-15                               ClusterIP   None           <none>        5432/TCP       73s
awx-lab-service                                   NodePort    10.43.253.21   <none>        80:31864/TCP   12s
awx-operator-controller-manager-metrics-service   ClusterIP   10.43.54.27    <none>        8443/TCP       2m37s

root@no-awx-204:~/awx-operator# 
kubectl get secret awx-lab-admin-password -o jsonpath="{.data.password}" | base64 --decode ; echo
UYXS3KmMB6zcajONv2qdAFJbnBkgzcKn

http://10.14.17.204:31864


kubectl get secret awx-lab-admin-password -o jsonpath="{.data.password}" -n awx | base64 --decode ; echo
tjbAdSyRfS3VnIhHJNtdEAif8zZ8Hkuk

root@awx:~/awx-operator# kubectl get secrets -n awx
NAME                             TYPE                DATA   AGE
awx-lab-admin-password           Opaque              1      3h10m
awx-lab-app-credentials          Opaque              3      3h8m
awx-lab-broadcast-websocket      Opaque              1      3h10m
awx-lab-postgres-configuration   Opaque              6      3h10m
awx-lab-receptor-ca              kubernetes.io/tls   2      3h9m
awx-lab-receptor-work-signing    Opaque              2      3h8m
awx-lab-secret-key               Opaque              1      3h10m
redhat-operators-pull-secret     Opaque              1      3h11m 


Delete pod Unknown:
https://stackoverflow.com/questions/54478616/how-to-delete-a-pod-in-unknown-state-in-kubernetes
kubectl delete pod -n awx <pod_name> --grace-period=0 --force
root@awx:~# kubectl delete pod -n awx awx-lab-migration-24.6.1-mdxkj --grace-period=0 --force
Warning: Immediate deletion does not wait for confirmation that the running resource has been terminated. The resource may continue to run on the cluster indefinitely.
pod "awx-lab-migration-24.6.1-mdxkj" force deleted

Posd in  Init:
https://stackoverflow.com/questions/50075422/kubernetes-pods-hanging-in-init-state
 kubectl delete pods -n awx --all
kubectl delete service -n awx --all

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate


*********************************************************
Portainer k3s GUI
http://awx.nrslab.eu:30777
port 30777/30779
kubectl apply -n portainer -f https://raw.githubusercontent.com/portainer/k8s/master/deploy/manifests/portainer/portainer.yaml
https://docs.portainer.io/start/install-ce/server/kubernetes/baremetal


ansible-galaxy collection list
  # /root/.ansible/collections/ansible_collections
  Collection        Version
  ----------------- -------
  ansible.netcommon 8.0.0  
  ansible.utils     6.0.0  
  nokia.sros        1.6.0  
  # /usr/lib/python3/dist-packages/ansible_collections
  Collection                Version
  ------------------------- -------
  amazon.aws                1.4.0  
  ansible.netcommon         1.5.0  
  ansible.posix             1.1.1  


nano requirements.yml
---
collections:
  - name: kubernetes.core
    version: '>=2.3.2'
  - name: operator_sdk.util
    version: "0.5.0"
  - nokia.sros
    version: '>=1.6.0'
  - ansible.netcommon
    version: '>=8.0.0'




******************************************
git tag  (q to exit)
export VERSION=2.16.1
git checkout tags/2.16.1





doc: https://github.com/ansible/awx/blob/devel/INSTALL.md
apt install python3-pip



sudo -i
pip3 install awxkit
awx --help


***logs from install to new ubuntu 24.x server********************************

jonbov@awx:~$ 
jonbov@awx:~$ 
jonbov@awx:~$ sudo -i 
[sudo] password for jonbov: 
root@awx:~# 
root@awx:~# curl -sfL https://get.k3s.io   | sh -
kubectl version
[INFO]  Finding release for channel stable
[INFO]  Using v1.32.5+k3s1 as release
[INFO]  Downloading hash https://github.com/k3s-io/k3s/releases/download/v1.32.5+k3s1/sha256sum-amd64.txt
[INFO]  Downloading binary https://github.com/k3s-io/k3s/releases/download/v1.32.5+k3s1/k3s
[INFO]  Verifying binary download
[INFO]  Installing k3s to /usr/local/bin/k3s
[INFO]  Skipping installation of SELinux RPM
[INFO]  Creating /usr/local/bin/kubectl symlink to k3s
[INFO]  Creating /usr/local/bin/crictl symlink to k3s
[INFO]  Creating /usr/local/bin/ctr symlink to k3s
[INFO]  Creating killall script /usr/local/bin/k3s-killall.sh
[INFO]  Creating uninstall script /usr/local/bin/k3s-uninstall.sh
[INFO]  env: Creating environment file /etc/systemd/system/k3s.service.env
[INFO]  systemd: Creating service file /etc/systemd/system/k3s.service
[INFO]  systemd: Enabling k3s unit
Created symlink /etc/systemd/system/multi-user.target.wants/k3s.service → /etc/systemd/system/k3s.service.
[INFO]  systemd: Starting k3s
Client Version: v1.32.5+k3s1
Kustomize Version: v5.5.0
Server Version: v1.32.5+k3s1
root@awx:~# kubectl version
Client Version: v1.32.5+k3s1
Kustomize Version: v5.5.0
Server Version: v1.32.5+k3s1
root@awx:~# git clone https://github.com/ansible/awx-operator.git
Cloning into 'awx-operator'...
remote: Enumerating objects: 11117, done.
remote: Counting objects: 100% (22/22), done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 11117 (delta 4), reused 7 (delta 2), pack-reused 11095 (from 2)
Receiving objects: 100% (11117/11117), 3.80 MiB | 2.07 MiB/s, done.
Resolving deltas: 100% (6482/6482), done.
root@awx:~# sudo apt install jq
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
jq is already the newest version (1.7.1-3build1).
jq set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 117 not upgraded.
root@awx:~# cd awx-operator
root@awx:~/awx-operator# export NAMESPACE=awx
root@awx:~/awx-operator# kubectl create ns ${NAMESPACE}
namespace/awx created
root@awx:~/awx-operator# sudo kubectl config set-context --current --namespace=awx
Context "default" modified.
root@awx:~/awx-operator# curl -s https://api.github.com/repos/ansible/awx-operator/releases/latest | grep tag_name | cut -d '"' -f 4
2.19.1
root@awx:~/awx-operator# git checkout 2.19.1
Note: switching to '2.19.1'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at dd37ebd Update index.md (#1904)
root@awx:~/awx-operator# make deploy
Command 'make' not found, but can be installed with:
apt install make        # version 4.3-4.1build1, or
apt install make-guile  # version 4.3-4.1build1
root@awx:~/awx-operator# apt install make
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Suggested packages:
  make-doc
The following NEW packages will be installed:
  make
0 upgraded, 1 newly installed, 0 to remove and 117 not upgraded.
Need to get 180 kB of archives.
After this operation, 414 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu noble/main amd64 make amd64 4.3-4.1build2 [180 kB]
Fetched 180 kB in 1s (273 kB/s)
Selecting previously unselected package make.
(Reading database ... 84047 files and directories currently installed.)
Preparing to unpack .../make_4.3-4.1build2_amd64.deb ...
Unpacking make (4.3-4.1build2) ...
Setting up make (4.3-4.1build2) ...
Processing triggers for man-db (2.12.0-4build2) ...
Scanning processes...                                                                                                                                 
Scanning linux images...                                                                                                                              

Running kernel seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
root@awx:~/awx-operator# make deploy
Warning: resource namespaces/awx is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
namespace/awx configured
customresourcedefinition.apiextensions.k8s.io/awxbackups.awx.ansible.com created
customresourcedefinition.apiextensions.k8s.io/awxmeshingresses.awx.ansible.com created
customresourcedefinition.apiextensions.k8s.io/awxrestores.awx.ansible.com created
customresourcedefinition.apiextensions.k8s.io/awxs.awx.ansible.com created
serviceaccount/awx-operator-controller-manager created
role.rbac.authorization.k8s.io/awx-operator-awx-manager-role created
role.rbac.authorization.k8s.io/awx-operator-leader-election-role created
clusterrole.rbac.authorization.k8s.io/awx-operator-metrics-reader created
clusterrole.rbac.authorization.k8s.io/awx-operator-proxy-role created
rolebinding.rbac.authorization.k8s.io/awx-operator-awx-manager-rolebinding created
rolebinding.rbac.authorization.k8s.io/awx-operator-leader-election-rolebinding created
clusterrolebinding.rbac.authorization.k8s.io/awx-operator-proxy-rolebinding created
configmap/awx-operator-awx-manager-config created
service/awx-operator-controller-manager-metrics-service created
deployment.apps/awx-operator-controller-manager created
root@awx:~/awx-operator# kubectl get pods -n awx
NAME                                               READY   STATUS              RESTARTS   AGE
awx-operator-controller-manager-58b7c97f4b-64p6k   0/2     ContainerCreating   0          14s
root@awx:~/awx-operator# nano awx.yaml
root@awx:~/awx-operator# kubectl apply -f awx.yaml
awx.awx.ansible.com/awx-lab created
root@awx:~/awx-operator# kubectl get pods -n awx
NAME                                               READY   STATUS    RESTARTS   AGE
awx-operator-controller-manager-58b7c97f4b-64p6k   2/2     Running   0          99s
root@awx:~/awx-operator# kubectl get service -n awx
NAME                                              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
awx-operator-controller-manager-metrics-service   ClusterIP   10.43.220.190   <none>        8443/TCP   102s
root@awx:~/awx-operator# 