# PostgreSQL Installation and Configuration

```apple js
# Create the Postgres user & group
groupadd -g 8889 postgres
useradd -c 'Postgres SQL' -d /home/postgres -g 8889 -m -r -s /bin/bash -u 8889 postgres




# Install the software using the Configuration items in the table below
# The initdb is run duing installation to create the DB (postgres)
```
[Documentation](https://www.postgresql.org/docs/current/static/index.html)
 
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
# Create a DB. All commands from SHELL (bash) prompt
createdb django
createuser django

# To login w/o password. Set the .pgpass file. Then login 
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
Create a schema for the user | create schema mymdb authorization mymdb; (In the owner's DB)
Set search path to role | alter role mymdb set search_path = "mymdb"; (as superuser)
Revoke schema creation from public |  revoke create on schema public from public; (as superuser)

