# Instance

In this folder and sub-folders goes the (virtual machine) instance related files and information.

## Deployment

Independent from OpenStack installation.

- To generate a single installation script run `make` in this folder.
- This will generate a `instance-setup.sh` file, which must be run in each instance to configure the instance, by passing it as a user-data script.

## Operating System

- Ubuntu 14.04 LTS

## Bugs

- Graphical Login must be issued twice for LDAP users due to Ubuntu bugs in lightdm.

