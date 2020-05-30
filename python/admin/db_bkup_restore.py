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
 - Check if DB requested are configured
"""
from lank import obj_utils
from lank.lank_cfg import host, scriptname, maintainers
from lank.db_bkup_restore_cfg import dbs, brman_db, dir_perms
from datetime import datetime

import argparse
import os
# import stat

def pre_req_checks(brman_db, dbname):
    r"""Pre-requisite checks to ensure DB backup / restore will succceed.

    Following checks are implemented
     - Establish connectivity to the BRMAN database and Target DB
     - Ensure DB properties are correctly set
        - Binary Logs are enabled
     - Ensure destination directories are present with valid permissions

    :param      dbname:         Database to be backed up
    :returns    precheck_msgs   Messages from the checks
                precheck_rc      Count of Errors
    """
    precheck_msgs = []
    precheck_rc = 0
    # Extract properties of the DB
    brman_dbid = dbs[brman_db]["dbid"]
    brman_dbtype = dbs[brman_db]["dbtype"]

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

    # Establish connectivity

    # Verify DB settings

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

    if (args.email):
        recipient = args.email.split(',')
    else:
        recipient = maintainers
    mylog.info("Email Recipients --> {}".format(recipient), 0)

    dbname = args.dbname
    mylog.info("Database Name    --> {}".format(dbname), 0)

    if (args.timestamp):
        timestamp = args.timestamp
    else:
        timestamp = datetime.now()
    mylog.info("Timestamp        --> {}".format(timestamp), 0)

    if (args.action_type):
        action_type  = args.action_type
        mylog.info("Action Type      --> {}".format(action_type), 0)

    # Establish a Cursor and Connection to the database. At this time
    # all options require a connection to the Database.

    # The state of the db backups and restore is in the brman DB.
    # brman_dbid = dbs["brman"]["dbid"]
    # brman_dbtype = dbs["brman"]["dbtype"]

    # dbid = dbs[dbname]["dbid"]
    # dbtype = dbs[dbname]["dbtype"]

    # mydb_brman = obj_utils.DBConnect(brman_dbid, brman_dbtype)
    # mydb = obj_utils.DBConnect(dbid, dbtype)

    if (args.pre_reqs):
        pre_reqs = args.pre_reqs
        mylog.info("Pre Reqs Checks  --> {}".format(pre_reqs), 0)
        (prereqs_msgs, prereqs_rc) = pre_req_checks(brman_db, dbname)
        if (prereqs_rc > 0):
            mylog.warning("Error count --> {}".format(prereqs_rc), 0)
            error_rc += prereqs_rc
            error_msgs.append(prereqs_msgs)

    # except Exception as e:
    # error_rc += 1
    # err = "Errors in {}. Error Code --> {}. RC --> {}".\
    #     format(scriptname, error_msgs, error_rc)
    # mylog.warning(err, 0)

    # exit(error_rc)

if __name__ == "__main__":
    mylog = obj_utils.LogMe()
    main()