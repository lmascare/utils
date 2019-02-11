#!/usr/local/bin/python3
r"""Script to perform all TLS related activities.

The intent of process_tls.py is to do the following
    - Run nmap with --ssl-enum-ciphers script with XML output
    - Extract all the relevant data from the XML script using the Python
      module xml2dict
    - Populate a history table with the data
    - Update the state table with changed data
    - Report (email recipients) on changes

Todo
    - Run nmap with --ssl-enum-ciphers script with XML output
    - Extract all the relevant data from the XML script using the Python
      module xml2dict
    - Populate a history table with the data
    - Update the state table with changed data
    - Report (email recipients) on changes
"""
from lank import utils
from lank.tls_schema import tls_tables
from lank.tls_cfg import hosts_to_scan, recipient, dbid, dbtype
import argparse
from datetime import datetime


def fail(message):
    """Process failures during a dict.get."""
    utils.logit("critical", "Failed dict.get routine. Error --> {}".
                format(message), 0)


def create_schema(cursor, connection, table):
    """Create schema for TLS processing.

    This function creates a table or all tables in the TLS schema.
    :param  cursor:
    :param  connection:
    :param  table:

    :returns    (error_message, error_rc)
    """
    error_message = []
    error_rc = 0
    utils.logit("info", "In create_schema function", 0)
    if (table == "all"):
        tables = tls_tables.keys()
        utils.logit("info", "Request to create entire schema", 0)
    else:
        utils.logit("info", "Request to create table --> {}".format(table), 0)
        tables = table if type(table) is list else [table]

    for table_name in tables:
        utils.logit("info", "Creating table --> {}".format(table_name), 1)
        (create_sql, *args) = tls_tables.get(table_name, fail)(table_name)
        try:
            cursor.execute(create_sql)
            error_detail = ["Successfully created table --> {}".format(table_name)]
            utils.logit("info", error_detail, 0)
            connection.commit()
        except Exception as e:
            error_rc += 1
            error_detail = ["ERROR creating table --> {}".format(table_name)]
            utils.logit("warning", error_detail, 0)
            utils.logit("warning", "SQL Error --> {}".format(e), 0)
            error_detail.append(e)

        sql_stmt = cursor.mogrify(create_sql)
        utils.logit("info", sql_stmt, 0)
        error_message.append(error_detail)
        error_message.append(sql_stmt)

    return(error_message, error_rc)


def process_parameters():
    """Process all input parameters."""
    parser = argparse.ArgumentParser(description="Process TLS Data")
    parser.add_argument("-c", "--create_table",
                        help="Create TLS table. [all] for entire schema",
                        metavar="table_name")
    parser.add_argument("-s", "--scan_host", help="Scan Hosts(s)",
                        metavar="scan_host")
    parser.add_argument("-t", "--timestamp", help="Pass timestamp",
                        metavar="timestamp")
    parser.add_argument("-u", "--update_db", help="Update CMDB with results",
                        action="store_true")
    args = parser.parse_args()

    error_message = []
    error_rc = 0

    if (args.create_table):
        table = args.create_table
        (cursor, connection) = utils.db_connect(dbid, dbtype)
        (table_message, table_rc) = create_schema(cursor, connection, table)
        error_message.append(table_message)
        error_rc += table_rc

    return (error_message, error_rc)

def main():
    """Fabled main where it all begins."""
    (error_message, rc) = process_parameters()
    if (rc > 0):
        utils.logit("warning", "Script ended with '{}' error(s)".format(rc), 1)
        # utils.logit("warning", "Error Message --> {}".format(error_message), 0)
    else:
        utils.logit("info", "Congratulations. Script completed successfully", 1)

if __name__ == "__main__":
    utils.init()
    main()
