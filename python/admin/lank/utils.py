""" This Module contains commonly used utilities.

List of functions available in this module
 - logit  -- Complete
 - runcmd -- Complete
"""

import logging
import sys
import os
import inspect

import subprocess
import shlex
from vars import logdir

def init():
    """ Init function

    - Defines the log directory. Creates it if not present
    - Note that it explicitly calls os.chmod as os.mkdir with perms
      does not correctly set the permissions.
    """
    global logdir
    global scriptname

    #logdir = '/u/tmp'
    if not (os.path.isdir(logdir)):
        os.mkdir(logdir)
        os.chmod(logdir,0o777)
    #else:
    #   print("{} exists".format(logdir))


def logit(message,level):
    """Function logit

      - This module derives the logfile name from the scriptname,
        It then appends this name to the logdir from function init()
      - Receives a message with a level and writes it to the to the logfile
      - If it receives a level of 50 (critical), it will display the message
        on the screen and exit.

    Example of usage
       from lank import utils
       utils.init()
       utils.logit("hello","critical")

       This will write "hello" to the logfile as follows and exit
       <-- time stamp  -->:<Level> :<PID>:<script>:<message>
       12-03-2016 22:54:12:CRITICAL:19790:utils.py:hello
    """

    scriptname = os.path.basename(sys.argv[0])
    logfile = logdir + '/' + scriptname + '.log'

    '''
    Here's where my main logging functionality is set.
    I prefer to send the level as a word, but the logging.log function requires 
    an integer. I don't want users to pass numbers for level. I'll generate it. 
    I spent too much time searching how to do this.
   '''

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
    # print("From print : {} : {}".format(message,level))

    if(plevel == 10):
        print("{}".format(message))

    if (plevel == 50):
        print("{}".format(message))
        print("CRITICAL Level : Mandatory Exit...")
        sys.exit(1)


def runcmd(os_cmd):
    """ Function runcmd

    The purpose of this function is to have a standard way of
    calling OS commands. The STDIN, STDOUT and STDERR are correctly decoded
    We use shlex to split the command supplied into tokens for Popen

    Examples:
        utils.runcmd('ps -eaf')
        utils.runcmd('ifconfig -a')
    """

    args = shlex.split(os_cmd)
    # print(os_cmd, args)
    p = subprocess.Popen(args,
                         stdout = subprocess.PIPE,
                         stdin  = subprocess.PIPE,
                         stderr = subprocess.PIPE
                         )
    stdout,stderr = p.communicate()
    out = stdout.decode('utf-8')
    err = stdout.decode('utf-8')
    print(out,err)


def get_filename():
    """ Function that returns the filename from the calling script """

    frame,filename,line_number,function_name,lines,index = inspect.stack()[1]
    #print(frame,filename,line_number,function_name,lines,index)
    return filename
