#!/usr/bin/env bash

# Python 3.4.0
# Installing Project Dependencies

apt-get -y install python3-pip

pip3 install -r /vagrant/requirements.txt

echo "Successfully installed Python packages."