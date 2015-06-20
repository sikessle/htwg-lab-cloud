# Networking

This project uses as a first step the **nova-network** feature and not neutron.

## Flat Networking

We use a flat network, where every instance can reach other instances.

## Accessing DevStack from outside the VM

### DevStack

See local.conf.

### VirtualBox

#### VirtualBox Network Settings

Network -> Host-Only: 
- vboxnet0
- No DHCP
- IP Address: 172.16.0.254
- Netmask: 255.255.0.0

#### DevStack VM Settings

Adapter 1:
- NAT

Adapter 2:
- Host-Only: vboxnet0


### DevStack VM Ubuntu Network Config

/etc/network/interfaces: see interfaces.txt


