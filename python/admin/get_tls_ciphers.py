#!/usr/local/bin/python3
"""
nmap - Scanner

https://pypi.org/project/python-nmap/
https://xael.org/norman/python/python-nmap/python-nmap-0.4.1.tar.gz

nmap --script ssl-enum-ciphers -p 443 www.ibm.com
"""
import nmap
scan_host = 'www.ibm.com'
scan_port = '443'
# nm = nmap.PortScanner()
# nmap_results = nm.scan(scan_host, arguments='--script ssl-enum-ciphers -p 443')
# print (nmap_results)
# print (nmap_results.keys())

results = {
    'nmap':
        {
            'command_line': 'nmap -oX - --script ssl-enum-ciphers -p 443 www.ibm.com',
            'scaninfo': {'tcp': {'method': 'connect', 'services': '443'}},
            'scanstats': {'timestr': 'Mon Jan 28 20:44:44 2019', 'elapsed': '2.78', 'uphosts': '1', 'downhosts': '0', 'totalhosts': '1'}},
    'scan':
        {
            '96.6.191.242':
                {'hostnames': [{'name': 'www.ibm.com', 'type': 'user'},
                               {'name': 'a96-6-191-242.deploy.static.akamaitechnologies.com', 'type': 'PTR'}],
                 'addresses': {'ipv4': '96.6.191.242'},
                 'vendor': {},
                 'status': {'state': 'up', 'reason': 'syn-ack'},
                 'tcp': {443: {'state': 'open',
                               'reason': 'syn-ack',
                               'name': 'https',
                               'product': '',
                               'version': '',
                               'extrainfo': '',
                               'conf': '3',
                               'cpe': '',
                               'script': {'ssl-enum-ciphers':
                                              '\n  TLSv1.0: '
                                              '\n    ciphers: '
                                              '\n      TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A'
                                              '\n      TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (secp256r1) - A'
                                              '\n      TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A'
                                              '\n      TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A'
                                              '\n    compressors: \n      NULL'
                                              '\n    cipher preference: server'
                                              '\n  TLSv1.1: '
                                              '\n    ciphers: '
                                              '\n      TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A'
                                              '\n      TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (secp256r1) - A'
                                              '\n      TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A'
                                              '\n      TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A'
                                              '\n    compressors: \n      NULL'
                                              '\n    cipher preference: server'
                                              '\n  TLSv1.2: '
                                              '\n    ciphers: '
                                              '\n      TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (secp256r1) - A'
                                              '\n      TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (secp256r1) - A'
                                              '\n      TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (secp256r1) - A'
                                              '\n      TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (secp256r1) - A'
                                              '\n      TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A'
                                              '\n      TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (secp256r1) - A'
                                              '\n      TLS_RSA_WITH_AES_256_GCM_SHA384 (rsa 2048) - A'
                                              '\n      TLS_RSA_WITH_AES_128_GCM_SHA256 (rsa 2048) - A'
                                              '\n      TLS_RSA_WITH_AES_256_CBC_SHA256 (rsa 2048) - A'
                                              '\n      TLS_RSA_WITH_AES_128_CBC_SHA256 (rsa 2048) - A'
                                              '\n      TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A'
                                              '\n      TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A'
                                              '\n    compressors: \n      NULL'
                                              '\n    cipher preference: server'
                                              '\n  least strength: A'
                                          }
                               }
                         }
                 }
        }
}

#print (type(results))
