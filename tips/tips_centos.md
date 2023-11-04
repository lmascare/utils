## Administration

#### Start / stop services
* systemctl start <service>
* systemctl stop <service>

#### Enable / Disable services from starting during boot
* systemctl enable \<service\>
* systemctl disable \<service\>
* systemctl reenable \<service\>

#### Services disabled
* systemctl disable private_chef-runsvdir-start.service
* systemctl disable chef-client.service
* systemctl disable nexposeconsole.service
* systemctl disable splunk.service

### Issue with yum repository
```text
One of the configured repositories failed (Kubernetes),
 and yum doesn't have enough cached data to continue. At this point the only
 safe thing yum can do is fail. There are a few ways to work "fix" this:

     1. Contact the upstream for the repository and get them to fix the problem.

     2. Reconfigure the baseurl/etc. for the repository, to point to a working
        upstream. This is most often useful if you are using a newer
        distribution release than is supported by the repository (and the
        packages for the previous distribution release still work).

     3. Run the command with the repository temporarily disabled
            yum --disablerepo=kubernetes ...

     4. Disable the repository permanently, so yum won't use it by default. Yum
        will then just ignore the repository until you permanently enable it
        again or use --enablerepo for temporary usage:

            yum-config-manager --disable kubernetes
        or
            subscription-manager repos --disable=kubernetes

     5. Configure the failing repository to be skipped, if it is unavailable.
        Note that yum will try to contact the repo. when it runs most commands,
               so will have to try and fail each time (and thus. yum will be be much
        slower). If it is a very temporary problem though, this is often a nice
        compromise:

            yum-config-manager --save --setopt=kubernetes.skip_if_unavailable=true

```

#### Networking

* /etc/sysconfig/network  - Contains hostname and enable networking
* NETWORKING=yes
* HOSTNAME=
* FORWARD_IPV4=false
* NTPSERVERARGS=iburst

* /etc/sysconfig/network-scripts/ifcfg-eth0 has
* DEVICE=eth
* IPADDR=
* NETMASK=
* BROADCAST=
* GATEWAY=
* DNS1=
* DNS2=
* DOMAIN=
* ONBOOT=yes
* BOOTPROTO=static

* /etc/hosts will get the IP from there. Also look at /etc/host.conf

* /etc/resolv.conf for DNS
 
* /etc/ntp.conf

#### Check the status of all the services
* chconfig --list

#### Create a service (eg nexpose)
* systemctl enable nexposeconsole.service

#### start the sshd server
* /etc/ssh contains the config files
* service sshd status   -- Lists the status of the sshd server
* service sshd stop     -- stops the sshd server
* service sshd start    -- starts the sshd server

### Determine of SELinux is enforcing
* [Article](https://stackoverflow.com/questions/20688844/sshd-gives-error-could-not-open-authorized-keys-although-permissions-seem-corre)
* [Article on SeLinux ssh] (https://linux.die.net/man/8/ssh_selinux)
* getenforce will return enforcing

```
# Temporary change
chcon  -t ssh_home_t /u/users/lmascare/.ssh/authorized_keys
ls -ldZ /u/users/lmascare/.ssh/authorized_keys


```


#### Update the /etc/sysconfig/iptables with an entry for port 22
* iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT

#### LVM
* lvdisplay -- Display properties of volume groups with volumes
* pvs --all 	Displays all physical volumes
* lvmdiskscan  Scan for all devices visible to LVM2

#### Create a physical volume on c0d1 (full disk)
* pvcreate /dev/cciss/c0d1

#### Create a volume group vg_u
* vgcreate vg_u /dev/cciss/c0d1

#### Create the logical volume on volume group vg_u
* lvcreate --name lv_u --size 33.91G vg_u

#### Now create the fs
* mkfs -t ext4 /dev/vg_u/lv_u

#### /etc/fstab entry 
 /dev/mapper/vg_u-lv_u   /u                      ext4    defaults        0     2
                                                                         ^     ^
                                                         mnt_opts        dump  fsck_pass (root fs=1, others=2)

#### Remove a Logical Volume
##### Provide the full path to the logical volume via the volume group
# lvremove vg_u/lv_u	

#### Remove the volume group (if all logical volumes have been removed from the vg)
* vgremove vg_u

#### Now remove the physical volume
* pvremove /dev/cciss/c0d1



#### SWAP
##### you must first create the swapfile on the disk or file using mkswap
* mkswap /dev/vg_c0d1/lv_swap

#### /etc/fstab entry
 /dev/mapper/vg_c0d1-lv_swap 	swap                    swap    defaults        0 0

#### Add swap from all entries in /etc/fstab
* swapon -a

#### List swap configuaration
* swapon -s

#### For file based swap
* fallocate --length 8GiB /swapfile1
* dd if=/dev/zero of=/swapfile1 bs=1MiB count=8192

#### Add entry to /etc/fstab
 /swapfile1 swap swap defaults 0 0

#### Activate it
* swapon -a

#### Reference 
https://www.centos.org/docs/5/html/5.2/Deployment_Guide/s2-swap-creating-file.html

#### YUM
##### Ensure the rpm to create the repo exists
* yum install createrepo
* rpm -q -a |egrep createrepo

##### Init the repo
* createrepo /u/repository/fedora-14 (after creating the directories)

#### Yum cleanup
* yum-complete-transaction --cleanup-only
* yum history redo last

#### USERADD
useradd -c 'Larry Mascarenhas' -d /home/lmascare -g 100 -m -k /etc/skel \
-s /bin/bash -u 1001 lmascare
passwd lmascare # Set the new password

##### To see which pkg provides a file
yum whatprovides */mkpasswd

#### Ensure rc.d scripts work as expected. Use the Wiki for reference
* https://wiki.debian.org/LSBInitScripts  
* update-rc.d app start 99 2 3 . stop 99 0 1 6 .
