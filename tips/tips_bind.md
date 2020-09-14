# Installing and Configuring BIND

```apple js
# Ensure NIC has a static IP - duh-uh

# Install bind, bind utils
yum install bind bind-utils

# Configure into a chrooted environment

```

#### Configuring Geo-IP
 * ToDo

#### Tips
* Download latest stable version from ftp://ftp.isc.org/isc/bind9/
* [Documentation](https://bind9.readthedocs.io/en/latest/introduction.html)
 - [Best Practices](https://kb.isc.org/docs/bind-best-practices-recursive)
 - [Sample Configs](https://gitlab.isc.org/isc-projects/bind9/commit/4a827494618e776a78b413d863bc23badd14ea42)

##### Compile for CentOS

* sudo yum install libuv-devel
* sudo yum install libcap-devel
* sudo yum install lmdb-devel
* sudo yum install json-c-devel
* ./configure \
   --prefix=/usr/local/bind-9.11.22 \
   --with-json-c \
   --with-lmdb
* make install

##### Compile for Ubuntu
###### Compiled 9.11.22 due to [DOS issue](https://kb.isc.org/docs/operational-notification-an-error-in-handling-tcp-client-quota-limits-can-exhaust-tcp-connections-in-bind-9160)
* apt install libuv-dev -y
* apt install libuv1-dev -y
* apt install libcap-dev -y
* apt install liblmdb-dev -y
* apt install libjson-c-dev -y
* sudo apt install -y libtool
* sudo apt install -y libtool-bin
* apt install libssl-dev

* ./configure \
   --prefix=/usr/local/bind-9.17.4 \
   --with-json-c \
   --with-lmdb

* make
* make install
* cd /usr/local/bin
* ln -s /usr/local/bind-9.17.4/bin/named-checkconf .
* ln -s /usr/local/bind-9.17.4/bin/named-checkzone .
* ln -s /usr/local/bind-9.17.4/sbin/named .
* ln -s /usr/local/bind-9.17.4/sbin/rndc .
* ln -s /usr/local/bind-9.17.4/sbin/rndc-confgen .

#### Configuring BIND

##### Reloading DNS Configuration
/usr/local/bin/rndc -c /home/chroot/domain/etc/rndc.conf reload

##### Create chrooted env
```commandline
# CentOS
mkdir /home/chroot/domain
cd /home/chroot

# Ubuntu
mkdir /u/chroot/domain
cd /u/chroot

# Ensure the named user account and group exists

# Ubuntu
groupadd -g 53 named
useradd -c 'Bind Server' -d /u/chroot/domain -g 53 -u 53 -s /bin/false named

chown named:named domain
chmod 750 domain
mkdir dev ; cd dev
mknod null c 1 3
mknod random c 1 8
mknod urandom c 1 9
mknod zero c 1 5
ln -s /dev/log log
cd ..
mkdir -p var/run var/named etc
chown -R named:named var etc
chgrp -R 770 var etc

cd etc
ln -s /etc/localtime localtime
```

#### Create skeleton etc/named.conf & etc/rndc.conf.
```
/usr/local/bin/rndc-confgen

# etc/named.conf
key "rndc-key" {
      algorithm hmac-sha256;
      secret "Af14YoMaTp4vm3PeVIZimEuPNUz3llWHvfsoc5pciw4=";
};
# 
controls {
      inet 127.0.0.1 port 953
              allow { 127.0.0.1; } keys { "rndc-key"; };
};

# etc/rndc.conf

key "rndc-key" {
        algorithm hmac-sha256;
        secret "Af14YoMaTp4vm3PeVIZimEuPNUz3llWHvfsoc5pciw4=";
};

options {
        default-key "rndc-key";
        default-server 127.0.0.1;
        default-port 953;
};
```

#### Admin setup
```
chmod 600 named.conf rndc.conf
chown named:named named.conf rndc.conf

# Verify named.conf
/usr/local/bin/named-checkconf -t /home/chroot/domain /etc/named.conf

# Add ZONES

# Setup root.hints file
See --> https://tldp.org/HOWTO/DNS-HOWTO-8.html#maint

cd /home/chroot/domain/etc
dig @e.root-servers.net . ns > root.hints

# CentOS
# Allow the firewall to pass the query through (CentOS)
firewall-cmd --zone=public --add-port=53/tcp --permanent
firewall-cmd --reload

Lookup GitHub utils:misc/dns for zonefiles, named.conf, rndc.conf service
```
 
