#!/usr/local/bin/python3.7
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
from netaddr import *
import time
sleep_time = 1.0

def multi_ping(subnet):
    """Ping the network using multiprocessing."""
    for host in IPNetwork(subnet).iter_hosts():
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

    hosts = IPNetwork(subnet)

    # print(hosts[0:4])
    network_ip = hosts.network
    broadcast_ip = hosts.broadcast
    subnet_size = hosts.size

    # print (hosts, network_ip, broadcast_ip, subnet_size)
    # exit()
    hosts = list(IPNetwork(subnet))
    hosts.remove(network_ip)
    hosts.remove(broadcast_ip)

    hosts_in_subnet = (len(hosts))
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
    p = Pool(parallelism)
    results = p.map(mpool_ping, hosts)
    print(list(results))
    print(len(results))


if __name__ == "__main__":
    utils.init()
    process_args()
    exit(0)