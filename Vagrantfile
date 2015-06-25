# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
    env_name = "mangulo-env"

    config.vm.hostname = env_name

    config.vm.box = "ubuntu/trusty64"

    config.vm.provider :virtualbox do |v|
        v.name = env_name
    end

    config.vm.provision :shell, path: "vagrant/update.sh"
    config.vm.provision :shell, path: "vagrant/python.sh"
    config.vm.provision :shell, path: "vagrant/heroku.sh"

    config.vm.network :forwarded_port, guest: 4444, host: 4444
end
