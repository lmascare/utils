# SFTP Configuration. 

### [SFTP Configuration](https://www.howtoforge.com/tutorial/how-to-setup-an-sftp-server-on-centos/)

* Create the chroot directory for all SFTP
```text
mkdir /u/sftp
chmod root:root/sftp
chown 701 /sftpusers
```

* Create a group
```
groupadd -g 2222 sftpusers
```

* Users should be created with nologin shell
```text
useradd -g sftpusers -d /upload -s /sbin/nologin testftpuser
mkdir -p /u/sftp/testftpuser/upload
chown root:sftpusers /u/sftp/testftpuser
chown testftpuser:sftpusers /u/sftp/testftpuser/upload
```

### sshd_config modification to support sftp
```text
# At the END of the file
Match Group sftpusers
ChrootDirectory /u/sftp/%u
ForceCommand internal-sftp
```

### Restart the FTP service
```text
sudo systemctl restart sshd
```

### Test connectivity
```text
sftp testftpuser@localhost
testftpuser@localhost's password:
Connected to localhost.
sftp> pwd
Remote working directory: /upload
sftp>
```