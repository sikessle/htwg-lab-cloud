![HTWG Lab Cloud](design/logo-large.png?raw=true)

OpenStack based cloud platform for the HTWG Laboraties.

# Branching/Issues/Folders

- Put devstack related files to "devstack" and virtual machine instance related files to "instance"
- Branch per feature
- Merge if feature works flawless to master
- GitHub Issues to manage Features, Bugs, etc.

# Deployment on Ubuntu 14.04

## Requirements

See Vagrantfile for network config.

## Running

Run `deploy.sh` in this folder as normal user in your Ubuntu 14.04 machine (which will be the HTWG Lab Cloud Host).

# Deployment with VirtualBox

## Requirements

- Vagrant
- VirtualBox

## Running

Configuration:

- **Vagrantfile** adjust eth2 IP, so that it is an IP in your local real network.
- **devstack/local.conf** adjust `FLOATING_RANGE`, subnet of eth2 (mostly it is sufficient to change the ip to the ip of eth2)
- **devstack/local.conf** adjust `LAB_CLOUD_PUBLIC_IP` (should match eth2 of Vagrantfile)

Running: 

- Run `vagrant up` in this folder to bring the machine up
- `vagrant ssh` to ssh in machine
- `vagrant destroy` to clean up everything and delete all traces

## Without Vagrant

**Manually** configure VirtualBox VM:

- **eth0**: NAT
- **eth1**: Host-Only, no DHCP, static ip: 192.168.35.129
- **eth2**: Bridged, ip: 192.168.1.111

IP of eth2 can be changed, then you have to change it as well in `devstack/local.conf`.

Look out for `LAB_CLOUD_PUBLIC_IP` and `FLOATING_RANGE`. They should match your local network.

For example: If you have the IP `192.168.0.20`, then your router probably is in `192.168.0.1/24` subnet. Then configure the `LAB_CLOUD_PUBLIC_IP=192.168.0.111` and `FLOATING_RANGE=192.168.0.128/25`.