#!/usr/local/bin/python3
"""Test Driven Development.

This suite of tests will pytest all functions in lank.obj_utils
Classes to test
  - Creds
    - encrypt_cred    -- Done
    - decrypt_token   -- Done
    - encrypt_creds   -- Done
    - decrypt_tokens  -- Done
    - create_key      -- Not started
  - Logme
    - critical
    - error
    - warning
    - info
    - debug
    - notset
    - writelog
"""
from lank import obj_utils
import pytest

# Test class DnsQuery
# @pytest.fixture
# def dns_qry():
#    return obj_utils.DnsQuery()

def test_get_dns_rec():
    r"""Get the DNS record for IP address and hostname.

    Getting the record will exercise all the methods within the DnsQyery
    class.
    Hostname   --> www.incspot.com
    IP Address --> 165.160.32.176
    """
    my_dns_ip = obj_utils.DnsQuery(ip_address='165.160.32.176')
    my_dns_host = obj_utils.DnsQuery(hostname='www.incspot.com')
    # my_dns_i_h = obj_utils.DnsQuery(ip_address='165.160.32.176', hostname="")
    # my_dns_h_i = obj_utils.DnsQuery(ip_address=None, hostname="www.incspot.com")

    expected_host = "incspot"
    expected_ip = "165.160.32.176"
    expected_ptr = "176.32.160.165.in-addr.arpa."
    expected_fqdn = "incspot.cscinfo.com."
    expected_cname = "The DNS query name does not exist: incspot.kellynoah.com."

    ip_dns_rec = my_dns_ip.get_dns_rec()
    host_dns_rec = my_dns_host.get_dns_rec()

    recd_host = ip_dns_rec[0]
    recd_ip = ip_dns_rec[1]
    recd_ptr = ip_dns_rec[2]
    recd_fqdn = ip_dns_rec[3]
    recd_cname = ip_dns_rec[4]

    assert expected_host == recd_host
    assert expected_ip == recd_ip
    assert expected_ptr == recd_ptr
    assert expected_fqdn == recd_fqdn
    assert expected_cname == recd_cname

    rcd_host = host_dns_rec[0]
    rcd_ip = host_dns_rec[1]
    rcd_ptr = host_dns_rec[2]
    rcd_fqdn = host_dns_rec[3]
    rcd_cname = host_dns_rec[4]

    assert expected_host == rcd_host
    assert expected_ip == rcd_ip
    assert expected_ptr == rcd_ptr
    assert expected_fqdn == rcd_fqdn
    assert expected_cname == rcd_cname


# Test class Creds
@pytest.fixture
def creds():
    """Decorator to return an instance of class Creds."""
    return obj_utils.Creds()


def test_encrypt_cred():
    """Define a Credential, encrypt it. Decrypt it to confirm."""
    cred = "Pytest Cred"
    # Create an instance of the class
    my_cred = obj_utils.Creds()

    # Encrypt the Credential
    e_cred = my_cred.encrypt_cred(cred)

    # Now decrypt the credential
    e_token = my_cred.decrypt_token(e_cred)

    # After decryption, both cred and e_token should match
    assert cred == e_token


def test_encrypt_creds(creds):
    """Encrypt DB credentials and decrypt them as well. Verify.

    dbname, dbuser, dbpass, dbhost, dbport
    The parameter 'creds' will call the method 'creds' and receive an
    instance of the obj_utils.Creds()
    """
    dbname = "prueba"
    dbuser = "prueba_user"
    dbpass = "prueba_password"
    dbhost = "prueba_host"
    dbport = "prueba_port"

    # Create an instance of the class
    # my_creds = obj_utils.Creds()

    # Encrypt the Credentials
    (e_dbname, e_dbuser, e_dbpass, e_dbhost, e_dbport) = creds.encrypt_creds(
        dbname, dbuser, dbpass, dbhost, dbport)

    # Now decrypt the credential
    (d_dbname, d_dbuser, d_dbpass, d_dbhost, d_dbport) = creds.decrypt_tokens(
        e_dbname, e_dbuser, e_dbpass, e_dbhost, e_dbport)

    # After decryption, both cred and e_token should match
    assert (dbname, dbuser, dbpass, dbhost, dbport) == (
        d_dbname, d_dbuser, d_dbpass, d_dbhost, d_dbport)
