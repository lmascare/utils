"""Use Object Oriented Programming for functions."""
import sys
import os
import logging

from .vars import dbname, dbuser, dbpass, dbport, logdir
# import subprocess
# import shlex

"""
This module contains Classes
 - logme (logging in OO)      -- Status completed
 - runcmd (run an OS command) -- Status not started
"""

"""
ToDo

 - Define a module which has only variables. Those should be imported here.
    -- Completed

    -- Completed.
 - Port runcmd.
 - Create a class to import CSV files.

Completed
    - logme
         - The 'init' function now correctly handles creating the logfile. The
           class is initialized once in the code which runs the init function.

"""


class logme:
    """Class logme.

    In this section we
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
       12-03-2016 22:54:12:CRITICAL:19790:<script_name>.log:Critical Error
    """

    def __init__(self):
        """Initialize the class."""
        global logfile
        scriptname = os.path.basename(sys.argv[0])
        logfile = logdir + "/" + scriptname + ".log"
        # print(logfile)
        if not (os.path.exists(logdir)):
            os.mkdir(logdir)
            os.chmod(logdir, 0o777)

        if not os.path.exists(logfile):
            os.mknod(logfile, 0o666)
            os.chmod(logfile, 0o666)

        # Since it is called from init. It will print to the logfile only
        # once when the class is initialized. The plevel=20 is 'info'
        self.writelog(20, "Started " + scriptname)
        # Best practice is to remove the return statement from init
        # return (None)

    def critical(self, message):
        """Level: Critical messages."""
        plevel = 50
        self.message = message
        self.writelog(plevel, message)

    def error(self, message):
        """Level: ERROR messages."""
        plevel = 40
        self.message = message
        self.writelog(plevel, message)

    def warning(self, message):
        """Level: WARNING messages."""
        plevel = 30
        self.message = message
        self.writelog(plevel, message)

    def info(self, message):
        """Level: INFO messages."""
        plevel = 20
        self.message = message
        self.writelog(plevel, message)

    def debug(self, message):
        """Level: DEBUG messages."""
        """This level will write to the logfile as well as STDOUT"""
        plevel = 10
        self.message = message
        self.writelog(plevel, message)

    def notset(self, message):
        """Level: LEVEL NOT SET messages."""
        plevel = 0
        self.message = message
        self.writelog(plevel, message)

    def writelog(self, plevel, message):
        """Write the message to logfile.

        This function performs the following steps
         - Defines the format for logging
         - Sets the logging level based on input
         - If LEVEL = Debug
                - print to STDOUT
         - If LEVEL = CRITICAL
                - print to STDOUT
                - Exit with status = 1
        """
        # filename = os.path.basename(sys.argv[0])
        # We need to log the source filename. Easiest way is to prepend
        # it to the message
        # 06/06/2017. We can prepend source filename as we cannot have a
        # string and dict/list object added
        # message = src_filename + ':' + message
        # print(filename)
        logging.basicConfig(
            filename=logfile,
            level=logging.DEBUG,
            format='%(asctime)s:%(levelname)-8s:%(process)d:%(message)s',
            datefmt='%m-%d-%Y %H:%M:%S'
        )
        logging.log(plevel, message)

        if (plevel == 10):
            print("{}".format(message))

        """
        Critical Mesages will
         -- Display to STDOUT
         -- Write to the logfile
         -- Exit with error code 1
        """
        if (plevel == 50):
            print("{}".format(message))
            print("CRITICAL Level : Mandatory Exit...")
            sys.exit(1)

# End class logme
#################
