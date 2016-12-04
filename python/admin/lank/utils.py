'''
This Module contains commonly used utilities. It allows standardization

List of functions available in this module
 - logit
 - runcmd
 -
'''

import logging
import sys
import os

def init():
    global logdir
    global scriptname

    logdir = '/u/tmp'
    if not (os.path.isdir(logdir)):
        # We explicitly call os.chmod as os.mkdir with perms does not
        # work reliably
        os.mkdir(logdir)
        os.chmod(logdir,0o777)
    #else:
    #   print("{} exists".format(logdir))


'''
What I would like to do is 
have another module that displays to stdout 
whenver module debugit is called
'''

''' 
Function logit
  - This module derives the logfile name from the scriptname,
    It then appends this name to the logdir from function init()

  - Receives a message with a level and writes it to the to the logfile

Example of usage
   from lank import utils
   utils.init()
   utils.logit("hello","critical")

   This will write "hello" to the logfile as follows
   <-- time stamp  -->:<Level> :<PID>:<script>:<message>
   12-03-2016 22:54:12:CRITICAL:19790:utils.py:hello

'''

def logit(message,level):
    scriptname = os.path.basename(sys.argv[0])
    logfile = logdir + '/' + scriptname + '.log'

    # OLD style formatting
    #print ("Logfile is %s/%s" % (logdir, logfile) )

    # NEW style formatting
    # print ("Logfile is {}/{}".format(logdir, logfile) )

    # Here's where my main logging functionality is set
    # Have to do this as the logging.log function requires 
    # an integer. I don't want users to pass numbers for
    # level. I'll generate it. I spent too much time searching 
    # how to do this
    #
    if (level == "critical"):
        plevel=50
    elif (level == "error"):
        plevel=40
    elif (level == "warning"):
        plevel=30
    elif (level == "info"):
        plevel=20
    elif (level == "debug"):
        plevel=10
    elif (level == "notset"):
        plevel=0
    else:
        plevel=50

    logging.basicConfig(filename=logfile, level=logging.DEBUG,
            format='%(asctime)s:%(levelname)-8s:%(process)d:%(filename)s:%(message)s',
                        datefmt='%m-%d-%Y %H:%M:%S'
                        )
    logging.log(plevel,message)
    #print("From print : {} : {}".format(message,level))
