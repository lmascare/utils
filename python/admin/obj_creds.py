#!/usr/local/bin/python3

from lank import obj_utils
from lank.lank_cfg import db_creds

"""
mykey = obj_utils.creds()
k = "/tmp/lm1"
auth_key = mykey.create_key()
"""

"""Single cred encrypt / decrypt"""
cred = "lank4me"

mycred = obj_utils.Creds(keyfile="lm")
# print(type(mycred))
e_cred = mycred.encrypt_cred(cred)

print("Encrypted Cred  --> {}".format(e_cred))

# my_token = "gAAAAABchCDyqA_xZElEtdQZjVA4g5DjRor-zYLz2VQ5H3Cx4brLOZH4ncnRJAwL9\
# L8ci-JHgZp0OvzkMwM2-DQYayafOb_QQA=="
my_token = e_cred
my_cred = mycred.decrypt_token(my_token)

print("Decrypted Token --> {}".format(my_cred))
# """

"""Multiple creds encrypt / decrypt"""
# dbname = "lankinc"
# dbuser = "lankinc"
# dbpass = "lankinc"
# dbhost = "localhost"
# dbport = "5432"

mycreds = obj_utils.Creds()
# print(mycreds)
# (db_name, db_user, db_pass, db_host, db_port) = mycreds.encrypt_creds(
    # dbname, dbuser, dbpass, dbhost, dbport)

# print("DB Name --> {}".format(db_name))
# print("DB User --> {}".format(db_user))
# print("DB Pass --> {}".format(db_pass))
# print("DB Host --> {}".format(db_host))
# print("DB Port --> {}".format(db_port))

# (de_name, de_user, de_pass, de_host, de_port) = mycreds.decrypt_tokens(
    # db_name, db_user, db_pass, db_host, db_port)

# print("DBNAME --> {}\n"
      # "DBUSER --> {}\n"
      # "DBPASS --> {}\n"
      # "DBHOST --> {}\n"
      # "DBPORT --> {}".format(de_name, de_user, de_pass, de_host, de_port))
# """

dbid = "lankinc"
dli_name = db_creds[dbid]["db_name"]
dli_user = db_creds[dbid]["db_user"]
dli_pass = db_creds[dbid]["db_pass"]
dli_host = db_creds[dbid]["db_host"]
dli_port = db_creds[dbid]["db_port"]

(dl_name, dl_user, dl_pass, dl_host, dl_port) = mycreds.decrypt_tokens(
    dli_name, dli_user, dli_pass, dli_host, dli_port)

print("DBID   --> {}\n"
      "DBNAME --> {}\n"
      "DBUSER --> {}\n"
      "DBPASS --> {}\n"
      "DBHOST --> {}\n"
      "DBPORT --> {}".format(dbid, dl_name, dl_user, dl_pass, dl_host, dl_port))
