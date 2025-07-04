https://developers.redhat.com/articles/2023/05/08/how-create-execution-environments-using-ansible-builder#installing_the_execution_environment_builder

disk size:
ensure 48GB disk, mounted as /
verify with:
df -i
sudo cfdisk
****************************
sudo -i
cd /opt
mkdir ansible
cd ansible

apt update
apt upgrade
apt install make
apt install jq

#install Podman and Ansible-Builder


sudo apt-get -y install ansible
sudo apt-get -y install podman
sudo apt install python3-virtualenv
sudo apt install python3.10-venv

#verify Podman
podman images
podman ps -a

quit sudo (exit or ctrl-D)
cd /opt/ansible

#run in virtual environment

python3 -m venv venv-ee
source venv-ee/bin/activate
cd venv-ee/

#inside venv:
pip install ansible-builder

ansible-builder --help

ansible-builder -h build 
pip install --upgrade pip

mkdir EE_project_directory && cd EE_project_directory
  add 4 files to EE_project_directory:
  execution-environment.yml
  requirements.yml
  requirements.txt
  bindep.txt
-(Sample files on https://github.com/jonbov/Ansible/tree/master/ansible_sros/AWX/EE_project_directory)
ls -ll
  -rw-rw-r-- 1 netnordic netnordic   41 Jun 30 04:47 bindep.txt
  -rw-rw-r-- 1 netnordic netnordic 1009 Jun 30 04:47 execution-environment.yml
  -rw-rw-r-- 1 netnordic netnordic   55 Jun 30 04:47 requirements.txt
  -rw-rw-r-- 1 netnordic netnordic  146 Jun 30 04:47 requirements.yml

verify awx-ee on quay-io:
https://quay.io/repository/ansible/awx-ee?tab=tags



ansible-builder build -t network_automation -v 3
-build takes approx 20 minutes
[4/4] COMMIT sros_automation
--> 8d5d8e4b186
Successfully tagged localhost/network_automation:latest

Complete! The build context can be found at: /opt/ansible/venv-ee/EE_project_directory/context

podman images
REPOSITORY                         TAG         IMAGE ID      CREATED      SIZE
localhost/network_automation       latest      e3c6e03047ed  4 days ago   935 MB
quay.io/jonbov/network_automation  latest      e3c6e03047ed  4 days ago   935 MB
quay.io/centos/centos              stream9     ab9123964b93  2 weeks ago  171 MB


podman create -it --name network_ee localhost/network_automation:latest
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman create -it --name network_ee localhost/network_automation:latest
e62eab8c21309e14dd14f5ea82bf4e17a52e37b2400b810a3af25dd673b09b0c

podman ps -a
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman ps -a
  CONTAINER ID  IMAGE                             COMMAND     CREATED         STATUS      PORTS       NAMES
  d7449d99a782  localhost/sros_automation:latest  bash        46 seconds ago  Created                 network_ee
#check ststus "Created"

podman start network_ee 
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman start network_ee 
  network_ee

podman ps -a
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman ps -a
  CONTAINER ID  IMAGE                             COMMAND     CREATED        STATUS            PORTS       NAMES
  d7449d99a782  localhost/sros_automation:latest  bash        2 minutes ago  Up 2 seconds ago              network_ee
#check status 'UP"

podman exec -it network_ee python3 --version
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman exec -it network_ee python3 --version
  Python 3.9.21

podman exec -it network_ee ansible-galaxy collection list
#use grep to search
podman exec -it network_ee ansible-galaxy collection list | grep sros
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman exec -it network_ee ansible-galaxy collection list

  # /usr/local/lib/python3.9/site-packages/ansible_collections
  Collection                    Version
  ----------------------------- -------
  amazon.aws                    6.5.0  
  ansible.netcommon             5.3.0  
  ansible.posix                 1.5.4  

podman exec -it network_ee ansible --version
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman exec -it network_ee ansible --version
  ansible [core 2.15.13]
    config file = None
    configured module search path = ['/runner/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
    ansible python module location = /usr/local/lib/python3.9/site-packages/ansible
    ansible collection location = /runner/.ansible/collections:/usr/share/ansible/collections
    executable location = /usr/local/bin/ansible
    python version = 3.9.21 (main, Feb 10 2025, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-5)] (/usr/bin/python3)
    jinja version = 3.1.6
    libyaml = True

podman exec -it network_ee ansible-community --version
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman exec -it network_ee ansible-community --version
  Ansible community version 8.7.0

podman exec -it network_ee /bin/bash
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman exec -it network_ee /bin/bash
  bash-5.1$ 
  bash-5.1$ 

podman stop network_ee
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman stop network_ee
  network_ee
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman ps -a
  CONTAINER ID  IMAGE                             COMMAND     CREATED         STATUS                       PORTS       NAMES
  d7449d99a782  localhost/sros_automation:latest  bash        16 minutes ago  Exited (137) 20 seconds ago              network_ee

#remove container:
podman rm network_ee
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman rm network_ee
  d7449d99a78281df8fa1895a93512621b0494579386aef436d3d4aaadd73e8d3
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman ps -a
  CONTAINER ID  IMAGE       COMMAND     CREATED     STATUS      PORTS       NAMES
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman images
  REPOSITORY                 TAG         IMAGE ID      CREATED         SIZE
  localhost/sros_automation  latest      8d5d8e4b186e  20 minutes ago  918 MB
#observe container removed, image still in place

podman tag localhost/network_automation:latest quay.io/jonbov/network_automation
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman tag localhost/network_automation:latest quay.io/jonbov/network_automation
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman images
  REPOSITORY                              TAG         IMAGE ID      CREATED         SIZE
  localhost/network _automation               latest      8d5d8e4b186e  36 minutes ago  918 MB
  quay.io/jonbov/network_automation          latest      8d5d8e4b186e  36 minutes ago  918 MB

podman login quay.io
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman login quay.io
  Username: jonbov
  Password: 
  Login Succeeded!
#Password in Lastpass


podman push quay.io/jonbov/network_automation:latest 
  (venv-ee) netnordic@no-awx-204:/opt/ansible/venv-ee/EE_project_directory$ podman push quay.io/jonbov/sros_automation:latest 
  Getting image source signatures
  Copying blob fedb19017a53 done  
  Copying blob 25276956a05a done  
  Copying blob 0ab502f731de done  
  Copying blob 99903deacf37 done  
  Copying blob fc53407d81f4 done  
  Copying blob c79f3694349f skipped: already exists  
  Copying blob 49d2f32fe31b done  
  Copying blob 2ea58f2517c5 done  
  Copying blob 44d07f5e9e9a done  
  Copying blob cf346fb84bdc done  
  Copying blob 96d8adae63c0 done  
  Copying blob 4c4210b62de4 done  
  Copying blob db86868b918b done  
  Copying blob 0cb8a9a3ad2c done  
  Copying config 8d5d8e4b18 done  
  Writing manifest to image destination
  Storing signatures

Verify image is updated to repository:
https://quay.io/repository/jonbov/network_automation?tab=tags
Set Repository Visibility to "Public"
Fetch tag from repository, and import into AWX "Execution Environments"
(Tag: Podman pull)



******************************

cat <<EOT >> execution-environment.yml
---
version: 1
dependencies:
  galaxy: requirements.yml
EOT

cat <<EOT >> requirements.yml
---
collections:
  - name: servicenow.itsm
EOT

ansible-builder build -v3 -t custom-ee

