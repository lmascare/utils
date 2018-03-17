set echo on
spool ctrl
STARTUP NOMOUNT
CREATE CONTROLFILE REUSE DATABASE "ESRV" NORESETLOGS ARCHIVELOG
    MAXLOGFILES 32
    MAXLOGMEMBERS 4
    MAXDATAFILES 254
    MAXINSTANCES 8
    MAXLOGHISTORY 904
LOGFILE
  GROUP 1 '/u5/oracle/data/esrv/redo01.log'  SIZE 10M,
  GROUP 2 '/u5/oracle/data/esrv/redo02.log'  SIZE 10M,
  GROUP 3 '/u5/oracle/data/esrv/redo03.log'  SIZE 10M,
  GROUP 4 '/u5/oracle/data/esrv/redo04.log'  SIZE 10M
DATAFILE
  '/u5/oracle/data/esrv/system01.dbf',
  '/u5/oracle/data/esrv/tools01.dbf',
  '/u5/oracle/data/esrv/rbs01.dbf',
  '/u5/oracle/data/esrv/users01.dbf',
  '/u5/oracle/data/esrv/ofcmain01.dbf',
  '/u5/oracle/data/esrv/ofcmesg01.dbf',
  '/u5/oracle/data/esrv/ofcindb01.dbf',
  '/u5/oracle/data/esrv/ofcinds01.dbf'
CHARACTER SET UTF8
;
# Recovery is required if any of the datafiles are restored backups,
# or if the last shutdown was not normal or immediate.
RECOVER DATABASE
# All logs need archiving and a log switch is needed.
ALTER SYSTEM ARCHIVE LOG ALL;
# Database can now be opened normally.
ALTER DATABASE OPEN ;
# Commands to add tempfiles to temporary tablespaces.
# Online tempfiles have complete space information.
# Other tempfiles may require adjustment.
ALTER TABLESPACE TEMP ADD TEMPFILE '/u5/oracle/data/esrv/temp01.dbf' REUSE;
# End of tempfile additions.
#
spool off
