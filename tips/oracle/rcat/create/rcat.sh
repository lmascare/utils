#!/bin/sh
ORACLE_SID=rcat ; ORAENV_ASK=NO
export ORACLE_SID ORAENV_ASK

. oraenv
svrmgrl << EOF
spool crdb1.log
connect internal
startup nomount pfile = "/bb/oracle/admin/rcat/pfile/initrcat.ora"
CREATE DATABASE "rcat"
   maxdatafiles 254
   maxinstances 8
   maxlogfiles 32
   maxlogmembers 4
   character set UTF8
   national character set UTF8
DATAFILE '/oradata/data/rcat/system01.dbf' SIZE 100M AUTOEXTEND ON
logfile '/oradata/data/rcat/redo01.log' SIZE 10M, 
        '/oradata/data/rcat/redo02.log' SIZE 10M, 
        '/oradata/data/rcat/redo03.log' SIZE 10M,
        '/oradata/data/rcat/redo04.log' SIZE 10M;
disconnect
spool off
exit


EOF
