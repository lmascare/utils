# Ubuntu Tips

#### Create Volumes
* lvdisplay    - Display properties of a volume group with volumes
* pvs --all    - Dispays all physical volumes and associated volume groups
* lvmdiskscan  - Scans all devices visible to LVM

**Create a Volume Group, Logical Volume and Filesystem**  
```
vgcreate vg_u /dev/sdb1
lvcreate --name lv_u --size 68G vg_u
mkfs -t ext4 /dev/vg_u/lv_u
```

**Install Oracle Virtualbox**  
```
apt-get install virtualbox
apt-get install vagrant
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
```


