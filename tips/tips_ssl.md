# SSL / TLS technologies

### Querying for SSL / TLS Protocols
```text
openssl s_client -connect www.incspot.com:443 -tls1
openssl s_client -connect www.incspot.com:443 -tls1_1
openssl s_client -connect www.incspot.com:443 -tls1_2
openssl s_client -connect www.incspot.com:443 -ssl3

# Using nmap
nmap --script ssl-enum-ciphers -p 443 www.ibm.com
``` 
### Generating SSL Certs
#### [Lets Encryt](https://certbot.eff.org/lets-encrypt/ubuntuxenial-apache)