# Ubuntu Administration Tips

* To su to root, login as regular user, then sudo su
* Install the following packages
    * ntp

#### Install the Array Configuration Utility (ACU)
* HP YUM repository
    * https://downloads.linux.hpe.com/
    * Download the add_repo.sh script from the 'Getting started link'

```apple js
# Management component pack for Proliant
./add_repo.sh mcp

# Enroll keys
curl http://downloads.linux.hpe.com/SDR/hpPublicKey1024.pub | apt-key add -
curl http://downloads.linux.hpe.com/SDR/hpPublicKey2048.pub | apt-key add -
curl http://downloads.linux.hpe.com/SDR/hpPublicKey2048_key1.pub | apt-key add -
curl http://downloads.linux.hpe.com/SDR/hpePublicKey2048_key1.pub | apt-key add -

# Update the indexes
apt-get update

# Install the HP Prolian iLO online configuration utility
apt-get install hponcfg
apt-get install ssacli
apt-get install ssa
```
#### hponcfg utility
```apple js
# Retrieve the current configuration and write it to a file
hponcfg -a -w silicon.xml

# Update the XML file appropriately. Then apply the changes
hponcfg -v -i silicon.xml
```
* iLO user admin / E****s  
* iLO used DSS. Therefore add to .ssh/config

* Setting up a new user in iLO
```apple js
<!-- HPONCFG VERSION = "4.4.0" -->
<!-- Device: iLO3  Firmware Version : 1.88 -->
<RIBCL VERSION="2.0">
<LOGIN USER_LOGIN="admin" PASSWORD="password">
<USER_INFO mode="write">
<ADD_USER USER_NAME="Larry Mascarenhas" USER_LOGIN="lmascare" PASSWORD="%user_password%">
        <ADMIN_PRIV value="Y"/>
        <REMOTE_CONS_PRIV value="Y"/>
        <RESET_SERVER_PRIV value="Y"/>
        <VIRTUAL_MEDIA_PRIV value="Y"/>
        <CONFIG_ILO_PRIV value="Y"/>
</ADD_USER>
</USER_INFO>
</LOGIN>
</RIBCL>

# As root
hponcfg -f set_ilo_user.xml -s user_password=F******!
```

```apple js
Host silicon-mgmt
  HostName 
  HostKeyAlgorithms=+ssh-dss
```
* Looking at the Array Controller
```apple js
ssa -start
ssacli
 > ctlr all show config
 > ctlr all show status
``` 

```apple js

   Internal Drive Cage at Port 2I, Box 1, OK


   Array A (SAS, Unused Space: 0  MB)

      logicaldrive 1 (68.3 GB, RAID 1, OK)

      physicaldrive 1I:1:6 (port 1I:box 1:bay 6, SAS HDD, 72 GB, OK)
      physicaldrive 2I:1:3 (port 2I:box 1:bay 3, SAS HDD, 72 GB, OK)


   Array B (SAS, Unused Space: 0  MB)

      logicaldrive 2 (68.3 GB, RAID 1, OK)

      physicaldrive 1I:1:7 (port 1I:box 1:bay 7, SAS HDD, 72 GB, OK)
      physicaldrive 1I:1:8 (port 1I:box 1:bay 8, SAS HDD, 72 GB, OK)

   Unassigned

      physicaldrive 1I:1:5 (port 1I:box 1:bay 5, SAS HDD, 72 GB, OK)
      physicaldrive 2I:1:1 (port 2I:box 1:bay 1, SAS HDD, 72 GB, OK)
      physicaldrive 2I:1:2 (port 2I:box 1:bay 2, SAS HDD, 72 GB, OK)
      physicaldrive 2I:1:4 (port 2I:box 1:bay 4, SAS HDD, 72 GB, OK)

   SEP (Vendor ID PMCSIERA, Model  SRC 8x6G) 250  (WWID: 50014380146AD98F)


Smart Array P410i in Slot 0 (Embedded)    (sn: 500143801361F210)


   Port Name: 1I

   Port Name: 2I


   Internal Drive Cage at Port 1I, Box 1, OK



   Internal Drive Cage at Port 2I, Box 1, OK



   Unassigned

      physicaldrive 1I:1:1 (port 1I:box 1:bay 1, SAS HDD, 72 GB, OK)
      physicaldrive 1I:1:2 (port 1I:box 1:bay 2, SAS HDD, 72 GB, OK)
      physicaldrive 1I:1:3 (port 1I:box 1:bay 3, SAS HDD, 72 GB, OK)
      physicaldrive 1I:1:4 (port 1I:box 1:bay 4, SAS HDD, 72 GB, OK)
      physicaldrive 2I:1:5 (port 2I:box 1:bay 5, SAS HDD, 72 GB, OK)
      physicaldrive 2I:1:6 (port 2I:box 1:bay 6, SAS HDD, 72 GB, OK)
      physicaldrive 2I:1:7 (port 2I:box 1:bay 7, SAS HDD, 72 GB, OK)
      physicaldrive 2I:1:8 (port 2I:box 1:bay 8, SAS HDD, 72 GB, OK)

   SEP (Vendor ID PMCSIERA, Model  SRC 8x6G) 250  (WWID: 500143801361F21F)

```