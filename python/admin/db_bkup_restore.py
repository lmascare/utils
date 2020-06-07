#!/usr/local/bin/python3.7
r"""Backup and Restore MySQL Database.

This script will perform Backup and Restore of a MySQL Database

Backup Strategy
 - Full Backup of all databases
 - Full Backup of a single database
 - Incremental Backup of all databases
 - Incremental Backup of a single database

Restore Strategy
 - Full Restore of all databases
 - Full Restore of a single database
 - Incremental Restore of all databases
 - Incremental Restore of a single database

ToDO
 - Update brman table when
    - Backup Starts, Ends, Backup Type (Full / Incr), Status
 - In the log index file, upload every entry into the database.

Completed
 - Run as mysql user only
 - Check mysqldump and mysqlbinlog executable exists
 - Check if DB requested are configured in dbcreds
 - Full backup
 - INCR backups.
"""
from lank import obj_utils
from lank.lank_cfg import host, scriptname, maintainers
from lank.db_bkup_restore_cfg import dbs, brman_db, mysql_db, dir_perms, \
    connect_sql, verify_sql, check_files, full_bkup_cmd, incr_bkup_cmd, \
    defaults_file, secure_sql, logbin_index_sql, preferred_user
from datetime import datetime
from shutil import copyfile

import argparse
import os


def do_backup(dbname, bkup_type, timestamp, timestamp2):
    r"""Perform Database backup.

    Database backup is performed based on the type of request. Invokes
    mysqldump with appropriate options to perform the backup.

    Ref:
    https://dev.mysql.com/doc/refman/5.7/en/backup-policy.html
    https://dev.mysql.com/doc/refman/5.7/en/recovery-from-backups.html
    https://dev.mysql.com/doc/refman/5.7/en/mysqladmin.html
    mysqldump options --> https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html

    # Permission denied when SELECT INTO OUTFILE
    https://stackoverflow.com/questions/2783313/
    how-can-i-get-around-mysql-errcode-13-with-select-into-outfile

    InnoDB tables are used so mysqldump options for full backups are
    --defaults-file          File created in backup_dir/.my.cnf to protect
                             username and password
    --single-transaction     Uses are consistent read and guarantees that data
                             seen my mysqldump does not change
    --flush-logs             Enables point-in-time restore
    --master-data=2          Causes mysqldump to write binary log info to output
                             which assists in point-in-time recovery.
    --databases              Database to be backed up
    --tab                    Location of backup /u/admin/bkup/<dbname>/<YYYY-MM-DD>/
    --fields-terminated-by   Use ',' to separate fields
    --fields-enclosed-by='"' Use '"' to encapsulate fields that have ','.
    --lines-terminated-by    Handle lines terminated by \r\n

    Incremental backups
    mysqladmin --defaults-file flush-logs
    Then read the mysql-bin.index file and copy all the log files specified.
    select @@log_bin_index;

    :param      dbname:     Database to be backed up
    :param      bkup_type:  Backup type 'full | incr'

    :returns    bkup_msgs:  Messages received from components
                bkup_rc:    Error count encountered from components
    """
    bkup_msgs = []
    bkup_rc = 0
    mylog.info("Performing backup of {}".format(dbname.upper()), 0)
    try:
        # backups are done as the root user
        mysql_dbid = dbs[mysql_db]["dbid"]
        mysql_dbtype = dbs[mysql_db]["dbtype"]
        dbid = dbs[dbname]["dbid"]

        db_backup_dir = dbs[dbname]["backup_dir"] + "/" + timestamp

        db_defaults_file = db_backup_dir + "/" + defaults_file

        db_backup_file = db_backup_dir + "/" + dbname + "_" + timestamp2 + ".binlog"

        if not os.path.isdir(db_backup_dir):
            mylog.info("Creating directory --> {}".format(db_backup_dir), 0)
            os.mkdir(db_backup_dir)
            os.chmod(db_backup_dir, 0o777)
        # The mysqldump uses credentials to perform the backup. This is
        # received via the restapi database type variable dbtype. It is used
        # create the .my.cnf file for mysqldump and mysqladmin entries
        dbtype = "restapi"
        mylog.info("Retrieving credentials for dbname --> {} dbtype --> {}".
                   format(dbid, dbtype), 0)
        db_creds = obj_utils.DBConnect(mysql_dbid, dbtype)
        with open(db_defaults_file, "w") as f:
            f.write("[mysqldump]\n")
            f.write("user={}\n".format(db_creds.dbuser))
            f.write("password={}\n".format(db_creds.dbpass))
            f.write("host={}\n".format(db_creds.dbhost))
            f.write("port={}\n\n".format(db_creds.dbport))

            f.write("[mysqladmin]\n")
            f.write("user={}\n".format(db_creds.dbuser))
            f.write("password={}\n".format(db_creds.dbpass))
            f.write("host={}\n".format(db_creds.dbhost))
            f.write("port={}\n".format(db_creds.dbport))

            f.close()
            os.chmod(db_defaults_file, 0o0600)
        mylog.info("Received credentials for --> {}. Performing backup".
                   format(db_creds.dbuser), 0)
        if (bkup_type == "full"):
            bkup_cmd = full_bkup_cmd.format(
                db_defaults_file,
                db_backup_dir,
                dbname,
                db_backup_file
            )
            mylog.info("Backup Command --> {}".format(bkup_cmd), 0)
            os.system(bkup_cmd)
        elif (bkup_type == "incr"):
            # For Incremental backups, run
            #   - mysqladmin flush-logs
            #   - Read the index file for all the logs to be copied
            #   - Copy them over to the backup_dir
            #   - Update the DB with the stat of each file.
            bkup_cmd = incr_bkup_cmd.format(
                db_defaults_file
            )
            mylog.info("Backup Command --> {}".format(bkup_cmd), 0)
            os.system(bkup_cmd)
            mydb_creds = obj_utils.DBConnect(mysql_dbid, mysql_dbtype)
            (mydb_cursor, mydb_connection) = mydb_creds.connect()
            mydb_cursor.execute(logbin_index_sql)
            log_index_file = mydb_cursor.fetchone()[0]
            mylog.info("Log Index File --> {}".format(log_index_file), 0)
            mydb_connection.close()

            # Now copy the files specified in the log_index_file
            with open(log_index_file, "r") as f:
                logfiles = f.readlines()
                logfiles = [x.strip() for x in logfiles]
                mylog.info("List of logfiles --> {}".format(logfiles), 0)
                for logfile in logfiles:
                    base_filename = os.path.basename(logfile)
                    copyfile(logfile, db_backup_dir + "/" + base_filename)
    except Exception as e:
        err = "FAILED: Errors during backup. Error --> {}".format(e)
        bkup_msgs.append(err)
        bkup_rc += 1
        mylog.warning(err, 0)

    return (bkup_msgs, bkup_rc)


def pre_req_checks(brman_db, dbname, mysqldb, today):
    r"""Pre-requisite checks to ensure DB backup / restore will succceed.

    Following checks are implemented
     - Establish connectivity to the BRMAN database and Target DB
     - Ensure DB properties are correctly set
        - Binary Logs are enabled
        - secure-file-priv
     - Ensure destination directories are present with valid permissions

    :param      dbname:         Database to be backed up
    :returns    precheck_msgs   Messages from the checks
                precheck_rc      Count of Errors
    """
    precheck_msgs = []
    precheck_rc = 0
    mylog.info("Pre-requisites check for {}".format(dbname), 0)
    # Ensure it runs only as preferred_user
    current_user = os.environ['LOGNAME']
    if [current_user != preferred_user]:
        err = "FAILED: Incorrect user --> {}. Preferred --> {}".\
            format(current_user, preferred_user)
        precheck_msgs.append(err)
        precheck_rc += 1
        mylog.warning(err, 0)
    else:
        mylog.info("SUCCESS: Preferred user logged in", 0)
    # Extract properties of the DB
    brman_dbid = dbs[brman_db]["dbid"]
    brman_dbtype = dbs[brman_db]["dbtype"]

    mysql_dbid = dbs[mysqldb]["dbid"]
    mysql_dbtype = dbs[mysqldb]["dbtype"]

    dbid = dbs[dbname]["dbid"]
    dbtype = dbs[dbname]["dbtype"]
    db_backup_dir = dbs[dbname]["backup_dir"]
    db_restore_dir = dbs[dbname]["restore_dir"]

    mylog.info("Backup Directory  --> {}".format(db_backup_dir), 0)
    mylog.info("Restore Directory --> {}".format(db_restore_dir), 0)

    # Verify appropriate directories are created
    def check_dirs(chk_dir):
        r"""Check Directory Existence & Permissions."""
        dir_msg = []
        dir_rc = 0
        mylog.info("Checking Directory Existence and Permissions --> {}".
                   format(chk_dir), 0)
        if not os.path.exists(chk_dir):
            mylog.info("Directory does not exist. Creating.", 0)
            try:
                os.makedirs(chk_dir, exist_ok=True)
                mylog.info("Directory '{}' created successfully".
                           format(chk_dir), 0)
            except Exception as e:
                err = "Unable to create directory '{}'. Error --> {}".\
                    format(chk_dir, e)
                dir_msg.append(err)
                dir_rc += 1
                mylog.warning(err, 0)
        else:
            mylog.info("Directory '{}' exists".format(chk_dir), 0)

        # Check Permissions
        if (dir_rc == 0):
            mylog.info("Checking Permissions for {}".format(chk_dir), 0)
            st = os.stat(chk_dir)
            dir_mode = oct(st.st_mode)
            mylog.info("Permissions --> {}".
                       format(dir_mode), 0)
            if (dir_mode != dir_perms):
                mylog.warning("Permission '{}' does not match '{}'. Setting".
                              format(dir_mode, dir_perms), 0)
                try:
                    mylog.info("Setting permissions", 0)
                    os.chmod(chk_dir, int(dir_perms, 8))
                    mylog.info("Successful", 0)
                except Exception as e:
                    err = "Unable to set permissions for {}. Error --> {}".\
                        format(chk_dir, e)
                    mylog.warning(err, 0)
                    dir_msg.append(err)
                    dir_rc += 1
        else:
            err = "Unable to check / set directory permissions"
            dir_msg.append(err)
            dir_rc += 1
            mylog.warning(err, 0)

        return (dir_msg, dir_rc)

    for check_dir in [db_backup_dir, db_restore_dir]:
        (msg, rc) = check_dirs(check_dir)
        if (rc > 0):
            precheck_msgs.append(msg)
            precheck_rc += rc

    # Verify DB connectivity
    def db_checks(dbid, dbtype):
        r"""Database connectivity and settings checks."""
        dbcheck_msgs = []
        dbcheck_rc = 0
        mylog.info("Testing DB connectivity --> {}".format(dbid), 0)
        try:
            mydb_creds = obj_utils.DBConnect(dbid, dbtype)
            (mydb_cursor, my_connection) = mydb_creds.connect()

            mydb_cursor.execute(connect_sql)
            row_data = (mydb_cursor.fetchone()[0]).strftime("%Y-%m-%d")

            if (row_data == today):
                mylog.info("Established DB connectivity", 0)
            else:
                err = "Failed DB connectivity check"
                dbcheck_msgs.append(err)
                mylog.warning(err, 0)
                dbcheck_rc += 1
                my_connection.close()
        except Exception as e:
            err = "FAILED. DB Connectivity & Settings checks . Error --> {}".\
                format(e)
            dbcheck_msgs.append(err)
            dbcheck_rc += 1

        return (dbcheck_msgs, dbcheck_rc)

    for db_check in [(brman_dbid, brman_dbtype), (dbid, dbtype)]:
        (db_msg, db_rc) = db_checks(db_check[0], db_check[1])
        if (rc > 0):
            precheck_msgs.append(db_msg)
            precheck_rc += db_rc

    # Verify DB settings
    mylog.info("Verifying DB settings for backup and restore", 0)
    try:
        mysql_creds = obj_utils.DBConnect(mysql_dbid, mysql_dbtype)
        (mysql_cursor, mysql_connection) = mysql_creds.connect()

        # Binary logs settings
        mylog.info("Checking Binary Logs settings", 0)
        mysql_cursor.execute(verify_sql)
        row_data = mysql_cursor.fetchall()
        if (len(row_data) > 0):
            mylog.info("DB correctly set for backup and restore", 0)

        # secure-file-priv settings
        mylog.info("Checking secure-file-priv settings", 0)
        mysql_cursor.execute(secure_sql)
        row_data = mysql_cursor.fetchone()[0]
        if (row_data == ""):
            mylog.info("DB correctly set for secure-file-priv", 0)
    except Exception as e:
        err = "Failed verifying DB settings for backup and restore. " \
              "Error --> {}".format(e)
        precheck_msgs.append(err)
        precheck_rc += 1
        mylog.warning(err, 0)

    # Check existence of required binaries
    mylog.info("Checking existence of required files", 0)
    for req_file in check_files:
        if not os.path.exists(req_file):
            err = "FAILED: File does not exist --> {}".format(req_file)
            precheck_msgs.append(err)
            precheck_rc += 1
            mylog.warning(err, 0)
        else:
            mylog.info("SUCCESS: File exists --> {}".format(req_file), 0)

    return (precheck_msgs, precheck_rc)


def main():
    r"""Fabled main, where it all begins.

    Process flow
     - Determine if the DB is correctly setup for backups
     - Ensure we have connectivity to
        - DB requiring backup
        - DB that will hold the backup status
     - Is there enough space in the destination directory
     -
    """
    error_msgs = []
    error_rc = 0
    # try:
    parser = argparse.ArgumentParser(
        description="Backup and Restore Manager"
    )
    parser.add_argument("-c", "--create-schema",
                        help="Create schema to hold backup / restore status",
                        action="store_true"
                        )
    parser.add_argument("-a", "--action",
                        help="Perform backup / restore action of a DB",
                        choices = ["backup", "restore"],
                        )
    parser.add_argument("-d", "--dbname",
                        help="Database Name for Backup or Restore",
                        required=True
                        )
    parser.add_argument("-e", "--email",
                        help="Email Address to send messages",
                        )
    parser.add_argument("-P", "--pre_reqs",
                        help="Perform pre-requisite checks for Backup / "
                             "Restore of a DB",
                        action="store_true",
                        required=True
                        )
    parser.add_argument("-t", "--timestamp",
                        help="Timestamp (YYYYMMDD HH:MM:SS)",
                        action="store_true"
                        )
    parser.add_argument("-T", "--action_type",
                        help="Type of Backup or Restore",
                        choices=["full", "incr"],
                        default="full"
                        )
    args = parser.parse_args()

    if (args.action):
        action = args.action
        mylog.info("Action           --> {}".format(action), 0)

    if (args.action_type):
        action_type = args.action_type
        mylog.info("Action Type      --> {}".format(action_type), 0)

    if (args.email):
        recipient = args.email.split(',')
    else:
        recipient = maintainers
    mylog.info("Email Recipients --> {}".format(recipient), 0)

    dbname = args.dbname
    mylog.info("Database Name    --> {}".format(dbname), 0)
    if dbname not in dbs:
        mylog.critical("Invalid Database specified --> {}".format(dbname), 0)

    if (args.timestamp):
        timestamp = args.timestamp
    else:
        timestamp = datetime.now()
    today = timestamp.strftime("%Y-%m-%d")
    timestamp2 = timestamp.strftime("%Y%m%d_%H%M%S")
    mylog.info("Timestamp        --> {}".format(timestamp), 0)
    mylog.info("Timestamp2       --> {}".format(timestamp2), 0)
    mylog.info("Today            --> {}".format(today), 0)

    # pre_reqs is a required parameter. Therefore no need to check for else.
    if (args.pre_reqs):
        pre_reqs = args.pre_reqs
        mylog.info("Pre Reqs Checks  --> {}".format(pre_reqs), 0)
        (prereqs_msgs, prereqs_rc) = pre_req_checks(
            brman_db, dbname, mysql_db, today
        )
        if (prereqs_rc > 0):
            mylog.warning("FAILED: Pre-requisites. Error count --> {}".
                          format(prereqs_rc), 0)
            mylog.warning("Pre-requisite failure(s) --> {}".
                          format(prereqs_msgs), 0)
            error_rc += prereqs_rc
            error_msgs.append(prereqs_msgs)
        else:
            if (action == "backup"):
                (bkup_msgs, bkup_rc) = do_backup(
                    dbname, action_type, today, timestamp2
                )
                if (bkup_rc > 0):
                    mylog.warning("Error count --> {}".format(bkup_rc), 0)
                    error_rc += bkup_rc
                    error_msgs.append(bkup_msgs)
    exit(error_rc)

if __name__ == "__main__":
    mylog = obj_utils.LogMe()
    main()