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
    import utils
    # import signal

    #from vars import dbname, dbuser, dbpass, dbport
    from vars import db_creds
    utils.init()

    dbnames = db_creds.keys()
    # print(dbnames)

    for dbname in dbnames:
        # print dbname

        dbuser = db_creds[dbname]['db_user']
        print(dbuser)

        dbpass = db_creds[dbname]['db_pass']
        print(dbpass)

        dbport = db_creds[dbname]['db_port']
        print(dbport)

    # (db_name, db_user, db_pass, db_port) = utils.get_creds(dbname, dbuser, dbpass, dbport)
    #print("DBNAME = {} DBUSER = {} DBPASS = {} DBPORT = {}".format(db_name, db_user, db_pass, db_port))

    #utils.hello()
    #utils.logit("hello","critical")
    #utils.logit("hello","error")
    #utils.logit("hello","warning")
    #utils.logit("hello","info")

    ##utils.logit("info", "hello", 1)
    ##utils.timeout(1)
    ##signal.pause()
    
    #utils.runcmd('ps -eaf')
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
