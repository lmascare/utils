#!/usr/local/bin/python3

from lank import utils

if __name__ == "__main__":
    utils.init()
    # ip = '172.31.251.1'

    # host_name = "www.incspot.com"
    # host_name = '165.160.32.176'
    host_name = "google.com"
    # host_name = "172.217.10.142"
    # import dns.resolver
    # my_res = dns.resolver.Resolver()
    # ip = my_res.query(host_name, "A")
    # for host_ip in ip:
    #     print(host_ip)

    # from dns import resolver
    # ip = resolver.query(host_name, "A")
    # print(ip[0])

    utils.dns_queries(host_name)
    # (host_name, host_ip, host_ptr) = utils.dns_queries(host_name)
    tuple_entry = utils.dns_queries(host_name)
    print(tuple_entry)
    # print("Hostname --> {}\n"
    #       "IP       --> {}\n"
    #       "PTR      --> {}".format(host_name, host_ip, host_ptr))