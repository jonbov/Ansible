https://developers.redhat.com/articles/2023/05/08/how-create-execution-environments-using-ansible-builder#installing_the_execution_environment_builder

#install Podman and Ansible-Builder
sudo apt-get -y install podman


#verify Podman
podman images
podman ps -a

#run in virtual environment
sudo apt install python3-virtualenv
python3 -m venv venv-ee-demo
source venv-ee-demo/bin/activate
cd venv-ee-demo/

#inside venv:
pip install ansible-builder

ansible-builder --help

ansible-builder -h build 

mkdir project_directory && cd project_directory

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

