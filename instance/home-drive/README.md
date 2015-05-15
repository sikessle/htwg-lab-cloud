# Mount home drive from HTWG

The user's home drive from the HTWG must be mounted on login.

- Mount home drive (z-drive) at login as "home-drive"
- Add directory to sidebar in nautilus

## HTWG home drive

Lies in `smb://homedrive.htwg-konstanz.de/home`

## Required Packages

- libpam_mount
- cifs-utils

## Script notes

Involved files: 

- /etc/security/pam_mount.conf.xml
- ~/pam_mount.conf.xml (created)

