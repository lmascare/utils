#!/bin/sh
ORACLE_SID=prueba ; ORAENV_ASK=NO
export ORACLE_SID ORAENV_ASK

. oraenv
$ORACLE_HOME/bin/svrmgrl << EOF
connect internal/oracle
alter user system default tablespace SYSTEM;
alter user system temporary tablespace TEMP;

EOF
