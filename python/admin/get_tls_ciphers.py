#!/usr/local/bin/python3
"""
nmap - Scanner

https://pypi.org/project/python-nmap/
https://xael.org/norman/python/python-nmap/python-nmap-0.4.1.tar.gz

nmap --script ssl-enum-ciphers -p 443 www.ibm.com
"""
import nmap
import xmltodict

from datetime import datetime
from lank import utils
from lank import tls_schema
from lank.tls_cfg import dbid, dbtype, hosts_to_scan, ports_to_scan, \
    recipient

# scan_host = 'www.google.com'
# scan_host = 'www.incspot.com'
# scan_host = 'www.ibm.com'
# scan_host = 'www.microsoft.com'
#ToDo
# scan_host = "www.nytimes.com"
#END ToDo

# scan_host = "www.facebook.com"
#scan_host = "www.redhat.com"
scan_host = "www.bloomberg.com"
scan_host = "www.bloombergpolarlake.com"
scan_host = "www.americanprairie.org"
scan_host = "students.sbschools.org"

scan_port = '443'
nm = nmap.PortScanner()
try:
    nm.scan(scan_host, arguments='--script ssl-enum-ciphers -p 443')
    nmap_results = nm.get_nmap_last_output()
except Exception as e:
    utils.logit("info", "Error scanning host --> {}.".format(scan_host), 0)
    utils.logit("critical", "Error Code --> {}".format(e), 1)
# print (nmap_results)

try:
    doc = xmltodict.parse(nmap_results)
except Exception as e:
    utils.logit("critical", "Unable to convert XML to Dict. Error --> {}".
                format(e), 1)

# with open('nytimes_xml') as f:
# # with open('incspot_xml') as f:
#     doc = xmltodict.parse(f.read())

nmap_run = doc["nmaprun"]

scanner = nmap_run["@scanner"]
cli = nmap_run["@args"]
ver = nmap_run['@version']

verbosity = nmap_run['verbose']['@level']
debug_lvl = nmap_run['debugging']['@level']

nmap_start_time = nmap_run["@start"]
nmap_start_time_ts = datetime.fromtimestamp(int(nmap_start_time)).\
    strftime("%Y-%m-%d %H:%M:%S")

scan_info = nmap_run['scaninfo']
scan_type = scan_info["@type"]
scan_protocol = scan_info['@protocol']

nmap_host = nmap_run["host"]
nmap_hostnames = nmap_host["hostnames"]
nmap_hostname = nmap_hostnames["hostname"]

test_start = nmap_host["@starttime"]
test_start_ts = datetime.fromtimestamp(int(test_start)).\
    strftime("%Y-%m-%d %H:%M:%S")

test_end = nmap_host['@endtime']
test_end_ts = datetime.fromtimestamp(int(test_end)).\
    strftime("%Y-%m-%d %H:%M:%S")

status = nmap_host['status']['@state']
ip_address = nmap_host['address']['@addr']

if type(nmap_hostname) is list:
    hostname = nmap_hostname[0]['@name']
    fqdn = nmap_hostname[1]['@name']
else:
    hostname = nmap_hostname['@name']
    fqdn = None
# hostname = nmap_hostname[0]['@name']
# fqdn = nmap_hostname[1]['@name']

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
nmap_end_time_ts = datetime.fromtimestamp(int(nmap_end_time)).\
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
            cipher_value0     = port_table[p_c]['table'][0]['table'][c_c]['elem'][0]['#text']
            cipher_dict[cipher_key0] = cipher_value0

            cipher_key1 = port_table[p_c]['table'][0]['table'][c_c]['elem'][1]['@key']
            cipher_value1  = port_table[p_c]['table'][0]['table'][c_c]['elem'][1]['#text']
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
        cipher_value0     = port_table['table'][0]['table'][c_c]['elem'][0]['#text']
        cipher_dict[cipher_key0] = cipher_value0

        cipher_key1 = port_table['table'][0]['table'][c_c]['elem'][1]['@key']
        cipher_value1  = port_table['table'][0]['table'][c_c]['elem'][1]['#text']
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

exit(0)
