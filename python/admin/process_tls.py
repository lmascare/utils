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
from multiprocessing import Pool
from datetime import datetime
from functools import partial
import nmap
import xmltodict
import argparse


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

        # sql_stmt = cursor.mogrify(create_sql)
        utils.logit("info", "SQL Statement --> {}".format(create_sql), 0)
        error_message.append(error_detail)
        error_message.append(create_sql)

    return(error_message, error_rc)


def process_host(scan_port, scan_host):
    """NMap scan a host. Process the results and return to calling program."""
    nm = nmap.PortScanner()
    try:
        nmap_args = '--script ssl-enum-ciphers -p ' + scan_port
        nm.scan(scan_host, arguments=nmap_args)
        nmap_results = nm.get_nmap_last_output()
    except Exception as e:
        utils.logit("info", "Error scanning host --> {}.".format(scan_host), 0)
        utils.logit("critical", "Error Code --> {}".format(e), 1)

    try:
        doc = xmltodict.parse(nmap_results)
    except Exception as e:
        utils.logit("critical", "Unable to convert XML to Dict. Error --> {}".
                    format(e), 1)

    nmap_run = doc["nmaprun"]

    scanner = nmap_run["@scanner"]
    cli = nmap_run["@args"]
    ver = nmap_run['@version']

    verbosity = nmap_run['verbose']['@level']
    debug_lvl = nmap_run['debugging']['@level']

    nmap_start_time = nmap_run["@start"]
    nmap_start_time_ts = datetime.fromtimestamp(int(nmap_start_time)). \
        strftime("%Y-%m-%d %H:%M:%S")

    scan_info = nmap_run['scaninfo']
    scan_type = scan_info["@type"]
    scan_protocol = scan_info['@protocol']

    nmap_host = nmap_run["host"]
    nmap_hostnames = nmap_host["hostnames"]
    nmap_hostname = nmap_hostnames["hostname"]

    test_start = nmap_host["@starttime"]
    test_start_ts = datetime.fromtimestamp(int(test_start)). \
        strftime("%Y-%m-%d %H:%M:%S")

    test_end = nmap_host['@endtime']
    test_end_ts = datetime.fromtimestamp(int(test_end)). \
        strftime("%Y-%m-%d %H:%M:%S")

    status = nmap_host['status']['@state']
    ip_address = nmap_host['address']['@addr']

    if type(nmap_hostname) is list:
        hostname = nmap_hostname[0]['@name']
        fqdn = nmap_hostname[1]['@name']
    else:
        hostname = nmap_hostname['@name']
        fqdn = None

    nmap_ports = nmap_host["ports"]
    nmap_port = nmap_ports["port"]
    port_script = nmap_port['script']
    port_table = port_script['table']

    protocol = nmap_port['@protocol']
    test_port = nmap_port['@portid']
    port_state = nmap_port['state']['@state']
    service = nmap_port['service']['@name']
    nmap_script = nmap_port['script']['@id']

    nmap_runstats = nmap_run['runstats']['finished']

    nmap_end_time = nmap_runstats['@time']
    nmap_end_time_ts = datetime.fromtimestamp(int(nmap_end_time)). \
        strftime("%Y-%m-%d %H:%M:%S")
    time_string = nmap_runstats['@timestr']
    elapsed_time = nmap_runstats['@elapsed']
    port_test_status = nmap_runstats['@exit']
    test_summary = nmap_runstats['@summary']

    print("Scanner          --> {}".format(scanner))
    print("CLI              --> {}".format(cli))
    print("NMAP Script      --> {}".format(nmap_script))
    print("NMAP Start Time  --> {} - {}".format(nmap_start_time, nmap_start_time_ts))
    print("Version          --> {}".format(ver))
    print("Scan Type        --> {}".format(scan_type))
    print("Scan Protocol    --> {}".format(scan_protocol))
    print("Verbosity        --> {}".format(verbosity))
    print("Debug Level      --> {}".format(debug_lvl))
    print("Test Start Time  --> {} - {}".format(test_start, test_start_ts))
    print("Test End Time    --> {} - {}".format(test_end, test_end_ts))
    print("Host State       --> {}".format(status))
    print("IP Address       --> {}".format(ip_address))
    print("Hostname         --> {}".format(hostname))
    print("FQDN             --> {}".format(fqdn))
    print("Port Protocol    --> {}".format(protocol))
    print("Port Test        --> {}".format(test_port))
    print("Port State       --> {}".format(port_state))
    print("Port Service     --> {}".format(service))
    print("NMAP End Time    --> {} - {}".format(nmap_end_time, nmap_end_time_ts))
    print("Time String      --> {}".format(time_string))
    print("Elapsed Time     --> {} secs".format(elapsed_time))
    print("Status           --> {}".format(port_test_status))
    print("Summary          --> {}".format(test_summary))

    if type(port_table) is list:
        tls_ssl_count = len(port_table)
        for p_c in range(tls_ssl_count):
            tls_ssl = port_table[p_c]['@key']
            cipher_preference = port_table[p_c]['elem']['#text']
            print("Protocol Version --> {}".format(tls_ssl))

            cipher_count = len(port_table[p_c]['table'][0]['table'])
            # print(cipher_count)
            cipher_dict = {}
            for c_c in range(cipher_count):
                cipher_key0 = port_table[p_c]['table'][0]['table'][c_c]['elem'][0]['@key']
                cipher_value0 = port_table[p_c]['table'][0]['table'][c_c]['elem'][0]['#text']
                cipher_dict[cipher_key0] = cipher_value0

                cipher_key1 = port_table[p_c]['table'][0]['table'][c_c]['elem'][1]['@key']
                cipher_value1 = port_table[p_c]['table'][0]['table'][c_c]['elem'][1]['#text']
                cipher_dict[cipher_key1] = cipher_value1

                cipher_key2 = port_table[p_c]['table'][0]['table'][c_c]['elem'][2]['@key']
                cipher_value2 = port_table[p_c]['table'][0]['table'][c_c]['elem'][2]['#text']
                cipher_dict[cipher_key2] = cipher_value2

                print("         Text --> {}, kexinfo --> {} Strength --> {}".
                      format(cipher_dict['name'], cipher_dict['kex_info'], cipher_dict['strength']))

            compressor_value = port_table[p_c]['table'][1]['elem']
            print("         Compressors       --> {}".format(compressor_value))
            print("         Cipher Preference --> {}\n".format(cipher_preference))
        least_strength = port_script['elem']['#text']
        print("Least Strength   --> {}".format(least_strength))
    else:
        tls_ssl = port_table['@key']
        cipher_preference = port_table['elem']['#text']
        print("Protocol Version --> {}".format(tls_ssl))
        cipher_count = len(port_table['table'][0]['table'])
        cipher_dict = {}
        for c_c in range(cipher_count):
            cipher_key0 = port_table['table'][0]['table'][c_c]['elem'][0]['@key']
            cipher_value0 = port_table['table'][0]['table'][c_c]['elem'][0]['#text']
            cipher_dict[cipher_key0] = cipher_value0

            cipher_key1 = port_table['table'][0]['table'][c_c]['elem'][1]['@key']
            cipher_value1 = port_table['table'][0]['table'][c_c]['elem'][1]['#text']
            cipher_dict[cipher_key1] = cipher_value1

            cipher_key2 = port_table['table'][0]['table'][c_c]['elem'][2]['@key']
            cipher_value2 = port_table['table'][0]['table'][c_c]['elem'][2]['#text']
            cipher_dict[cipher_key2] = cipher_value2

            print("         Text --> {}, kexinfo --> {} Strength --> {}".
                  format(cipher_dict['name'], cipher_dict['kex_info'], cipher_dict['strength']))

        compressor_value = port_table['table'][1]['elem']
        print("         Compressors       --> {}".format(compressor_value))
        print("         Cipher Preference --> {}\n".format(cipher_preference))
        least_strength = port_script['elem']['#text']
        print("Least Strength   --> {}".format(least_strength))

    return ('pass')


def process_parameters():
    """Process all input parameters."""
    parser = argparse.ArgumentParser(description="Process TLS Data")
    parser.add_argument("-c", "--create_table",
                        help="Create TLS table. [all] for entire schema",
                        metavar="table_name")
    parser.add_argument("-m", "--mpx",
                        help="Multiprocessing Factor (Default=4)",
                        metavar="mpx_factor",
                        default=4)
    parser.add_argument("-p", "--scan_port",
                        help="Port to scan (Default=443)",
                        metavar="scan_port",
                        default=str(443))
    parser.add_argument("-s", "--scan_host",
                        help="Scan Hosts. 'all' for all configured hosts",
                        metavar="scan_host")
    parser.add_argument("-t", "--timestamp",
                        help="Pass timestamp (YYYYMMDD)",
                        metavar="timestamp")
    parser.add_argument("-u", "--update_db",
                        help="Update CMDB with results",
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
        # This is a standalone routine.
        return (error_message, error_rc)

    if (args.timestamp):
        timestamp = args.timestamp
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    utils.logit("info", "Timestamp --> {}".format(timestamp), 0)

    if (args.mpx):
        mpx = int(args.mpx)
    utils.logit("info", "Multiprocessing factor --> {}".format(mpx), 0)

    if (args.scan_port):
        scan_port = str(args.scan_port)
    utils.logit("info", "Port to scan --> {}".format(scan_port), 0)

    if (args.scan_host):
        if (args.scan_host == 'all'):
            scan_host = hosts_to_scan
        else:
            scan_host = args.scan_host if type (args.scan_host) is list else \
                [args.scan_host]
        utils.logit("info", "Hosts to scan --> {}".format(scan_host), 0)

        s = Pool(mpx)
        func = partial(process_host, scan_port)
        scan_results = s.map(func, scan_host)
        s.close()
        s.join()
        print (scan_results)


    # Return to main with message and rc
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
