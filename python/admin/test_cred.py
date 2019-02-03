#!/usr/local/bin/python3

from lank import utils


utils.init()

# utils.create_key()
# exit()

dbname = "dmzdb"
dbuser = "dmzdb"
dbpass = "dmzdb"
dbport = "5432"

(db_name, db_user, db_pass, db_port) = utils.encrypt_creds(dbname, dbuser, dbpass, dbport)

# dbname = 'gAAAAABcV1HROmvUfUByqtZg5lS2HHRCXeDA36TE-uDrsgcExb8B3iEBHqdwuf0RLE_PDFlXf8RjRuC4Q0exn6ZSRW38wLbJ7g=='
# db_name = utils.decrypt_token(dbname)

print ("DBNAME --> {}".format(db_name))
print ("DBUSER --> {}".format(db_user))
print ("DBPASS --> {}".format(db_pass))
print ("DBPORT --> {}".format(db_port))
