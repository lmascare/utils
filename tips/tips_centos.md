# Networking
#
# /etc/sysconfig/network  - Contains hostname and enable networking
# NETWORKING=yes
# HOSTNAME=
# FORWARD_IPV4=false
# NTPSERVERARGS=iburst
#
# /etc/sysconfig/network-scripts/ifcfg-eth0 has
# DEVICE=eth
# IPADDR=
# NETMASK=
# BROADCAST=
# GATEWAY=
# DNS1=
# DNS2=
# DOMAIN=
# ONBOOT=yes
# BOOTPROTO=static
#
# /etc/hosts will get the IP from there. Also look at /etc/host.conf
#
# /etc/resolv.conf for DNS
# 
# /etc/ntp.conf
#
# Check the status of all the services
# chkconfig --list
#
# start the sshd server
# /etc/ssh contains the config files
# service sshd status   -- Lists the status of the sshd server
# service sshd stop     -- stops the sshd server
# service sshd start    -- starts the sshd server


# Update the /etc/sysconfig/iptables with an entry for port 22
# iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT

# LVM
# lvdisplay -- Display properties of volume groups with volumes
# pvs --all 	Displays all physical volumes
# lvmdiskscan  Scan for all devices visible to LVM2
#
# Create a physical volume on c0d1 (full disk)
# pvcreate /dev/cciss/c0d1

# Create a volume group vg_u
# vgcreate vg_u /dev/cciss/c0d1

# Create the logical volume on volume group vg_u
# lvcreate --name lv_u --size 33.91G vg_u

# Now create the fs
# mkfs -t ext4 /dev/vg_u/lv_u

# /etc/fstab entry 
# /dev/mapper/vg_u-lv_u   /u                      ext4    defaults        0     2
#                                                                         ^     ^
#                                                         mnt_opts        dump  fsck_pass (root fs=1, others=2)

# Remove a Logical Volume
# Provide the full path to the logical volume via the volume group
# lvremove vg_u/lv_u	

# Remove the volume group (if all logical volumes have been removed from the vg)
# vgremove vg_u

# Now remove the physical volume
# pvremove /dev/cciss/c0d1



# SWAP
# you must first create the swapfile on the disk or file using mkswap
# mkswap /dev/vg_c0d1/lv_swap
#
# /etc/fstab entry
# /dev/mapper/vg_c0d1-lv_swap 	swap                    swap    defaults        0 0

# Add swap from all entries in /etc/fstab
# swapon -a

# List swap configuaration
# swapon -s
#
# For file based swap
# fallocate --length 8GiB /swapfile1
# dd if=/dev/zero of=/swapfile1 bs=1MiB count=8192
#
# Add entry to /etc/fstab
# /swapfile1 swap swap defaults 0 0
#
# Activate it
# swapon -a
#
# Reference https://www.centos.org/docs/5/html/5.2/Deployment_Guide/s2-swap-creating-file.html
#

# YUM
# 
# Ensure the rpm to create the repo exists
# rpm -q -a |egrep createrepo
# Else
# yum install createrepo

# Init the repo
# createrepo /u/repository/fedora-14 (after creating the directories)
#

# USERADD
useradd -c 'Larry Mascarenhas' -d /home/lmascare -g 100 -m -k /etc/skel \
-s /bin/bash -u 1001 lmascare
passwd lmascare # Set the new password

# To see which pkg provides a file
yum whatprovides */mkpasswd

# Ensure rc.d scripts work as expected. Use the Wiki for reference
# https://wiki.debian.org/LSBInitScripts
update-rc.d app start 99 2 3 . stop 99 0 1 6 .
