#!/usr/local/bin/python3

import pandas as pd
import xmltodict

with open('ibm_ciphers.xml') as fd:
    doc = xmltodict.parse(fd.read())

pd_nmap = pd.DataFrame(doc)

# print (pd_nmap.set_index("nmaprun"))
print (pd_nmap.pivot_table)
# print (pd_nmap.dtypes)