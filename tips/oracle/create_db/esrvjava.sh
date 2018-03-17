#!/bin/sh
ORACLE_SID=esrv
export ORACLE_SID

/u4/oracle/product/8.1.7/bin/svrmgrl << EOF
spool /u2/oracle/admin/esrv/create/jvminst.log;
connect internal/oracle
@/u4/oracle/product/8.1.7/javavm/install/initjvm.sql;
spool off
spool /u2/oracle/admin/esrv/create/initxml.log;
@/u4/oracle/product/8.1.7/oracore/admin/initxml.sql
spool off
spool /u2/oracle/admin/esrv/create/catxsu.log;
@/u4/oracle/product/8.1.7/rdbms/admin/catxsu.sql
spool off
spool /u2/oracle/admin/esrv/create/init_jis.log;
@/u4/oracle/product/8.1.7/javavm/install/init_jis.sql
spool off
spool /u2/oracle/admin/esrv/create/jisja.log;
@/u4/oracle/product/8.1.7/javavm/install/jisja.sql
spool off
spool /u2/oracle/admin/esrv/create/jisaephc.log;
@/u4/oracle/product/8.1.7/javavm/install/jisaephc.sql
spool off
spool /u2/oracle/admin/esrv/create/initplgs.log;
@/u4/oracle/product/8.1.7/rdbms/admin/initplgs.sql
spool off
spool /u2/oracle/admin/esrv/create/initjsp.log;
@/u4/oracle/product/8.1.7/jsp/install/initjsp.sql
spool off
spool /u2/oracle/admin/esrv/create/jspja.log;
@/u4/oracle/product/8.1.7/jsp/install/jspja.sql
spool off
spool /u2/oracle/admin/esrv/create/initplsj.log;
@/u4/oracle/product/8.1.7/rdbms/admin/initplsj.sql
spool off
spool /u2/oracle/admin/esrv/create/initjms.log;
@/u4/oracle/product/8.1.7/rdbms/admin/initjms.sql
spool off
spool /u2/oracle/admin/esrv/create/initrepapi.log;
@/u4/oracle/product/8.1.7/rdbms/admin/initrepapi.sql
spool off
spool /u2/oracle/admin/esrv/create/initsoxx.log;
@/u4/oracle/product/8.1.7/rdbms/admin/initsoxx.sql
spool off
exit;

EOF
