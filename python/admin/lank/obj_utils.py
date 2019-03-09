"""Use Object Oriented Programming for functions."""
import sys
import os
import logging

from vars import logdir, keyfile, adm_tmp
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
    - Retuns cursor, connection
 - runcmd.
 - Create a class to import CSV files

Completed
 - creds
    - Encrypt, decrypt, create_key
 - logme
    - The 'init' function now correctly handles creating the logfile. The
      class is initialized once in the code which runs the init function.
"""


class creds:
    """Class creds. Encrypt, Decrypt Creds.

    This class provides the following functions
    encrypt_cred   - Encrypt a single credential
    decrypt_token  - Decrypt a single token
    encrypt_creds  - Encrypt creds to connect to a DB
    decrypt_tokens - Decrypt tokens to connect to a DB
    create_key     - Create a private key to use for encryption / decription
    """

    def __init__(self):
        """Initiaze the class.

        The key is essential to all functions. Ensure it is available.
        """
        if os.path.exists(keyfile):
            global authkey, f
            authkey = open(keyfile, "r").read()
            from cryptography.fernet import Fernet
            f = Fernet(authkey)
        else:
            mylog = logme()
            mylog.critical("AUTHKEY {} does not exit".format(authkey))

    def encrypt_cred(self, cred):
        """Encrypt a credential.

        :param  cred:  - Credential to be encrypted
        :return token: - Returns the encrypted token
        """
        # Ensure the supplied string is converted to bytes
        byte_token = str.encode(cred)
        encrypted_token = (f.encrypt(byte_token)).decode()
        return (encrypted_token)

    def decrypt_token(self, token):
        """Decrypt a token.

        :param  token: - Encrypted token to be decrypted
        :return cred:  - Returned the decrypted credential
        """
        byte_token = str.encode(token)
        # Convert the bytestream back to string
        decrypted_token = (f.decrypt(byte_token)).decode()
        return (decrypted_token)

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
        byte_dbname = str.encode(dbname)
        byte_dbuser = str.encode(dbuser)
        byte_dbpass = str.encode(dbpass)
        byte_dbhost = str.encode(dbhost)
        byte_dbport = str.encode(dbport)

        # Now encrypt these strings
        encrypted_dbname = (f.encrypt(byte_dbname)).decode()
        encrypted_dbuser = (f.encrypt(byte_dbuser)).decode()
        encrypted_dbpass = (f.encrypt(byte_dbpass)).decode()
        encrypted_dbhost = (f.encrypt(byte_dbhost)).decode()
        encrypted_dbport = (f.encrypt(byte_dbport)).decode()

        return (encrypted_dbname, encrypted_dbuser, encrypted_dbpass,
                encrypted_dbhost, encrypted_dbport)

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
        byte_dbname = str.encode(dbname)
        byte_dbuser = str.encode(dbuser)
        byte_dbpass = str.encode(dbpass)
        byte_dbhost = str.encode(dbhost)
        byte_dbport = str.encode(dbport)

        db_name = (f.decrypt(byte_dbname)).decode()
        db_user = (f.decrypt(byte_dbuser)).decode()
        db_pass = (f.decrypt(byte_dbpass)).decode()
        db_host = (f.decrypt(byte_dbhost)).decode()
        db_port = (f.decrypt(byte_dbport)).decode()

        return (db_name, db_user, db_pass, db_host, db_port)

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
        if tmp_keyfile is None:
            tmp_keyfile = adm_tmp \
                          + '/keyfile.' \
                          + os.environ['USER'] \
                          + '.' \
                          + str(os.getpid())
        from cryptography.fernet import Fernet
        key = Fernet.generate_key()
        try:
            f = open(tmp_keyfile, "wb")
            f.write(key)
            os.chmod(tmp_keyfile, 0o400)
            os.chown(tmp_keyfile, os.getuid(), os.getgid())
            print("Keyfile written to --> {}".format(tmp_keyfile))
        except Exception as e:
            print("Error Writing '{}'. Error --> {}".format(tmp_keyfile, e))
        f.close()


class logme:
    """Class logme. Provide logging functionality.

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
