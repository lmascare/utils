# Build a new Linux / Unix System

 - Load the OS
 - Patch to the latest version
 - Use static IP address
 - Setup DNS Client
```text
UBUNTU 18.04
/etc/network/interfaces.d

```
 - Setup FQDN
 - Update /etc/skel/.bashrc
```text
alias h=history
alias e=exit
alias c=clear
alias vi=vim
alias p="ps -eaf | egrep $1"

set -o vi
set -o ignoreeof

PATH=/opt/bb/bin:${PATH}
EDITOR=/usr/bin/vi
PAGER=/usr/bin/less

export EDITOR PAGER PATH
```
 - Add .vimrc to /etc/skel
 - Update ~root/.bashrc with same customizations.
 - Create FS
   - /u
   - /db/mysql
   - /db/postgres

 - Create directory structures
```text
/u (contains admin as toplevel directory)
  admin      751   root:oper
  admin/bin  751   oper:oper
  admin/cfg  751   oper:oper
  admin/etc  751   oper:oper
  admin/keys 770   oper:oper
  admin/logs 771   oper:oper
  admin/tmp  771   oper:oper

  # Location of MySQL installation
  mysql/<version>
  
  # Location of Postgres installation
  postgresql/<version>

  # Toplevel directory for users
  users      755   root:root
```

 - Create groups
 ```text
groupadd -g 4000 oper
groupadd -g 4001 mysql
groupadd -g 4002 postgres
```

 - Create user accounts
 ```text
useradd -c 'Operations Automation' -d /u/users/oper -g 4000 -m -k /etc/skel \
-s /bin/bash -u 4000 oper

useradd -c 'Larry Mascarenhas' -d /u/users/lmascare -g 4000 -m -k /etc/skel \
-s /bin/bash -u 6001 lmascare

useradd -c 'MySQL Database' -d /u/users/mysql -g 4001 -m -k /etc/skel \
-s /bin/bash -u 4001 mysql

useradd -c 'Postgres Database' -d /u/users/postgres -g 4002 -m -k /etc/skel \
-s /bin/bash -u 4002 postgres
```

 - Set passwords and expiration policy
```text
 - set passwords for oper, mysql, postgres, lmascare
 - /etc/login.defs for expiration
 - Enable logging of SU, FAILLOG_ENAB, LOG_UNKFAIL_ENAB, SULOG_FILE
 - Update PATH to include /opt/bb/bin
 - Set UMASK to 022
 
passwd mysql
passwd postgres
```

 - CRON allowed
```text
cat /etc/cron.allow
oper

```

 - Install Python3 and its modules
```text
See compile_and_install_python.md
```

 - Install MySQL
```
sudo apt-get update
sudo apt-get install cmake
sudo apt-get install build-essential
sudo apt-get install libssl-dev
sudo apt-get install libncurses5-dev
sudo apt-get install  pkg-config

Download & Install MySQL community edition source code
sudo dpkg --instdir=/u/mysql/5.7.28 -i mysql-community-source_5.7.28-1ubuntu18.04_amd64.deb

cd ~/misc
tar xfz /u/mysql/5.7.28/usr/share/src/mysql-community_5.7.28.orig.tar.gz

cd mysql-5.7.28
mkdir build
cd build
# LM Method
cmake .. -DDOWNLOAD_BOOST=1 -DWITH_BOOST=/opt/bb/local \
 -DCMAKE_INSTALL_PREFIX=/u/mysql/5.7.28 \
 -DMYSQL_DATADIR=/db/mysql/data \
 -DMYSQL_UNIX_ADDR=/u/mysql/5.7.28/run/mysqld.lock
cd ..
make

# Initial test cmake .. -DDOWNLOAD_BOOST=1 -DWITH_BOOST=/opt/bb/local
# cmake with all options
cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql \
  -DMYSQL_DATADIR=/usr/local/mysql/data \ 
  -DSYSCONFDIR=/etc \ 
  -DWITH_MYISAM_STORAGE_ENGINE=1 \
  -DWITH_INNOBASE_STORAGE_ENGINE=1 \
  -DWITH_MEMORY_STORAGE_ENGINE=1 \
  -DMYSQL_UNIX_ADDR=/tmp/mysqld.sock \
  -DMYSQL_TCP_PORT=3306 \
  -DENABLED_LOCAL_INFILE=1 \
  -DWITH_READLINE=1 \
  -DWITH_PARTITION_STORAGE_ENGINE=1 \
  -DEXTRA_CHARSETS=all \
  -DDEFAULT_CHARSET=utf8 \
  -DDEFAULT_COLLATION=utf8_general_ci \
  -DWITH_SSL=/usr/local/openssl

make install
```

 - Setup ENV for MySQL
    - create /usr/local/bin/mysqlenv
```
MYSQL_HOME=/u/mysql/5.7.28
MANPATH=${MYSQL_HOME}/man

PATH=${MYSQL_HOME}/bin:${PATH}

export PATH MANPATH
```
    - create /etc/profile.d/mysql.sh
```
# Set environment for MySQL
if [[ -f /usr/local/bin/mysqlenv ]]
then
    source /usr/local/bin/mysqlenv
fi
```
 - Create DATA directory for MySQL
    - mkdir /db/mysql/data
    - chown mysql:mysql /db/mysql/data
    - chmod 700 /db/mysql/data
 
 - Define a location for MySQL Socket
    - mkdir /u/mysql/5.7.28/run
    - chown mysql:mysql /u/mysql/5.7.28/run
    - chmod 700 /u/mysql/5.7.28/run
  
 - Review tips_mysql.md for Ubuntu initial setup
    

 - Install Postgres
   * See tips_postgres.md
 ```
 
 ```

    - Start / Stop scripts for Postgres

 - Install PERL
```
Download and install from ActiveState - as applicable
```
