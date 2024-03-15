
fix BorderLeaf1#

conf
interface Ethernet47
no  channel-group 999 
no ip address
no desc
interface Ethernet48
no desc
no  channel-group 999 
interface Ethernet49/1
switchport 
no ip address
interface Ethernet50/1
switchport
no ip address
interface Ethernet47
no switchport
ip address 10.14.2.8/31
interface Ethernet48
no switchport 
ip address 10.14.1.8/31
end