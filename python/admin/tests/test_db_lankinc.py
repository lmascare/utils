#!/usr/local/bin/python3
r"""TDD for Postgres SQL DB.

The tests will
    - Validate a table exists
    - Columns in the table are as expected
"""
from lank import obj_utils
import pytest



# @pytest.fixture
# def dbc(dbid, dbtype, timeout):
#     r"""Connect to the DB and get the Cursor and Connection."""
#     return obj_utils.DBConnect(dbid, dbtype, timeout)

def test_connection():
    r"""Establish a connection to the DB."""
    dbid = "lankinc"
    dbtype = "postgres"
    timeout = 5

    db = "lankinc"
    dbc = obj_utils.DBConnect(dbid, dbtype, timeout)
    (cursor, connection) = dbc.connect()
    sql = "select current_database()"
    cursor.execute(sql)
    dbname = (cursor.fetchall()[0][0])
    assert dbname == db

def test_invalid_dbid():
    r"""Test response to an invalid DB."""
    dbid = "prueba"
    dbtype = "postgres"
    timeout = 5
    dbc = obj_utils.DBConnect(dbid, dbtype, timeout)
    (cursor, connection) = dbc.connect()
    assert cursor == None
    assert connection == None

# Verify properties of a table
"""
select 
    column_name,
    data_type,
    character_maximum_length,
    character_octet_length,
    is_nullable
from
    information_schema.columns 
where
    table_name = 'core_email_data';
"""
