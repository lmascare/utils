# PostgreSQL Installation and Configuration

```apple js
# Create the Postgres user & group
groupadd -g 8889 postgres
useradd -c 'Postgres SQL' -d /home/postgres -g 8889 -m -r -s /bin/bash -u 8889 postgres

# Install the software using the Configuration items in the table below
# The initdb is run duing installation to create the DB (postgres)
```


[Documentation](https://www.postgresql.org/docs/current/static/index.html)
 * Using the [Postgres APT Repository](https://wiki.postgresql.org/wiki/Apt) 
 * Move the [INSTALLATION and DATADIR](https://www.digitalocean.com/community/tutorials/how-to-move-a-postgresql-data-directory-to-a-new-location-on-ubuntu-16-04) to the desired location
   * Edit /etc/postgresql/12/main/postgresql.conf
       - Change data_directory to /db/postgresql/12/main
   * Move /var/lib/postgresql to /db
        ```text
        cd /var/lib
        tar cf - postgresql | (cd /db ; tar xf -)
        mv postgresql postgresql.ori
        ```
   * Move installation to /u 
      #####Important to note /usr/lib is hardcoded in /usr/share/perl5/PgCommon.pm
        ```text
        cd /usr/lib
        tar cf - postgresql | (cd /u ; tar xf -)
        mv postgresql postgresql.ori
        ln -s /u/postgresql /usr/lib/postgresql
    
    * The startup script for postgres is linked to the SysV startup
        ```
        systemctl enable postgresql
        Synchronizing state of postgresql.service with SysV service script with /lib/systemd/systemd-sysv-install.
        Executing: /lib/systemd/systemd-sysv-install enable postgresql
        ```text
    * Start / stop PostgreSQL
        ```text
        systemctl start postgresql
        systemctl stop postgresql
        ```
    * Create ENV scripts (/usr/local/bin/pgenv)
    ```text
        #
        # Settings for PostgreSQL
        #
        PGSQL_HOME=/u/postgresql/12/
        MANPATH=${MANPATH}:/usr/share/postgresql/12
        #
        PATH=${PGSQL_HOME}/bin:${PATH}
        export PATH MANPATH
    ```
    * Create global profile script (/etc/profile.d/pgenv)
    ```
        # Set environment for PostgreSQL
        if [[ -f /usr/local/bin/pgenv ]]
        then
            source /usr/local/bin/pgenv
        fi
    ```
```
 * Verify the [Shared Memory](https://www.postgresql.org/docs/current/static/kernel-resources.html) parameters
 * Determine if memory overcommit is an issue (sysctl -w vm.overcommit_memory=2)
 * [Parameter Settings](https://www.postgresql.org/docs/current/static/runtime-config.html) 
 * psql [PROMPT](https://www.postgresql.org/docs/8.4/static/app-psql.html#APP-PSQL-PROMPTING)
wh

DB Item | Configuration
--- | ---
Installation Dir | /u/PostgreSQL/10
Installation | Server, pgAdmin, Stack Builder, CLI tools
SuperUser | E****s
Port | 5432
Locale | C

#### Command line utilities
```
#### Create a DB. All commands from SHELL (bash) prompt as user 'postgres'
createdb django
createuser -S -D -R -P -e <user>
psql -d django # This logs as superuser into DB 'django'
create schema django authorization django;
alter role django set search_path = "django";

#### To login w/o password. Set the .pgpass file. Then login 
psql -h localhost -d django -U django
```
Command | Options | Notes
--- |--- | ---
initdb | -D /var/lib/postgresql/10/main --auth-local peer --auth-host md5 | Create a new PG cluster
pg_ctl | -D /var/lib/postgresql/10/main -l logfile start | Initialize start / stop / Control a PostGres server
psql | -d \<dbname> -h \<host> -p \<port> -U \<dbuser> | Connect to a DB and perform DML

#### psql command options

Option | Results | 
--- | ---
\l | lis the Databases
\d *. | Lists all the Instance Tables
select * from pg_database; | Display list of DBs
psql -h <hostname> -l | List the DBs (using ~/.pgpass)
ENV Variables | PGDATABASE, PGHOST, PGPORT, PGUSER, PGPASSWORD
~/.pgpass | hostname:port:database:username:password Perms 0600
pg_hba.conf | eg line "host    all             all             0.0.0.0/0              md5"
Create a Data Tablespace | create tablespace lc_data location '/u/postgres/lc/data';
Create an Index Tablespace | create tablespace lc_index location '/u/postgres/lc/index';
Create a TEMP Tablespace | create tablespace lc_temp location '/u/postgres/lc/temp';
Create a DB | create database lcdb tablespace lc_data;
Set Prompt in ~/.psqlrc | \set PROMPT1 '%[%033[1;33;40m%]%n@%/%R%[%033[0m%]%# '
Create user | createuser -S -D -R -P -e lcuser (No superuser/create db/create role/sets password)
Create a schema for the user | create schema mymdb authorization mymdb; (as superuser in mymdb)
Set search path to role | alter role mymdb set search_path = "mymdb"; (as superuser)
Revoke schema creation from public |  revoke create on schema public from public; (as superuser)

