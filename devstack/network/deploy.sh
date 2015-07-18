#!/bin/bash

# Deploys feature

# Enable internet in instances. 
# SNAT: sending outgoing traffic over eth0 just before it is sended.
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
