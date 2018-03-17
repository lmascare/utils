#!/bin/sh
ORACLE_SID=esrv ; ORAENV_ASK=NO
export ORACLE_SID ORAENV_ASK

. oraenv
svrmgrl << EOF
spool /u2/admins/oracle/admin/esrv/create/crdb3.log
connect internal
@$ORACLE_HOME/rdbms/admin/catproc.sql
@$ORACLE_HOME/rdbms/admin/caths.sql
@$ORACLE_HOME/rdbms/admin/otrcsvr.sql
connect system/manager
@$ORACLE_HOME/sqlplus/admin/pupbld.sql

disconnect
spool off
exit


EOF
