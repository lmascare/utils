#!/bin/sh
ORACLE_SID=rcat ; ORAENV_ASK=NO
export ORACLE_SID ORAENV_ASK

. oraenv
$ORACLE_HOME/bin/sqlplus << EOF
system/manager
@$ORACLE_HOME/sqlplus/admin/help/helpbld.sql helpus.sql
EOF
