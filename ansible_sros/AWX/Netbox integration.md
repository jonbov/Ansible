
Get AIP key from Netbox
    in Netbox:
    click on username, upper right corner, select "API Token"
    Add Token.
    record key: 943aea909336d4dc2eea388c1df776c5e1c9d3e9

Ansible:
    install netbox collection if not already in place: (should be if ansible was installed with "pip install ansible")
    -ansible-galaxy collection install netbox.netbox
    verify:
    cvpadmin@ansible-vmbovrenet:~/ansible_sros$ ansible-galaxy collection list | grep netbox
    netbox.netbox                            3.20.0 

Sample:
01_netbox_connect_using_api.yml
---
  - name: test playbook
    hosts: localhost
    connection: local
    gather_facts: no
    vars:
      netbox_url: http://10.14.17.203:8000/
      netbox_token: 943aea909336d4dc2eea388c1df776c5e1c9d3e9
    tasks:
      - name: get devices
        uri:
          url: "{{ netbox_url }}/api/dcim/devices"
          method: GET
          headers:
            Authorization: "Token {{ netbox_token }}"
            Accept: 'application/json'
          return_content: yes
          body_format: json
          status_code: [200,201]
          validate_certs: false
        register: netbox_devices
        run_once: yes
      - debug:
          var: netbox_devices

02_inventory.yml
--- 
  plugin: netbox.netbox.nb_inventory
  api_endpoint:  http://10.14.17.203:8000
  token: 943aea909336d4dc2eea388c1df776c5e1c9d3e9
  validate_certs: false
  group_by:
    - device_roles
  #  _devices
    - manufacturers

  run playbook:
  ansible-inventory --list -i 


cvpadmin@ansible-vmbovrenet:~/ansible_sros$ 
ansible-playbook -i playbooks/Netbox/02_inventory.yml playbooks/AWX_sros_show_info_name.yml -u admin -k  -vvv
ansible-playbook playbooks/AWX_ping.yml

ansible-inventory -v --list -i netbox_inventory.yml

ansible-inventory -i playbooks/Netbox/02_inventory.yml --graph
@all:
  |--@ungrouped:
  |--@device_roles_core:
  |  |--SAR-8-200
  |  |--SAR-8-201
  |  |--SAR-8-202
  |--@manufacturers_nokia:
  |  |--SAR-8-200
  |  |--SAR-8-201
  |  |--SAR-8-202
  |  |--SAR-Hc-208
  |  |--SAR-Hc-209
  |--@device_roles_access:
  |  |--SAR-Hc-208
  |  |--SAR-Hc-209

  ansible-inventory -i hosts.ini --graph
@all:
  |--@ungrouped:
  |--@nn_sros:
  |  |--SAR-8-200
  |  |--SAR-8-201
  |  |--SAR-8-202
  |  |--SAR-8-203
  |  |--SAR-8-204
  |  |--SAR-8-205
  |  |--SAR-Hc-208
  |  |--SAR-Hc-209
  |--@nn_mdcli:
  |  |--IXR-e-210
  |--@gk15_sros:
  |  |--SAR-8-206
  |  |--SAR-8-207
  |--@gk15_nps:
  |  |--nps.bovre.net