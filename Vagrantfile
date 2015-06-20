# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

    config.vm.box = "ubuntu/trusty64"

    # Create a private network, which allows host-only access to the machine
    # using a specific IP.
    # config.vm.network "private_network", ip: "192.168.33.10"

    # Create a public network, which generally matched to bridged network.
    # Bridged networks make the machine appear as another physical device on
    # your network.
    # config.vm.network "public_network"

    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "4096"]
    end

    $script = <<-SHELL
        sudo apt-get update
        sudo apt-get install -y git
        git clone https://github.com/sikessle/htwg-lab-cloud.git 
        cd htwd-lab-cloud
        ./deploy.sh
    SHELL

    config.vm.provision "file", inline: $script, privileged: false

end
