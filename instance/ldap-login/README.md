# LDAP Login in Instances

A user must be able to log into the instance (ubuntu) with his LDAP credentials.

The required configuration for Ubuntu can be found in this directory.

- The client (Ubuntu instance) always contacts the LDAP server to authenticate the user.
- The client is not allowed to change the password for the user in the LDAP server.
- The client restricts the users who are allowed to login via LDAP to a single user. This must be injected via the cloud-init user-data field. This ensures that 1 instance maps to exactly 1 user.
- The client allows to login with graphical login interface

## LDAP Requirements

- uid
- uidNumber
- gidNumber
- homeDirectory

or similar (can be mapped).

## HTWG LDAP

URL: `ldap.htwg-konstanz.de`

BaseDN: dc=fh-konstanz,dc=de

User: ou=users,dc=fh-konstanz,dc=de

## Script notes

Run the script `install.sh` to configure the system for LDAP. 

### Relevant files

- /etc/nsswitch.conf Adding "ldap" as authentication module
- /etc/ldap.conf Configuring the LDAP and overriding/mapping values
- /etc/pam.d/common-session Creating home directory
- /etc/security/group.conf Assigning groups for LDAP users
- /etc/pam.d/common-auth Adding PAM groups module
- /etc/group Adding group for LDAP users
- /etc/lightdm/lightdm.conf for the graphical login (greeter)

ldap.conf can be customized to map the login attribute (default: uid) and groups from ldap. Overriding of values (home dir etc.) via `nss_override_attribute_value`.

We need to override uidNumber, gidNumber, homeDirectory and loginShell.

Default groups on Ubuntu 14.04: $username adm cdrom sudo dip plugdev lpadmin sambashare

## Testing

Use Apache Directory Studio to browse any directory.

## References

Useful is https://help.ubuntu.com/community/LDAPClientAuthentication .