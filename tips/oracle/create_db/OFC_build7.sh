:
# 
# $Header: OFC_build7.sh,v 1.4 93/06/04 11:51:30 gmehra: Stab $ 
# 
#  Copyright (c) 1991 by Oracle Corporation 
#    NAME
#      OFC_build7.sh - <one-line expansion of the name>
#    DESCRIPTION
#      <short description of component this file declares/defines>
#    RETURNS
# 
#    NOTES
#      <other useful comments, qualifications, etc.>
#    MODIFIED   (MM/DD/YY)
#     gmehra     06/04/93 -  rename the tablespaces 
#     gmehra     02/18/93 -  change initial dbf file names 
#     gmehra     02/08/93 -  minextents for rollbacks must be at least 2 
#     gmehra     01/26/93 -  Creation 

# Assume that ORACLE_HOME and ORACLE_SID are correct

# The following parameters are the default chosen sizes for the rest of 
# the installation utility.   Please feel free to comment out the old
# values and insert your new choices.  [Later on we can prompt for values
# and keep these as the defaults.]   
#
#   This build assumes 30M free above and beyond that of the SYSTEM tablespace.
#

TINYEXTENT=4K
SMALLEXTENT=10K
NORMALEXTENT=50K
BIGEXTENT=100K
LARGEEXTENT=250K

MAIN_FILE=/u5/oracle/data/esrv/ofcmain01.dbf
MAIN_SIZE=1000M
MAIN_INIT=$SMALLEXTENT
MAIN_NEXT=$NORMALEXTENT

MESG_FILE=/u5/oracle/data/esrv/ofcmesg01.dbf
MESG_SIZE=3000M
MESG_INIT=$BIGEXTENT
MESG_NEXT=$LARGEEXTENT

INDB_FILE=/u5/oracle/data/esrv/ofcindb01.dbf
INDB_SIZE=1000M
INDB_INIT=$BIGEXTENT
INDB_NEXT=$LARGEEXTENT

INDS_FILE=/u5/oracle/data/esrv/ofcinds01.dbf
INDS_SIZE=1000M
INDS_INIT=$SMALLEXTENT
INDS_NEXT=$NORMALEXTENT

LOGFILE=/u2/admins/oracle/admin/esrv/create/Install.log

svrmgrl << END_sqldba >> $LOGFILE
connect internal
set echo on
spool ofc_build

create tablespace OFC_MAIN datafile '$MAIN_FILE' size $MAIN_SIZE
 default storage (initial $MAIN_INIT next $MAIN_NEXT minextents 1 
 maxextents 99 pctincrease 0) online;

create tablespace OFC_MESG datafile '$MESG_FILE' size $MESG_SIZE
 default storage (initial $MESG_INIT next $MESG_NEXT minextents 1 
 maxextents 99 pctincrease 0) online;
 ALTER DATABASE DATAFILE '$MESG_FILE' AUTOEXTEND ON NEXT 500M;

create tablespace OFC_INDB datafile '$INDB_FILE' size $INDB_SIZE
 default storage (initial $INDB_INIT next $INDB_NEXT minextents 1  
 maxextents 99 pctincrease 0) online;

create tablespace OFC_INDS datafile '$INDS_FILE' size $INDS_SIZE
 default storage (initial $INDS_INIT next $INDS_NEXT minextents 1 
 maxextents 99 pctincrease 0) online;

spool off
END_sqldba
