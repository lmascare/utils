REM Create a tablespace RCAT.
REM Create the RMAN user

create user rman identified by rman
temporary tablespace temp
default tablespace rcat quota unlimited on rcat;

grant recovery_catalog_owner to rman;

rman catalog rman/rman
create catalog;

$ > export ORACLE_SID=prueba
$ > rman target / rcvcat rman/rman@rcat
RMAN> register database;

