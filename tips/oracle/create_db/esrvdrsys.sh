#!/bin/sh
ORACLE_SID=esrv
export ORACLE_SID

/u4/oracle/product/8.1.7/bin/svrmgrl << EOF
spool /u2/oracle/admin/esrv/create/ctxtbls.log;
connect internal/oracle
CREATE TABLESPACE DRSYS DATAFILE '/u4/oracle/data/esrv/drsys01.dbf' SIZE 400M REUSE
 AUTOEXTEND ON NEXT 640K
MINIMUM EXTENT 64K
DEFAULT STORAGE ( INITIAL 64K NEXT 64K MINEXTENTS 1 MAXEXTENTS  UNLIMITED  PCTINCREASE 50);
spool off
exit;

EOF
