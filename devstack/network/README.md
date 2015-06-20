# Networking

This project uses as a first step the **nova-network** feature and not neutron.

## Flat Networking

We use a flat network, where every instance can reach other instances.

## Accessing DevStack from outside the VM

### DevStack

local.conf:

	HOST_IP=172.16.0.1
	FLAT_INTERFACE=br100 ?????? NOT WORKING
	PUBLIC_INTERFACE=eth1
	FLOATING_RANGE=172.16.0.128/25

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

/etc/network/interfaces:

	auto lo
	iface lo inet loopback

	# The primary network interface
	auto eth0
	iface eth0 inet dhcp

	auto br100
	iface br100 inet static
	address 172.16.0.1
	netmask 255.255.0.0
	network 172.16.0.0
	broadcast 172.16.255.255
	    bridge_ports eth1
	    bridge_stp off
	    bridge_maxwait 0
	    bridge_fd 0


