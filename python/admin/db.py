#!/usr/bin/python

#!/usr/local/bin/python3

from lank import utils
import string
from lank.vars import db_creds
utils.init()

# dbid = "lifecycle"
# dbtype = "mysql"

dbid = "dmzdb"
dbtype = "postgres"

# dbna = db_creds[dbid]["db_name"]
# dbus = db_creds[dbid]["db_user"]
# dbpa = db_creds[dbid]["db_pass"]
# dbpo = db_creds[dbid]["db_port"]
# #
# # print (dbna, dbus, dbpa, dbpo)
#
# dbname = utils.decrypt_token(dbna)
# dbuser = utils.decrypt_token(dbus)
# dbpass = utils.decrypt_token(dbpa)
# dbport = utils.decrypt_token(dbpo)
#
# print (dbname)
# print (dbuser)
# print (dbpass)
# print (dbport)

(cursor, connection) = utils.db_connect(dbid, dbtype)

create_sql = """
create table lm (
name    varchar(20)
)
;
"""

cursor.execute(create_sql)
connection.commit()