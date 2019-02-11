"""Configuration for TLS Processing."""

dbid = "dmzdb"
dbtype = "postgres"
import os
host = os.uname()[1]

hosts_to_scan = [
    "www.bloomberg.com",
    "www.bloombergpolarlake.com"
    "www.google.com",
    "www.ibm.com",
    "www.incspot.com",
    "www.redhat.com",
    "www.americanprairie.org",
    "students.sbschools.org",
]
ports_to_scan = ['443']

recipient = ["larry.masc@gmail.com"]
