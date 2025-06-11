# FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| FABRIC | l3leaf | Leaf1 | 10.14.34.245/24 | 7050SX-64 | Provisioned | - |
| FABRIC | l3leaf | Leaf2 | 10.14.34.244/24 | 7050SX-64 | Provisioned | - |
| FABRIC | l3leaf | Leaf3 | 10.14.34.243/24 | 7050SX-64 | Provisioned | - |
| FABRIC | l3leaf | Leaf4 | 10.14.34.242/24 | 7050SX-64 | Provisioned | - |
| FABRIC | l3leaf | Leaf5 | 10.14.34.241/24 | 7050SX-64 | Provisioned | - |
| FABRIC | l3leaf | Leaf7 | 10.14.34.240/24 | 7050SX-64 | Provisioned | - |
| FABRIC | spine | Spine1 | 10.14.34.247/24 | 7050QX-32S | Provisioned | - |
| FABRIC | spine | Spine2 | 10.14.34.246/24 | 7050QX-32S | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | Leaf1 | Ethernet47 | mlag_peer | Leaf2 | Ethernet47 |
| l3leaf | Leaf1 | Ethernet48 | mlag_peer | Leaf2 | Ethernet48 |
| l3leaf | Leaf1 | Ethernet49/1 | spine | Spine1 | Ethernet6/1 |
| l3leaf | Leaf1 | Ethernet51/1 | spine | Spine2 | Ethernet6/1 |
| l3leaf | Leaf2 | Ethernet49/1 | spine | Spine1 | Ethernet7/1 |
| l3leaf | Leaf2 | Ethernet51/1 | spine | Spine2 | Ethernet7/1 |
| l3leaf | Leaf3 | Ethernet47 | mlag_peer | Leaf4 | Ethernet47 |
| l3leaf | Leaf3 | Ethernet48 | mlag_peer | Leaf4 | Ethernet48 |
| l3leaf | Leaf3 | Ethernet49/1 | spine | Spine1 | Ethernet8/1 |
| l3leaf | Leaf3 | Ethernet51/1 | spine | Spine2 | Ethernet8/1 |
| l3leaf | Leaf4 | Ethernet49/1 | spine | Spine1 | Ethernet9/1 |
| l3leaf | Leaf4 | Ethernet51/1 | spine | Spine2 | Ethernet9/1 |
| l3leaf | Leaf5 | Ethernet49/1 | spine | Spine1 | Ethernet1 |
| l3leaf | Leaf5 | Ethernet51/1 | spine | Spine2 | Ethernet1 |
| l3leaf | Leaf7 | Ethernet49/1 | spine | Spine1 | Ethernet2 |
| l3leaf | Leaf7 | Ethernet51/1 | spine | Spine2 | Ethernet2 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.255.255.0/26 | 64 | 24 | 37.5 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| Leaf1 | Ethernet49/1 | 10.255.255.1/31 | Spine1 | Ethernet6/1 | 10.255.255.0/31 |
| Leaf1 | Ethernet51/1 | 10.255.255.3/31 | Spine2 | Ethernet6/1 | 10.255.255.2/31 |
| Leaf2 | Ethernet49/1 | 10.255.255.5/31 | Spine1 | Ethernet7/1 | 10.255.255.4/31 |
| Leaf2 | Ethernet51/1 | 10.255.255.7/31 | Spine2 | Ethernet7/1 | 10.255.255.6/31 |
| Leaf3 | Ethernet49/1 | 10.255.255.9/31 | Spine1 | Ethernet8/1 | 10.255.255.8/31 |
| Leaf3 | Ethernet51/1 | 10.255.255.11/31 | Spine2 | Ethernet8/1 | 10.255.255.10/31 |
| Leaf4 | Ethernet49/1 | 10.255.255.13/31 | Spine1 | Ethernet9/1 | 10.255.255.12/31 |
| Leaf4 | Ethernet51/1 | 10.255.255.15/31 | Spine2 | Ethernet9/1 | 10.255.255.14/31 |
| Leaf5 | Ethernet49/1 | 10.255.255.17/31 | Spine1 | Ethernet1 | 10.255.255.16/31 |
| Leaf5 | Ethernet51/1 | 10.255.255.19/31 | Spine2 | Ethernet1 | 10.255.255.18/31 |
| Leaf7 | Ethernet49/1 | 10.255.255.21/31 | Spine1 | Ethernet2 | 10.255.255.20/31 |
| Leaf7 | Ethernet51/1 | 10.255.255.23/31 | Spine2 | Ethernet2 | 10.255.255.22/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.255.0.0/27 | 32 | 8 | 25.0 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | Leaf1 | 10.255.0.3/32 |
| FABRIC | Leaf2 | 10.255.0.4/32 |
| FABRIC | Leaf3 | 10.255.0.5/32 |
| FABRIC | Leaf4 | 10.255.0.6/32 |
| FABRIC | Leaf5 | 10.255.0.7/32 |
| FABRIC | Leaf7 | 10.255.0.8/32 |
| FABRIC | Spine1 | 10.255.0.1/32 |
| FABRIC | Spine2 | 10.255.0.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 10.255.1.0/27 | 32 | 6 | 18.75 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | Leaf1 | 10.255.1.3/32 |
| FABRIC | Leaf2 | 10.255.1.3/32 |
| FABRIC | Leaf3 | 10.255.1.5/32 |
| FABRIC | Leaf4 | 10.255.1.5/32 |
| FABRIC | Leaf5 | 10.255.1.7/32 |
| FABRIC | Leaf7 | 10.255.1.8/32 |
