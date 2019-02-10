#!/usr/local/bin/python3

import xmltodict
from datetime import datetime

with open('nytimes_xml') as f:
# with open('incspot_xml') as f:
    doc = xmltodict.parse(f.read())

# print (doc)
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

# print (type(nmap_hostname), hostname, fqdn)

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

# print (type(port_table))
# exit(0)
cipher_dict = {}

#NYTIMES
cipher = port_table['@key']
ciphers = port_table['table'][0]['@key']
compressor = port_table['table'][1]['elem']

cipher_strength = port_table['table'][0]['table'][0]['elem'][0]['#text']
cipher_name = port_table['table'][0]['table'][0]['elem'][1]['#text']
cipher_kex = port_table['table'][0]['table'][0]['elem'][2]['#text']

print (cipher, ciphers, compressor, cipher_name, cipher_kex, cipher_strength)
#NYTIMES

# port_table = doc['nmaprun']['host']['ports']['port']['script']['table']
# ciphers = doc['nmaprun']['host']['ports']['port']['script']['table'][0]['table'][0]['table'][0]
# cipher_elem = ciphers['elem']

# len_cipher_elem = len(cipher_elem)
# for l_c_e in range(len_cipher_elem):
#     print (cipher_elem[l_c_e].items())

# print (type(port_table[0]))
# for k, v in port_table[0].items():
#     print (k, type(v))

# exit(0)

# cipher           = doc['nmaprun']['host']['ports']['port']['script']['table'][0]['table'][0]['@key']
# compressor       = doc['nmaprun']['host']['ports']['port']['script']['table'][0]['table'][1]['@key']
# compressor_value = doc['nmaprun']['host']['ports']['port']['script']['table'][0]['table'][1]['elem']

# Next line is from NY Times as it is not a list
#cipher_strength = port_table['table'][0]['table'][0]['elem'][0]['#text']
cipher_key0      = port_table[0]['table'][0]['table'][0]['elem'][0]['@key']
cipher_value0    = port_table[0]['table'][0]['table'][0]['elem'][0]['#text']

cipher_dict[cipher_key0] = cipher_value0

cipher_key1      = port_table[0]['table'][0]['table'][0]['elem'][1]['@key']
cipher_value1    = port_table[0]['table'][0]['table'][0]['elem'][1]['#text']

cipher_dict[cipher_key1] = cipher_value1


cipher_key2      = port_table[0]['table'][0]['table'][0]['elem'][2]['@key']
cipher_value2    = port_table[0]['table'][0]['table'][0]['elem'][2]['#text']
cipher_dict[cipher_key2] = cipher_value2

print (cipher_dict['name'], cipher_dict['kex_info'], cipher_dict['strength'])

print (cipher_dict.items())

for k, v in cipher_dict.items():
    print (k, cipher_dict[k])

# print (cipher_dict['name'], cipher_dict['kex_info'], cipher_dict['strength'])

# print (cipher, compressor, compressor_value, cipher_key0, cipher_key1, cipher_key2)
#
# print ("{} --> {}".format(cipher_key0, cipher_value0))
# print ("{} --> {}".format(cipher_key1, cipher_value1))
# print ("{} --> {}".format(cipher_key2, cipher_value2))