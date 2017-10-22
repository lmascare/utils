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
    import signal

    utils.init()

    (db_name, db_user, db_pass, db_port) = utils.db_creds()
    print("DBNAME = {} DBUSER = {} DBPASS = {} DBPORT = {}".format(db_name, db_user, db_pass, db_port))

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
