#!/usr/local/bin/python3.7

from lank import obj_utils

dbid = "lankinc"
dbtype = "postgres"
timeout = 60

mydb = obj_utils.DBConnect(dbid, dbtype, timeout)
# print (type(mydb))

(cursor, connection) = mydb.connect()

sql = "select count(*) from core_email_data"

cursor.execute(sql)
rows = cursor.fetchall()
print(rows[0][0])

sql_db = "Select current_database()"
cursor.execute(sql_db)
dbname = (cursor.fetchall())[0][0]
print (dbname)

# Get the table definition and verify it matches definition
table_core_email_data = """
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
cursor.execute(table_core_email_data)
core_email_data_schema = cursor.fetchall()
print (core_email_data_schema)

core_email_data_def = [
    ('sender', 'character varying', 254, 1016, 'NO'),
    ('recipient', 'character varying', 254, 1016, 'NO'),
    ('subject', 'character varying', 70, 280, 'NO'),
    ('body', 'text', None, 1073741824, 'NO'),
    ('send_time', 'timestamp with time zone', None, None, 'NO'),
    ('cc_myself', 'boolean', None, None, 'NO'),
    ('email_tag', 'character varying', 32, 128, 'NO'),
    ('id', 'bigint', None, None, 'NO')
]

table_defs = {
    "core_email_data": {
        "sender": ['character varying', '254', '1016', 'NO'],
        "recipient": ['character varying', '254', '1016', 'NO'],
        "subject": ['character varying', '70', '280', 'NO'],
        "body": ['text', None, '1073741824', 'NO'],
        "send_time": ['timestamp with time zone', None, None, 'NO'],
        "cc_myself": ['boolean', None, None, 'NO'],
        "email_tag": ['character varying', 32, 128, 'NO'],
        "id": ['bigint', None, None, 'NO'],
    },
}

# Diff of 2 lists
l1 = ['1', '2', 'b']
r1 = ['3', '4', 'b', '1',]

my_list = obj_utils.list_diff_union(l1, r1)
diff = my_list.diff_lists()

print (f"Difference --> {diff}")

union = my_list.union_lists()
print (f"Union      --> {union}")


# (diff, union) = obj_utils.diff_lists(l1, l2)
# print (diff)
# print (union)