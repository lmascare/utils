"""Use Object Oriented Programming for functions."""
import sys
import os
import logging

from lank.vars import logdir, keyfile, adm_tmp
# import subprocess
# import shlex

"""
This module contains Classes
 - logme (logging in OO)      -- Status completed
 - runcmd (run an OS command) -- Status not started
"""

"""
ToDo
 - dbconnect
    - Inputs are dbid & dbtype
    - Returns cursor, connection
 - runcmd.
 - Create a class to import CSV files

Completed
 - creds
    - Encrypt, decrypt, create_key
 - logme
    - The 'init' function now correctly handles creating the logfile. The
      class is initialized once in the code which runs the init function.
"""


class LogMe:
    """Class LogMe. Provide logging functionality.

    This class provide logging functionality at various levels. Table below
    indicates how it will handle various levels
    ---------------------------------------------------------
    | Level     | Write to logfile | Write to STDOUT | Exit |
    |--------------------------------------------------------
    | critical  |     x            |      x          |  x   |
    | error     |     x            |      -          |  -   |
    | warning   |     x            |      -          |  -   |
    | info      |     x            |      -          |  -   |
    | debug     |     x            |      x          |  -   |
    ---------------------------------------------------------
    Definitions
        logdir  - Defined in global configuration file
        scriptname = os.path.basename(sys.argv[0])
        logfile = logdir + "/" + scriptname + ".log"

    Example of usage
    test.py
       import obj_utils
       mylog = obj_utils.LogMe()
       mylog.critical('Critical Error')

       logfile = "/u/admin/logs/test.py.log"
       This will write "Critical Error" to the logfile as follows
       <-- time stamp  -->:<Level> :<PID>:  <script>  :<message>
       12-03-2016 22:54:12:CRITICAL:19790:<script_name>.log:Critical Error
    """

    def __init__(self):
        """Initialize the class.

        In this section we
          - define the directory for global logging,
          - create the directory
          - create the file
          - ensure both are world writable

        """
        self.scriptname = os.path.basename(sys.argv[0])
        self.logfile = logdir + "/" + self.scriptname + ".log"
        # print(logfile)
        if not (os.path.exists(logdir)):
            os.mkdir(logdir)
            os.chmod(logdir, 0o777)

        if not os.path.exists(self.logfile):
            os.mknod(self.logfile, 0o666)
            os.chmod(self.logfile, 0o666)

        # Since it is called from init. It will print to the logfile only
        # once when the class is initialized. The plevel=20 is 'info'
        self.writelog(20, "*** Started " + self.scriptname + " ***")
        # Best practice is to remove the return statement from init
        # return (None)

    def critical(self, message):
        """Level: Critical messages."""
        self.plevel = 50
        self.message = message
        self.writelog(self.plevel, self.message)

    def error(self, message):
        """Level: ERROR messages."""
        self.plevel = 40
        self.message = message
        self.writelog(self.plevel, self.message)

    def warning(self, message):
        """Level: WARNING messages."""
        self.plevel = 30
        self.message = message
        self.writelog(self.plevel, self.message)

    def info(self, message):
        """Level: INFO messages."""
        self.plevel = 20
        self.message = message
        self.writelog(self.plevel, self.message)

    def debug(self, message):
        """Level: DEBUG messages."""
        """This level will write to the logfile as well as STDOUT"""
        self.plevel = 10
        self.message = message
        self.writelog(self.plevel, self.message)

    def notset(self, message):
        """Level: LEVEL NOT SET messages."""
        self.plevel = 0
        self.message = message
        self.writelog(self.plevel, self.message)

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
        self.plevel = plevel
        self.message = message
        logging.basicConfig(
            filename=self.logfile,
            level=logging.DEBUG,
            format='%(asctime)s:%(levelname)-8s:%(process)d:%(message)s',
            datefmt='%m-%d-%Y %H:%M:%S'
        )
        logging.log(self.plevel, self.message)

        if (self.plevel == 10):
            print("{}".format(self.message))

        """
        Critical Mesages will
         -- Display to STDOUT
         -- Write to the logfile
         -- Exit with error code 1
        """
        if (self.plevel == 50):
            print("{}".format(self.message))
            print("CRITICAL Level : Mandatory Exit...")
            sys.exit(1)

# End class logme
#################


class Creds:
    """Class creds. Encrypt, Decrypt Creds.

    This class provides the following functions
    encrypt_cred   - Encrypt a single credential
    decrypt_token  - Decrypt a single token
    encrypt_creds  - Encrypt creds to connect to a DB
    decrypt_tokens - Decrypt tokens to connect to a DB
    create_key     - Create a private key to use for encryption / description
    """

    from cryptography.fernet import Fernet

    def __init__(self):
        """Initialize the class."""
        if os.path.exists(keyfile):
            self.authkey = open(keyfile, "r").read()
            self.f = self.Fernet(self.authkey)
        else:
            self.mylog = logme()
            self.mylog.info("Keyfile {} does not exit".format(keyfile))
            self.authkey = None
            self.f = None

    def encrypt_cred(self, cred):
        """Encrypt a credential.

        :param  cred:  - Credential to be encrypted
        :return token: - Returns the encrypted token
        """
        if self.f is None:
            return ("No Keyfile")
        # Ensure the supplied string is converted to bytes
        self.cred = cred
        self.byte_token = str.encode(self.cred)
        self.encrypted_token = (self.f.encrypt(self.byte_token)).decode()
        return (self.encrypted_token)

    def decrypt_token(self, token):
        """Decrypt a token.

        :param  token: - Encrypted token to be decrypted
        :return cred:  - Returned the decrypted credential
        """
        if self.f is None:
            return ('No Keyfile')
        self.token = token
        self.byte_token = str.encode(self.token)
        # Convert the bytestream back to string
        self.decrypted_token = (self.f.decrypt(self.byte_token)).decode()
        return (self.decrypted_token)

    def encrypt_creds(self, dbname, dbuser, dbpass, dbhost, dbport):
        """Encrypt credentials to connect to a DB or RESTApi.

        It accepts the following parameters for encryption
        :param dbname:  - Database Name
        :param dbuser:  - Database Username
        :param dbpass:  - Database Password
        :param dbhost:  - Database Hostname
        :param dbport:  - Database Port

        :returns (dbname, dbuser, dbpass, dbhost, dbport):
        """
        # Ensure the supplied string is converted to bytes
        self.dbname = dbname
        self.dbuser = dbuser
        self.dbpass = dbpass
        self.dbhost = dbhost
        self.dbport = dbport
        self.byte_dbname = str.encode(self.dbname)
        self.byte_dbuser = str.encode(self.dbuser)
        self.byte_dbpass = str.encode(self.dbpass)
        self.byte_dbhost = str.encode(self.dbhost)
        self.byte_dbport = str.encode(self.dbport)

        # Now encrypt these strings
        self.encrypted_dbname = (self.f.encrypt(self.byte_dbname)).decode()
        self.encrypted_dbuser = (self.f.encrypt(self.byte_dbuser)).decode()
        self.encrypted_dbpass = (self.f.encrypt(self.byte_dbpass)).decode()
        self.encrypted_dbhost = (self.f.encrypt(self.byte_dbhost)).decode()
        self.encrypted_dbport = (self.f.encrypt(self.byte_dbport)).decode()

        return (self.encrypted_dbname, self.encrypted_dbuser,
                self.encrypted_dbpass, self.encrypted_dbhost,
                self.encrypted_dbport)

    def decrypt_tokens(self, dbname, dbuser, dbpass, dbhost, dbport):
        """Decrypts tokens to connect to a DB or RESTApi.

        It accepts the following encrypted tokens for decryption
        :param dbname:  - Database Name
        :param dbuser:  - Database Username
        :param dbpass:  - Database Password
        :param dbhost:  - Database Hostname
        :param dbport:  - Database Port

        :returns (dbname, dbuser, dbpass, dbhost, dbport):
        """
        self.dbname = dbname
        self.dbuser = dbuser
        self.dbpass = dbpass
        self.dbhost = dbhost
        self.dbport = dbport
        self.byte_dbname = str.encode(self.dbname)
        self.byte_dbuser = str.encode(self.dbuser)
        self.byte_dbpass = str.encode(self.dbpass)
        self.byte_dbhost = str.encode(self.dbhost)
        self.byte_dbport = str.encode(self.dbport)

        self.db_name = (self.f.decrypt(self.byte_dbname)).decode()
        self.db_user = (self.f.decrypt(self.byte_dbuser)).decode()
        self.db_pass = (self.f.decrypt(self.byte_dbpass)).decode()
        self.db_host = (self.f.decrypt(self.byte_dbhost)).decode()
        self.db_port = (self.f.decrypt(self.byte_dbport)).decode()

        return (self.db_name, self.db_user, self.db_pass, self.db_host,
                self.db_port)

    def create_key(self, tmp_keyfile=None):
        """
        Create cryptographic key for signing.

        This function will create a keyfile and stash in the adm_tmp directory
        File format : keyfile.username.pid
        It will set owner to the current owner and only he can read the file.

        This key should then be copied to the adm_keys dir with appropriate
        permissions. See your Systems Administrator for those details.

        *** IMPORTANT ***
        This key is used to encrypt all the credentials. Keep it safe. Loss of
        this key will require you to regenerate all credentials.
        :param  tmp_keyfile: - optional
        :return output_file: - Default location is
                               /u/admin/tmp/keyfile.<username>.<pid>
                               PERMS 0400
        """
        self.tmp_keyfile = tmp_keyfile
        if self.tmp_keyfile is None:
            self.tmp_keyfile = adm_tmp \
                               + '/keyfile.' \
                               + os.environ['USER'] \
                               + '.' \
                               + str(os.getpid())
        self.key = self.Fernet.generate_key()
        try:
            self.f = open(self.tmp_keyfile, "wb")
            self.f.write(self.key)
            os.chmod(self.tmp_keyfile, 0o400)
            os.chown(self.tmp_keyfile, os.getuid(), os.getgid())
            self.f.close()
            print("Keyfile written to --> {}".format(self.tmp_keyfile))
        except Exception as e:
            print("Error Writing '{}'. Error --> {}".
                  format(self.tmp_keyfile, e))
