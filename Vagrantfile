# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.hostname = $environ

    config.vm.provider :virtualbox do |v|
        v.name = $environ
    end

    config.vm.provision :shell, inline: $shell
    config.vm.network :forwarded_port, guest: 4444, host: 4444
end

$environ = "mangulo-env"
$shell = <<-CONTENTS
sudo -s
export DEBIAN_FRONTEND=noninteractive

# Update apt
apt-get update
apt-get -y upgrade

# Install Python packages
apt-get -y install python3-pip
apt-get -y install libffi-dev
apt-get -y install libpq-dev
pip3 install -r /vagrant/requirements.txt

# Install Heroku Toolbelt
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
CONTENTS
