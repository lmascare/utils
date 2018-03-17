# MySQL Tips

## MariaDB installation
 * cd /etc/yum.repos.d
 * vi mariadb.repo   
[mariadb]  
name = Mariadb  
baseurl = http://yum.mariadb.org/10.1/centos7-amd64  
gpgkey = https://yum.mariadb.org/RPM-GPG-KEY-MariaDB  
gpgcheck=1

### Install and start the services
 * yum install MariaDB-server MariaDB-client -y  
 * systemctl start mariadb 
 * systemctl enable mariadb  
 * systemctl status mariadb  

### Secure the installation
 * mysql_secure_installation
 * Determine defaults  
    * mysqld --print-defaults
 * Root login to setup users and databases
    * mysql -u root -p mysql
 
## Connection
 * mysql -h <host> -u <user> -p -D <dbname> - P <port(4303)>
 * /etc/my.cnf or /etc/mysql/my.cnf or $HOME/.my.cnf
 
## DDL

### Centos 7 has replaced MySQL with MariaDB
 * As root   
    * shutdown the mariadb server  
        systemctl stop mariadb

    * Initialize the system dictionary
        mysql_install_db --user=mysql
 
    * To recover the root password
        * start the server in safe mode
            * mysqld_safe --skip-grant-tables
            * mysql -u root mysql
            * update user set password=PASSWORD("<password>") where user='root';
            * flush privileges;
            * stop the mysqld_safe process
        * systemctl start mariadb
        * /usr/bin/mysql_secure_installation
        * mysql -u root -p mysql (enter root password)
        * create user lifecycle identified by '<password>';
    
    * Directories are in /var/lib/mysql*. Move them aside to and reinstall mysql.

 * show tables;
 * describe <tablename>;
 * select user from mysql.user;
 * Wildcard is %.

 * create user 'lifecycle'@'localhost' identifed by 'PASSWORD';
 * grant all privileges on lifecycle.* to 'lifecycle'@'localhost' \
   identified by 'PASSWORD';
 * grant all privileges on lifecycle.* to 'lifecycle'@'%' \
   identified by 'PASSWORD';
 * create database lifecycle default character set UTF8;

 * use lifecycle;
 * CREATE TABLE hostinfo (
      hostname    varchar(128) not null,
      hostgroup   varchar(128) not null
   );

   *Note group is a reserved word*

 * to load the data into the table and ignore the header

   load data local infile '/tmp/host.csv' into table hostinfo
    fields terminated by ',' ignore 1 lines;

    *Note local and full path are extremely important*

## mysql_config_editor
 * Not available on Mariadb. Use it to encrypt passwords

## .my.conf entries to support multiple DBs
 * The client section is common to all DBs
 [client]
 port=3306
 prompt='(\d)'
 * For specific MySQL DB entries
 
 **[mysqldb1]**  
  user=(user1)  
  password=(password)  
  database=(db1)  
  host=(host1)
 
 **[mysqldb2]**  
 user=(user2)  
 password=(password2)  
 database=(db2)  
 host=(host1)  
 
 * To connect to db1  
    _mysql --defaults-group-suffix=db1_

## DML
 * select count(*) from tablename;

## Backup and Recovery
 * By default the MySQL datafiles are in /var/lib/mysql  
 * Use the 'mysqldump' utility to do the backups  
   **D=`date +'%m%%d%Y_%H%M%S** # Sets D=ddmmyyyy_hrminsec
   **mysqldump --databases -u lifecyle -p lifecycle > mysql_backup_${D}.sql** # This will dump the entire DB.
   
 * This generates the SQL file for recovery using the 'mysql' client  
   **mysql < mysql_bacup_20170709_190432.sql**
   
## Load data from a CSV file into MySQL
* load historical data into a MySQL table  
* Ensure you convert STR to DATE  
* The 'ignore 1 lines' ensures that the header line is skipped  

load data local infile '/home/lmascare/misc/mysql/goog.csv'  
into table goog  
fields terminated by ',' ignore 1 lines  
(@date, open, high, low, close, volume)  
set date = str_to_date(@date,'%d-%b-%y');  
