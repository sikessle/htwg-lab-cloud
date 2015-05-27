# Image - Ubuntu 14.04 LTS cloud-image

Includes:

- VNC
- Unity as Desktop Environment
- Dropbox
- cloud-init, cloud-utils, cloud-initramfs-growroot packages
- git
- openssh-server (password auth not disabled)
- vim
- OpenOffice
- Firefox 
- and other default applications

## Credentials

Username: ubuntu (full name: HTWG Lab Cloud)
Password: ubuntu

### SSH

To ssh into the machine (while not in openstack), use the given ssh-key file: `ssh -i ssh-key ubuntu@<ip-of-vm>`

### VNC

Use any VNC Viewer to connect to the ip address of the vm and log in.

## Cloud.cfg

in /etc/cloud/cloud.cfg:

- lock_passwd: False