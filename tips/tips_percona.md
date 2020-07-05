# [Percona](https://www.percona.com/doc/percona-distribution-mysql/8.0/index.html)

### [Installation](https://www.percona.com/doc/percona-server/8.0/installation/apt_repo.html)

#### Ubuntu Installation
```text
apt-get install gnupg2
wget https://repo.percona.com/apt/percona-release_latest.$(lsb_release -sc)_all.deb
dpkg -i percona-release_latest.$(lsb_release -sc)_all.deb
apt-get update
percona-release setup ps80

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

```

