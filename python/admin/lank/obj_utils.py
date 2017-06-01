'''
This module contains Classes
 - logme (logging in OO) -- Status completed
 - runcmd (run an OS command) -- Status not started
'''

# Will be used by logme
import sys
import os
import logging

# Will be used by runcmd
import subprocess
import shlex

'''
Variables used everywhere
'''

dbname = 'lifecycle'
dbuser = 'lifecycle'
dbpass = 'waterloo'
dbport = 3306

'''
Class logme

In the init section we 
 - define the directory for global logging,
 - create the directory
 - create the file
 - ensure both are world writable

 Example of usage
   import obj_utils
      mylog = obj_utils.logme()
      mylog.critical('Critical Error')

   This will write "Critical Error" to the logfile as follows
   <-- time stamp  -->:<Level> :<PID>:  <script>  :<message>
   12-03-2016 22:54:12:CRITICAL:19790:lm.py:Critical Error

Status
  - Completed 
'''

class logme:

    logdir = '/u/logs'
    global logfile
    logfile = logdir + '/lank.log'
    if not (os.path.exists(logdir)):
        os.mkdir(logdir)
        os.chmod(logdir,0o777)
        os.open(logfile,'w',0o777)
        os.close(logfile)

    def __init__(self,):
    #    print(logfile)
        pass

    def critical(self,message):
        plevel=50
        self.message = message
        self.writelog(plevel,message)

    def error(self,message):
        plevel = 40
        self.message = message
        self.writelog(plevel, message)

    def warning(self,message):
        plevel = 30
        self.message = message
        self.writelog(plevel, message)

    def info(self,message):
        plevel = 20
        self.message = message
        self.writelog(plevel, message)

    def debug(self,message):
        plevel = 10
        self.message = message
        self.writelog(plevel, message)

    def notset(self,message):
        plevel = 0
        self.message = message
        self.writelog(plevel, message)

    def writelog(self,plevel,message):
        src_filename = os.path.basename(sys.argv[0])
        # We need to log the source filename. Easiest way is to prepend it to the message
        message = src_filename + ':' + message
        #print(message)
        logging.basicConfig(filename=logfile, level=logging.DEBUG,
                     #format='%(asctime)s:%(levelname)-8s:%(process)d:%(filename)s:%(message)s',
                     format='%(asctime)s:%(levelname)-8s:%(process)d:%(message)s',
                     datefmt='%m-%d-%Y %H:%M:%S'
                     )
        logging.log(plevel, message)

# Tests
#mylog = logme()
#critlog = mylog.critical('This is a critical test')
#mylog.critical('This is a critical test')
#errlog = mylog.error('This is an error test')

# End class logme
#################













