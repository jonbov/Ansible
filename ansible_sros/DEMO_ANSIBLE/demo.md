host: 10.14.17.201


pwd
/home/cvpadmin/ansible_sros

ansible-playbook -i hosts.ini playbooks/sros_underlay_push.yml 
show system lldp nei
show router route-table

configure/service
info
ansible-playbook -i hosts.ini playbooks/sros_vprn_create.yml 
info
show router 100 route-table
ping router 100

ansible-playbook -i hosts.ini playbooks/sros_sr_create.yml 
show router 100 route-table
ping router 100


ansible-playbook -i hosts.ini playbooks/AWX_sros_delete_config_files.yml 
file dir
ansible-playbook -i hosts.ini playbooks/AWX_sros_reboot.yml 
