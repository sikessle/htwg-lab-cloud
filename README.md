![HTWG Lab Cloud](resources/logo.png?raw=true)

OpenStack based cloud platform for the HTWG Laboraties.

# Branching/Issues/Folders

- Put devstack related files to "devstack" and virtual machine instance related files to "instance"
- Branch per feature
- Merge if feature works flawless to master
- GitHub Issues to manage Features, Bugs, etc.

# Project Goals

see Issues->Milestones

# DevStack

To bring the networking up and running after switching between different networks (HTWG, home, etc.) run the following in the ubuntu host: `sudo ifdown eth0 && sudo ifup eth0` 
