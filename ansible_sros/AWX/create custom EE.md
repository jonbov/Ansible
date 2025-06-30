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

mkdir EE_project_directory && cd EE_project_directory
  add 4 files to EE_project_directory:
  execution-environment.yml
  requirements.yml
  requirements.txt
  bindep.txt
-(Sample files on )
ls -ll
  -rw-rw-r-- 1 netnordic netnordic   41 Jun 30 04:47 bindep.txt
  -rw-rw-r-- 1 netnordic netnordic 1009 Jun 30 04:47 execution-environment.yml
  -rw-rw-r-- 1 netnordic netnordic   55 Jun 30 04:47 requirements.txt
  -rw-rw-r-- 1 netnordic netnordic  146 Jun 30 04:47 requirements.yml

verify awx-ee on quay-io:
https://quay.io/repository/ansible/awx-ee?tab=tags



ansible-builder build -t sros_automation -v 3
-build takes approx 20 minutes












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

