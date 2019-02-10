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
from .lank import utils
from .lank import tls_schema
from .lank.tls_cfg import hosts_to_scan, recipient, dbid, dbtype


def process_parameters():
    """Process all input parameters."""
    pass


def main():
    """Fabled main where it all begins."""
    (error_message, rc) = process_parameters()

if __name__ == "__main__":
    utils.init()
    main()
