## Vagrant Tips  


**Install Oracle Virtualbox**  
```
# Ubuntu
apt-get install virtualbox
apt-get install vagrant

# Centos/7
cd /etc/yum.repos.d
wget http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo
yum install -y VirtualBox-5.1
yum -y install https://releases.hashicorp.com/vagrant/2.0.1/vagrant_2.0.1_x86_64.rpm

# To open the GUI
sudo /usr/bin/virtualbox

# To see the Global Status. Note the id
sudo vagrant global-status

# SSH onto the box
vagrant ssh <id>

# To determine port configured for vagrant
vagrant ssh-config

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
vagrant box add ubuntu/bionic64 --provider=virtualbox  

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

# Virtualboxes created with vagrant
# Vagrantfile in git misc 

# As user 'lmascare

# To bring up Ubuntu ozone & neon
cd /u/vbox/ozone
vagrant up

cd /u/vbox/neon
vagrant up
```

```text
Vagrantfile

# Set hostname
config.vm.hostname = "ozone"
config.vm.define "ozone"

config.vm.box = "ubuntu/bionic64"

# Using public_network allows putty connection to port 22
config.vm.network "public_network", ip: "172.31.251.70", bridge: "enp3s0f0"

config.vm.provider "virtualbox" do |vb|

# Customize the amount of memory & cpu on the VM:
 vb.memory = "4096"
 vb.cpus = "2"
end

```