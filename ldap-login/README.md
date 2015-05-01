# LDAP Login in Instances

A user must be able to log into the instance (ubuntu) with his LDAP credentials.
The required configuration for Ubuntu can be found in this directory.

- The client (Ubuntu instance) always contacts the LDAP server to authenticate the user.
- The client is not allowed to change the password for the user in the LDAP server.
- The client restricts the users who are allowed to login via LDAP to a single user. This must be injected via the cloud-init user-data field. This ensures that 1 instance maps to exactly 1 user.
