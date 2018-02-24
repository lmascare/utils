# Splunk

#### Download Splunk Enterprise

#### Centos
**Installation**  
```apple js
#### Create the splunk User and Group
groupadd -g 8080 splunk
useradd -c 'Splunk User' -d /home/splunk -g splunk -m -k /etc/skel -s /bin/bash -u 8080 splunk

#### Password is E****s

#### Install (it installs in /opt/splunk)
rpm -i splunk-7.0.0-c8a78efdd40f-linux-2.6-x86_64.rpm

#### Ubuntu

apt-get install ./splunk-7.0.0.0.deb
sudo dpkg -i ./splunk-7.0.0.0.deb
```
**Configuration**  
```apple js

#### As user splunk
cd /opt/splunk/bin
./splunk start --accept-license

#### Port Selected : 6000 on Centos. Does not work.

#### To start at boot
splunk enable boot-start -user splunk

firewall-cmd --zone=public --add-port=6000/tcp --permanent
```
* It detects first run and creates certs in  
    __/opt/splunk/etc/auth__
* Web Interface at  
    * http://lmascare-centos.kellynoah.com:6000
    * http://lithium.kellynoah.com:8000
    * login: admin password: E****s 
