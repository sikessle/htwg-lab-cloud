# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

    config.vm.box = "ubuntu/trusty64"
    config.vm.hostname = "htwglabcloud"
    config.vm.synced_folder ".", "/vagrant", disabled: true

    # VM will have 
    #
    # eth0: nat                 host access to internet (default from vagrant)
    # eth1: host-only           internal management network (good: has no dhcp)
    # eth2: bridged DHCP        access from outside the VM and floating IPs -> internet
    #
    # eth0 provides a DHCP, we MUST NOT configure this in DevStack, otherwise
    # our instances get an IP from this DHCP instead of from nova-network
    config.vm.network :private_network, ip: "192.168.35.10"
    config.vm.network :public_network

    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "4096"]
        vb.name = "htwg-lab-cloud"
        # openstack guests to talk to each other
        vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
        vb.customize ["modifyvm", :id, "--nicpromisc3", "allow-all"]
        #vb.gui = true
    end

    $script = <<-SHELL
        cd ~
        pwd
        sudo apt-get install -y git
        git clone https://github.com/sikessle/htwg-lab-cloud.git 
        cd htwg-lab-cloud
        ./deploy.sh
        echo "****************************************************************"
        ip=$(ifconfig | grep eth2 -A 1 | grep "inet addr:[0-9|\.]*" -o | grep "[0-9|\.]*" -o)
        echo "HTWG Lab Cloud Dashboard running at: http://$ip"
        echo "****************************************************************"
    SHELL

    config.vm.provision "shell", inline: $script, privileged: false

end
