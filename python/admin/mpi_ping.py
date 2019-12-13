#!/usr/local/bin/python3
"""Multiprocessing Ping.

This script will take a Network Range. Then ping the hosts using a defined
parallelism value.
For example:
    ./mp_ping.py -n 172.31.251.0/24 -p 10
will ping entire subnet 172.31.251.0/24 with 10 hosts at a time.

URLs
Netaddr         --> https://netaddr.readthedocs.io/en/latest/tutorial_01.html
Multiprocessing --> https://docs.python.org/2/library/multiprocessing.html?highlight=multiprocessing#the-process-class
"""

from lank import utils
from multiprocessing import Process, Pool
import ipaddress

sleep_time = 1.0

def multi_ping(subnet):
    """Ping the network using multiprocessing."""
    #print (type(subnet))
    #exit()
    for host in subnet.hosts():
        ping_cmd = "/bin/ping -c 1 -i 1 -w 1 " + str(host)
        (stdout, stderr, rc) = utils.runcmd(ping_cmd)
        print("{} --> {}".format(host, rc))


def mpool_ping(host):
    ping_cmd = "/bin/ping -c 1 -i 1 -w 1 " + str(host)
    (stdout, stderr, rc) = utils.runcmd(ping_cmd)
    if (rc == 0):
        rc_str = "Ping Succeeded"
    elif (rc == 1):
        rc_str = "Ping Failed"
    else:
        rc_str ="Unknown Ping Error"
    # print("{} --> {}".format(host, rc_str))
    # print("Ping --> {}".format(host))
    tup_rec = (str(host), rc_str)
    return (tup_rec)


def get_cidr(host):
    r"""Determine the cidr for a given host."""
    cidrs = ["172.31.251.0/24",
             "192.168.0.0/24",
             "165.160.200.0/24"]
    found = 0
    for net in cidrs:
        network = ipaddress.ip_network(net)
        if ipaddress.ip_address(host) in network:
            print ("Host --> {} in Network --> {}".format(host, net))
            found += 1
    if (found == 0):
        print ("No Network found for {}".format(host))


def process_args():
    """Process the inputs. Call multi_ping.

    This routine takes 2 arguments
    :subnet:        The subnet range to ping
    :parallelism:   Parallelism factor
    """
    # parallelism = 10
    subnet = "172.31.251.0/24"
    # multi_ping(subnet, parallelism)
    # exit(0)

    hosts = ipaddress.ip_interface(subnet)
    hosts_network = ipaddress.ip_network(subnet, strict=False)

    # print(hosts[0:4])
    network_ip = hosts.network
    broadcast_ip = hosts_network[-1]
    netmask_ip = hosts.netmask
    subnet_size = hosts_network.num_addresses

    print (hosts, hosts_network[0], hosts_network[-1],
           network_ip, broadcast_ip, netmask_ip,  subnet_size)
    # exit()

    # hosts = list(IPNetwork(subnet))
    # hosts.remove(network_ip)
    # hosts.remove(broadcast_ip)

    # exit()

    hosts_in_subnet = subnet_size
    parallelism = hosts_in_subnet
    if (parallelism > 254):
        parallelism = 254

    print("Network          --> {}".format(network_ip))
    print("Broadcast        --> {}".format(broadcast_ip))
    print("Segment Size     --> {}".format(subnet_size))
    print("Hosts in Segment --> {}".format(hosts_in_subnet))
    print("Parallelism      --> {}".format(parallelism))

    # print(hosts[0:10])
    # p = Process(target=mp_ping, args=(hosts[0:10],))
    # p.start()
    # exit(0)
    # count_hosts = 0
    # for host in hosts:
    #     if (count_hosts < parallelism):
    #         p = Process(target=mp_ping, args=(host,))
    #         count_hosts += 1
    #         print(count_hosts)
    #         p.start()
    # # time.sleep(sleep_time)
    # p.join()

    # Junk
    # multi_results = multi_ping(hosts_network)
    # exit()

    p = Pool(parallelism)
    results = p.map(mpool_ping, hosts_network)
    p.close()
    p.join()
    print(list(results))
    print(len(results))


if __name__ == "__main__":
    utils.init()
    #host = "172.31.252.1"
    host = "172.31.251.1"
    host = "192.168.0.255"
    host = "165.160.200.255"
    get_cidr(host)
    # process_args()
    exit(0)