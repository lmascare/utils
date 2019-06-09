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
@pytest.fixture
def dns_qry():
    return obj_utils.DnsQuery()


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
