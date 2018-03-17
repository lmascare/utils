#!/bin/sh
ORACLE_SID=esrv ; ORAENV_ASK=NO
export ORACLE_SID ORAENV_ASK

. oraenv
svrmgrl << EOF
spool /u2/admins/oracle/admin/esrv/create/crdb1.log
connect internal
startup nomount pfile = "/u2/admins/oracle/admin/esrv/pfile/initesrv.ora"
CREATE DATABASE "esrv"
   maxdatafiles 254
   maxinstances 8
   maxlogfiles 32
   maxlogmembers 4
   character set UTF8
   national character set UTF8
DATAFILE '/u5/oracle/data/esrv/system01.dbf' SIZE 300M AUTOEXTEND ON
logfile '/u5/oracle/data/esrv/redo01.log' SIZE 10M, 
        '/u5/oracle/data/esrv/redo02.log' SIZE 10M, 
        '/u5/oracle/data/esrv/redo03.log' SIZE 10M,
        '/u5/oracle/data/esrv/redo04.log' SIZE 10M;
disconnect
spool off
exit


EOF
