# Image - Ubuntu 14.04 LTS cloud-image

`https://www.dropbox.com/sh/0dgcaxc2u7cbfgi/AAAgnS87aYXRp6HJzK7oWSrma?dl=0`

Includes:

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

Use nova get-vnc-console etc. or SPICE to access instance.

**WATCH OUT**: If using the OpenStack Dashboard VNC client, the keyboard layout may be not the one you're using locally. So beware when entering usernames and passwords (watch for z/y i.e. on German/Englisch keyboards).

## Cloud.cfg

in /etc/cloud/cloud.cfg:

- lock_passwd: False

## DevStack glance image-create

Run in devstack folder: `source openrc admin admin` to switch to admin-user.
Then run `glance image-create --name "Ubuntu-14.04" --is-public true --disk-format qcow2 --file ../Downloads/ubuntu-14.04-openstack-qcow2.img --container-format bare`

## Convert VirtualBox Image to OpenStack

### Prerequisites

The image must have installed the packages cloud-init, cloud-utils, cloud-initramfs-growroot. Also a password login must be enabled in cloud.cfg. 

**WARNING**: after executing these steps, the image cannot be booted anynmore in VirtualBox (without providing a cloud-init mock). So always execute these steps at last.

Copy and execute with sudo the script `cloud-init-script.sh` on the image. 

### Convert vdi to qcow2 img

run `image-virtualbox-to-openstack.sh <FULL-IMAGE-PATH-TO-VDI-SNAPSHOT>`

**WARNING**: Specify the path to the SNAPSHOT of the image, otherwise the snapshots are ignored and only the base vdi will be converted.

## Details

The following files have been edited:

- /etc/default/grub and then run update-grub to enable serial console on OpenStack
- /etc/network/interfaces
- openssh-server config files to enable password login


