# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

    config.vm.box = "ubuntu/trusty64"

    config.vm.hostname = "htwglabcloud"

    config.vm.network :private_network, ip: "172.16.100.10"

    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "4096"]
        vb.name = "htwg-lab-cloud"
    end

    $script = <<-SHELL
        cd ~
        sudo apt-get update
        sudo apt-get install -y git
        git clone https://github.com/sikessle/htwg-lab-cloud.git 
        cd htwd-lab-cloud
        ./deploy.sh
    SHELL

    config.vm.provision "shell", inline: $script, privileged: false

end
