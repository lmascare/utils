# [Percona](https://www.percona.com/doc/percona-distribution-mysql/8.0/index.html)

### [MySQL Database Installation](https://www.percona.com/doc/percona-server/8.0/installation/apt_repo.html)

#### Ubuntu Installation
```text
apt-get install gnupg2
wget https://repo.percona.com/apt/percona-release_latest.$(lsb_release -sc)_all.deb
dpkg -i percona-release_latest.$(lsb_release -sc)_all.deb
apt-get update
percona-release setup ps80
apt-get install percona-server-server

***
 * Percona Server is distributed with several useful UDF (User Defined Function) from Percona Toolkit.
 * Run the following commands to create these functions:

        mysql -e "CREATE FUNCTION fnv1a_64 RETURNS INTEGER SONAME 'libfnv1a_udf.so'"
        mysql -e "CREATE FUNCTION fnv_64 RETURNS INTEGER SONAME 'libfnv_udf.so'"
        mysql -e "CREATE FUNCTION murmur_hash RETURNS INTEGER SONAME 'libmurmur_udf.so'"

 * See http://www.percona.com/doc/percona-server/8.0/management/udf_percona_toolkit.html for more details

```

#### Centos Installation
```text
yum install https://repo.percona.com/yum/percona-release-latest.noarch.rpm
percona-release setup ps80
yum install percona-server-server

# Note after installation, the temp password for root is in /var/log/mysqld.log
alter user 'root'@'localhost' identified by 'PASSWORD';
```

### [MySQL XTRADB Cluster](https://www.percona.com/doc/percona-xtradb-cluster/8.0/index.html)

#### [Configuring Percona Repositories](https://www.percona.com/doc/percona-repo-config/percona-release.html#percona-release-usage)

#### [Ubuntu Installation](https://www.percona.com/doc/percona-xtradb-cluster/8.0/install/apt.html#apt)
```text
wget https://repo.percona.com/apt/percona-release_latest.generic_all.deb
dpkg -i percona-release_latest.generic_all.deb
apt-get install percona-xtradb-cluster

https://www.percona.com/doc/percona-xtradb-cluster/8.0/configure.html#configure

```

#### [CentOS Installation](https://www.percona.com/doc/percona-xtradb-cluster/8.0/install/yum.html#yum)
```text
# Update /etc/selinux/config. Set
SELINUX=permissive
sudo yum install percona-xtradb-cluster
```

#### Configuring Percona Cluster
##### Configuration
 Node | Hostname | IP Address   
--- | --- |  ---
Node 1 | ozone  | 172.31.251.70
Node 2 | neon   | 172.31.251.71 
Node 3 | helium | 172.31.251.72

```text
# Stop mysql service on all nodes

systemctl stop mysqld

# Ubuntu
cd /etc/mysql/mysql.conf.d/
cp -p mysqld.cnf mysqld.cnf.ori


# Centos
cd /etc
cp -p my.cnf my.cnf.ori

# Common for all OS
# Update following directives

wsrep_cluster_address=gcomm://172.31.251.70,172.31.251.71,172.31.251.72
wsrep_provider=/usr/lib/galera4/libgalera_smm.so
wsrep_node_address=172.31.251.70 # IP address as applicable
wsrep_cluster_name=pxc-cluster 
wsrep_node_name=ozone # neon or helium as applicable
pxc_strict_mode=ENFORCING
default_storage_engine=InnoDB
innodb_autoinc_lock_mode=2

#ToDo
 - Encrypt replication traffic

```
##### [Bootstrap the first node](https://www.percona.com/doc/percona-xtradb-cluster/8.0/bootstrap.html#bootstrap)
```text
On the first node, set
wsrep_cluster_address=gcomm://

systemctl start mysql@bootstrap.service

# At the MySQL client prompt
show status like 'wsrep%';

# look for 
wsrep_cluster_size = 1
wsrep_local_state_comment = synced

# Start the 2nd and 3rd Node as follows
systemctl start mysql

```


##### [Encrypting Replication traffic](https://www.percona.com/doc/percona-xtradb-cluster/8.0/security/encrypt-traffic.html#encrypt-replication-traffic)
 - See Generating Keys and Certificates Manually






















