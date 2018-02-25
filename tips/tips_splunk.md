# Splunk

#### Download Splunk Enterprise

#### Centos
**Installation**  
```apple js
# Create the splunk User and Group
groupadd -g 8080 splunk
useradd -c 'Splunk User' -d /home/splunk -g splunk -m -k /etc/skel -s /bin/bash -u 8080 splunk

# Password is E****s

# Install (it installs in /opt/splunk)
rpm -i splunk-7.0.0-c8a78efdd40f-linux-2.6-x86_64.rpm

# Ubuntu

apt-get install ./splunk-7.0.0.0.deb
sudo dpkg -i ./splunk-7.0.0.0.deb
```
**Configuration**  
```apple js

# As user splunk
cd /opt/splunk/bin
./splunk start --accept-license

# Port Selected : 6000 on Centos. Does not work.

# To start at boot
splunk enable boot-start -user splunk

firewall-cmd --zone=public --add-port=6000/tcp --permanent
```
* It detects first run and creates certs in  
    _/opt/splunk/etc/auth_
* Web Interface at  
    * http://lmascare-centos.kellynoah.com:6000
    * http://lithium.kellynoah.com:8000
    * login: admin password: E****s 

**Splunk Forwarder**
```angularjs
# Download from Splunk Website

# Ubuntu
sudo dpkg -i ./splunkforwarder-7.0.2-03bbabbd5c0f-linux-2.6-amd64.deb

# Centos
sudo rpm -i splunkforwarder-7.0.2-03bbabbd5c0f-linux-2.6-x86_64.rpm

# Configuration
# Management port is 8089
# Ubuntu & Centos are same.
# Run as root so it can collect data from all sources
cd /opt/splunkforwarder/bin/
./splunk start

# Accept the license
# It runs its checks and starts splunkforwarder

# Enable boot start
./splunk enable boot-start

# Splunk controls
./splunk start
./splunk retart
./splunk stop

# Configure the Receiver first to receive data from the splunkforwarder.
# On the Enterprise system
./splunk enable listen 9997 -auth admin:E****s

# Configure the Universal Forwarder to send data to the Enterprise Server
# By default, the installation sets admin/changeme as credentials.
./splunk edit user admin -password E****s

# To add a forward server
./splunk add forward-server lithium.kellynoah.com:9997

# To list the forward server
./splunk list forward-server

# To remove a forward server
./splunk remove forward-server lithium.kellynoah.com

# Configure as a deployment client. This enables it to be configured form
# a central place
./splunk set deploy-poll lithium.kellynoah.com:9997

# To add / remove monitoring a resource
./splunk add monitor -source /var/log/messages
./splunk remove monitor /var/log/messages
```
