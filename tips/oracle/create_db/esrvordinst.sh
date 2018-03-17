#!/bin/sh
ORACLE_SID=esrv
export ORACLE_SID

/u4/oracle/product/8.1.7/bin/svrmgrl << EOF
spool /u2/oracle/admin/esrv/create/ordinst.log;
connect internal/oracle
@/u4/oracle/product/8.1.7/ord/admin/ordinst.sql
spool off
exit;

EOF
