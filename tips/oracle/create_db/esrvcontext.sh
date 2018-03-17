#!/bin/sh
ORACLE_SID=esrv
export ORACLE_SID


cd /u4/oracle/product/8.1.7/ctx/admin

/u4/oracle/product/8.1.7/bin/sqlplus << EOF
internal
spool /u2/oracle/admin/esrv/create/spoolctx.log;
@/u4/oracle/product/8.1.7/ctx/admin/dr0csys ctxsys DRSYS DRSYS
connect ctxsys/ctxsys
@/u4/oracle/product/8.1.7/ctx/admin/dr0inst /u4/oracle/product/8.1.7/ctx/lib/libctxx8.so
@/u4/oracle/product/8.1.7/ctx/admin/defaults/drdefus.sql
spool off
exit

EOF
