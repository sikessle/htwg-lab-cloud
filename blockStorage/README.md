# Block Storage
In this folder and sub-folders goes the block storage related files and information.
There are the required links to setup block storage and attach it to a running instance.

## Dashboard
Setup with the dashboard.
- Compute -> Instanzen -> Instanz starten
- Compute -> Datenträger -> Datenträger erstellen
- Erstellter Datenträger -> Anhänge verwalten -> An Instanz anhaengen

## HTTP
Setup with the HTTP API.
- [Launch Image](http://developer.openstack.org/api-ref-compute-v2.html)
    - Create server
- [Block Storage](http://developer.openstack.org/api-ref-blockstorage-v2.html)
    - Create volume
- [Attach Block Storage](http://developer.openstack.org/api-ref-compute-v2-ext.html#os-volume_attachments)
    - Attach volume