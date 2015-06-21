# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

    config.vm.box = "ubuntu/trusty64"
    config.vm.hostname = "htwglabcloud"
    # Disable default synced folder
    config.vm.synced_folder ".", "/vagrant", disabled: true

    # Networking
    #
    # eth0 provides a DHCP, we MUST NOT configure this in DevStack, otherwise
    # our instances get an IP from this DHCP instead from nova-network
    #
    # eth0: devstack (internet)
    # eth1: br100 -- vnet0,1,.. -- instances    FLAT_INTERFACE
    # eth2: floating IPs                        PUBLIC_INTERFACE 
    #

    # eth0: NAT         host access to internet (default from vagrant)
    # eth1: Host-Only   internal management network (good: has no dhcp from VM)
    config.vm.network :private_network, ip: "192.168.35.129"
    # eth2: Bridged     access from outside of VM and floating IPs -> internet
    config.vm.network :public_network

    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "4096"]
        vb.name = "htwg-lab-cloud"
        # Promiscous mode
        # allow openstack guests to talk to each other
        vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
        vb.customize ["modifyvm", :id, "--nicpromisc3", "allow-all"]
        #vb.gui = true
    end

    # Install HTWG Lab Cloud on first boot
    $script = <<-SHELL
        cd ~
        pwd
        sudo apt-get install -y git
        git clone https://github.com/sikessle/htwg-lab-cloud.git
        cd htwg-lab-cloud
        ./deploy.sh
    SHELL

    config.vm.provision "shell", inline: $script, privileged: false

end
