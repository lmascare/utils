# Ports configured

**Running on lmascare-centos**  

Port Number | Application  
---- | ---------  
80   | Chef Manager  
443  | SSL Chef Manager  
3780 | Nexpose Console
6000 | Splunk
8000 | Chef
8008 | Django Web Server
8065 | Splunk AppServer Port
8080 | Jenkins  
8081 | Artifactory  
8089 | Splunk Mgmt
8191 | Splunk kvstore Port
8888 | Home Web Server  
8443 | Home WS SSL Port  

**Running on Lithium**  

Port Number | Application
--- | ---
8000 | Splunk
8065 | Splunk AppServer Port
8089 | Splunk Mgmt
8191 | Splunk kvstore Port
8999 | Receiver Port


**Running on Silicon**

Port Number | Application
--- | ---
80 | Apache
5000 | Keystone Auth_URI
8774 | Nova
8778 | Placement API
9292 | Glance API
11211 | Memcached
35357 | Keystone Auth_URL


  
# Systems

Machine Type | OS Type | Hostname | Notes  
--- | ---  | --- | ---  
T5220 | Solaris11 | krypton |  
DL380 G7 | Ubuntu 16.04 | silicon |     
laptop G62 | Centos 7.2 | lmascare-centos  
laptop envy | Ubuntu 16.04 | lithium | Virtual Desktop  
vbox  | Centos | helium  
vbox  | Ubuntu 16.04  | ozone  
vbox  | Solaris 11.3  | cobalt  

   
   
  