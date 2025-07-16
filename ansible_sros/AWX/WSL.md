WSL
https://learn.microsoft.com/en-us/windows/wsl/install
Powershell, run as administrator

wsl --install

wsl --list --verbose
  NAME            STATE           VERSION
* Ubuntu-22.04    Stopped         2

wsl --list --online

start:
wsl --distribution Ubuntu-22.04

stop:
wsl --terminate Ubuntu-22.04


Visual studio code:
skriv 'code'
jonbov@JHB-Matebook-X:/mnt/c/WINDOWS/system32$ code
jonbov@JHB-Matebook-X:/mnt/c/WINDOWS/system32$


jonbov@JHB-Matebook-X:/mnt/c/WINDOWS/system32$ ip addr show dev eth0
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:f8:06:ed brd ff:ff:ff:ff:ff:ff
    inet 172.29.99.223/20 brd 172.29.111.255 scope global eth0


