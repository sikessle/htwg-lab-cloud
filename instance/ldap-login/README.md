# LDAP Login in Instances

A user must be able to log into the instance (ubuntu) with his LDAP credentials.
The required configuration for Ubuntu can be found in this directory.

- The client (Ubuntu instance) always contacts the LDAP server to authenticate the user.
- The client is not allowed to change the password for the user in the LDAP server.
- The client restricts the users who are allowed to login via LDAP to a single user. This must be injected via the cloud-init user-data field. This ensures that 1 instance maps to exactly 1 user.
- The client allows to login via graphic login.

## LDAP Requirements

- uid
- uidNumber
- gidNumber
- homeDirectory

or similar (can be mapped).

## HTWG LDAP

URL: `ldap.htwg-konstanz.de`

BaseDN: dc=fh-konstanz,dc=de

Nutzer: ou=users,dc=fh-konstanz,dc=de

## Script notes

Run the script ldap.sh to configure the system for LDAP. If asked always choose "no". 

**We can automate that by editing the files /etc/nsswitch.conf, /etc/ldap.conf, /etc/pam.d/common-session**

ldap.conf can be customized to map the login attribute (default: uid) and groups from ldap. Overriding of values (home dir etc.) via nss_override_attribute_value.

We may need to override uidNumber, gidNumber and homeDirectory.

## Testing

Use Apache Directory Studio to browser any directory.

## References

Useful is https://help.ubuntu.com/community/LDAPClientAuthentication .
