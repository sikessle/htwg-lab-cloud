# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

    config.vm.box = "ubuntu/trusty64"
    config.vm.hostname = "htwglabcloud"
    config.vm.synced_folder ".", "/vagrant", disabled: true

    # VM will have eth0: NAT, eth1: host-only
    config.vm.network :private_network, ip: "172.16.100.10"

    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "4096"]
        vb.name = "htwg-lab-cloud"
        # openstack guests to talk to each other
        vb.customize ["modifyvm", :id, "--nicpromisc1", "allow-all"]
        vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
        #vb.gui = true
    end

    $script = <<-SHELL
        cd ~
        pwd
        sudo apt-get install -y git
        git clone https://github.com/sikessle/htwg-lab-cloud.git 
        cd htwg-lab-cloud
        ./deploy.sh
        echo "***************************"
        ip=$(ifconfig | grep eth1 -A 1 | grep "inet addr:[0-9|\.]*" -o | grep "[0-9|\.]*" -o)
        echo "HTWG Lab Cloud Dashboard running at: http://$ip"
        echo "***************************"
    SHELL

    config.vm.provision "shell", inline: $script, privileged: false

end
