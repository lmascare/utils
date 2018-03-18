# PostgresSQL Installation and Configuration

```apple js
# Create the Postgres user & group
groupadd -g 8889 postgres
useradd -c 'Postgres SQL' -d /home/postgres -g 8889 -m -r -s /bin/bash -u 8889 postgres




# Install the software using the Configuration items in the table below
# The initdb is run duing installation to create the DB
```
[Documentation](https://www.postgresql.org/docs/current/static/index.html)
 
 * Verify the [Shared Memory](https://www.postgresql.org/docs/current/static/kernel-resources.html) parameters
 * Determine if memory overcommit is an issue (sysctl -w vm.overcommit_memory=2)
 * [Parameter Settings](https://www.postgresql.org/docs/current/static/runtime-config.html) 
 

DB Item | Configuration
--- | ---
Installation Dir | /u/PostgreSQL/10
Installation | Server, pgAdmin, Stack Builder, CLI tools
SuperUser | E****s
Port | 5432
Locale | C

#### Command line utilities

Command | Options | Notes
--- |--- | ---
pg_ctl | | Initialize start / stop / Control a PostGres server 
psql | -d \<dbname> -h \<host> -p \<port> -U \<dbuser> | Connect to a DB and perform DML

#### psql command options

Option | Results
--- | ---
\l | lis the Databases
\d *. | Lists all the Instance Tables
ENV Variables | PGDATABASE, PGHOST, PGPORT, PGUSER, PGPASSWORD
~/.pgpass | hostname:port:database:username:password Perms 0600
pg_hba.conf | eg line "host    all             all             0.0.0.0/0              md5"
