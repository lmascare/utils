# NMAP tips

### [Cheat Sheet](https://s3-us-west-2.amazonaws.com/stationx-public-download/nmap_cheet_sheet_0.6.pdf)

### NMAP
* Scan all 64k ports on a host with OS recognition
    * nmap -p 1-65535 -T4 -A -v 172.31.251.143 -Pn
* Scan port 3389 (RDP) across a subnet
    *  nmap 172.31.251.0/24 -p 3389

### ZENMAP
* run as root. MIT Magic Cookie needs to be added

### CLI 
```commandline
# as regular user
echo $DISPLAY
xauth list 

sudo su
xauth add lmascare-centos/unix:12  MIT-MAGIC-COOKIE-1  504d59ed15113e4a1f4722e1dee22b5d

# Test SMTP mail relay
nmap -sV --script smtp-open-relay -v <target>
```
