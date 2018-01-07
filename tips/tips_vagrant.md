## Vagrant Tips  


**Install Oracle Virtualbox**  
```
apt-get install virtualbox
apt-get install vagrant

# To open the GUI
sudo /usr/bin/virtualbox

# To see the Global Status. Note the id
sudo vagrant global-status

# SSH onto the box
vagrant ssh <id>

# To determine the configured ports
vagrant port <id>
```

**Create a location for the Virtualbox Images**  
```apple js

mkdir /u/vbox
cd /u/vbox

# mkdir for hosts
mkdir helium ozone cobalt

# Set the VAGRANT_HOME
VAGRANT_HOME=/u/vbox/.vagrant
export VAGRANT_HOME  

# Download machine images <location=/u/vbox/.vagrant>
vagrant box add bento/centos-7 --provider=virtualbox
vagrant box add bento/ubuntu-16.04 --provider=virtualbox
vagrant box add plaurin/solaris-11_3 --provider=virtualbox  

# CentOS
cd helium
vagrant init centos/7

# Ubuntu
cd ozone
vagrant init ubuntu/xenial64

# Solaris11
cd cobalt
vagrant init plaurin/solaris-11_3

# Location of box
https://vagrantcloud.com/plaurin/boxes/solaris-11_3/versions/1/providers/virtualbox.box
# Add the following line to Vagrant
config.ssh.password = "1vagrant"
