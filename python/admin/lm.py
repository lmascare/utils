#!/usr/bin/python
#
# Utils is always imported first
#

def main():
    #import lank.utils
    # print (logfile)'
    #lank.utils.logit("hello",1,"crit")
    
    #from lank import utils

    # We set the PYTHONPATH so that we don't have to specify the modules dir.
    # Alternatively, we can set it in the main program as follows
    # sys.path.append('/u/gitwork/utils/python/admin/lank')
    from lank import utils
    # import signal

    #from vars import dbname, dbuser, dbpass, dbport
    from lank.vars import db_creds
    utils.init()
    # utils.create_key()
    # crd = utils.encrypt_cred('587')
    # print(crd)
    # exit(0)
    # from lank.vars import smtp_user, smtp_passwd, smtp_server, smtp_port
    # (gmus, gmpa, gmse, gmpo) = utils.get_creds(smtp_user, smtp_passwd, smtp_server, smtp_port)
    # print(gmus, gmpa, gmse, gmpo)
    # exit(0)

    recipient = ['larry.masc@gmail.com', 'larry_mario@yahoo.com']
    # recipient = 'larry_mario@yahoo.com'
    # recipient = 'larry.masc@gmail.com'
    subject = 'Test from Python'
    body = 'Test 5 to GMail and Yahoo with Mimetext and Multipart with file'
    # attachment = "NOFILE"
    attachment = "/home/lmascare/misc/earthmoon_nasa.jpg"
    # attachment = "/home/lmascare/misc/KEYS.gz"

    utils.send_mail(recipient, subject, body, attachment)

    exit(0)
    dbnames = db_creds.keys()
    print(dbnames)

    for dbcred in dbnames:
        print dbcred

        dbname = db_creds[dbcred]['db_name']
        print(dbname)

        dbuser = db_creds[dbcred]['db_user']
        print(dbuser)

        dbpass = db_creds[dbcred]['db_pass']
        print(dbpass)

        dbport = db_creds[dbcred]['db_port']
        print(dbport)

        (db_name, db_user, db_pass, db_port) = utils.get_creds(dbname, dbuser, dbpass, dbport)
        print("DBNAME = {} DBUSER = {} DBPASS = {} DBPORT = {}".format(db_name, db_user, db_pass, db_port))

    #utils.hello()
    #utils.logit("hello","critical")
    #utils.logit("hello","error")
    #utils.logit("hello","warning")
    #utils.logit("hello","info")

    ##utils.logit("info", "hello", 1)
    ##utils.timeout(1)
    ##signal.pause()
    
    utils.runcmd('ps -eaf')
    #utils.runcmd('ifconfig -a')

    # OO Programming

    # we set PYTHONPATH env variable
    #import sys
    #sys.path.append('/u/gitwork/utils/python/admin/lank')

    #import obj_utils

    #mylog = obj_utils.logme()
    #mylog.critical('Critical Message')
    #mylog.error('Error Message')
    #mylog.warning('Warning Message')
    #mylog.debug('DEBUG Message')
    #mylog.info('INFO Message')

if __name__ == "__main__":
    main()
