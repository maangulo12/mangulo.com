# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
    config.vm.box = "ubuntu/trusty64"

    config.vm.provider :virtualbox do |v|
        v.name = "flask-skeleton-vm"
    end

    config.vm.provision :shell, path: "vagrant/update.sh"
    config.vm.provision :shell, path: "vagrant/python.sh"

    config.vm.network :forwarded_port, guest: 5555, host: 5555
end
