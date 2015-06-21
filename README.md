![HTWG Lab Cloud](design/logo-large.png?raw=true)

OpenStack based cloud platform for the HTWG Laboraties.

# Branching/Issues/Folders

- Put devstack related files to "devstack" and virtual machine instance related files to "instance"
- Branch per feature
- Merge if feature works flawless to master
- GitHub Issues to manage Features, Bugs, etc.

# Deployment on Ubuntu 14.04

Run `deploy.sh` in this folder as normal user in your Ubuntu 14.04 machine (which will be the HTWG Cloud Lab Host).

# Deployment with VirtualBox

## Requirements

- Vagrant
- VirtualBox

## Running

Configuration:

- Vagrantfile adjust eth2 IP
- devstack/local.conf adjust FLOATING_RANGE 
- devstack/local.conf adjust LAB_CLOUD_PUBLIC_IP (should match eth2 of Vagrantfile)

Running: 

- Run `vagrant up` in this folder to bring the machine up
- `vagrant ssh` to ssh in machine
- `vagrant destroy` to clean up everything and delete all traces

