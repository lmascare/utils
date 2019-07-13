#!/usr/local/bin/python3.7

from lank import obj_utils

# my_dns = obj_utils.DnsQuery(ip_address='172.217.10.68', hostname="")
# my_dns = obj_utils.DnsQuery(ip_address=None, hostname="www.google.com")

# my_dns = obj_utils.DnsQuery(ip_address=None, hostname="www.ibm.com")

#my_dns = obj_utils.DnsQuery(ip_address='165.160.32.176', hostname="")
# my_dns = obj_utils.DnsQuery(ip_address=None, hostname="www.incspot.com")
my_dns = obj_utils.DnsQuery(ip_address='165.160.32.176')
# my_dns = obj_utils.DnsQuery(hostname="www.incspot.com")
# my_dns = obj_utils.DnsQuery(hostname="www.ibm.com")


#print ("CNAME --> {}".format(my_dns.get_cname()))
#print ("FQDN  --> {}".format(my_dns.get_fqdn()))
# print ("Host  --> {}".format(my_dns.get_hostname()))
# print ("IP    --> {}".format(my_dns.get_host_ip()))
# print ("PTR   --> {}".format(my_dns.get_ptr()))



# print (my_dns.get_dns_rec())
# rec = my_dns.get_dns_rec()
rec2 = f"DNS Rec --> {my_dns.get_dns_rec()}"
# print ("{}".format(rec))

# print(f"DNS Rec --> {my_dns.get_dns_rec()}")

print (rec2)