"""Use Object Oriented Programming for functions."""
import sys
import os
import logging

from .lank_cfg import logdir, keyfile, adm_tmp, db_creds
# import subprocess
# import shlex

"""
This module contains Classes
 - LogMe (logging in OO)
 - Creds (Encrypt / Decrypt / Create keyfile)
"""

"""
ToDo
 - dbconnect
    - Inputs are dbid & dbtype
    - Returns cursor, connection
 - runcmd
 - dbconnect
 - Export DB rows into CSV file
 - Import CSV files into DB

 - sendmail
 - signal handler
    - timeout
    - graceful exit

Completed
 - Creds
    - Encrypt, Decrypt, Create key
 - LogMe
    - The 'init' function now correctly handles creating the logfile. The
      class is initialized once in the code which runs the init function.
 - dns_query
"""


class DnsQuery:
    """DNS Queries.

    This class provides forward, reverse, PTR records
    """

    # DNS module will be used across this class.
    from dns import resolver, reversename

    def __init__(self, ip_address=None, hostname=None):
        r"""Initialize the class.

        The DnsQuery class provides functionality to receive either a
        hostname or an IP Address and returns a tuple of the remaining
        attributes.

        Output format : (hostname, ip_address, ptr, fqdn)
        --------------------------------------------------
        | Input      | Output                            |
        --------------------------------------------------
        | Hostname   | (hostname, ip_address, ptr, fqdn) |
        | IP Address | (hostname, ip_address, ptr, fqdn) |
        --------------------------------------------------

        Separately, you can get several Resource Records independently like:
        cname
        name server
        mx record
        SOA
        Ref : https://stackoverflow.com/questions/13842116/\
              how-do-we-get-txt-cname-and-soa-records-from-dnspython
        """
        self.dns_rec = ()
        self.ip_address = ip_address
        self.hostname = hostname
        self.host_ptr = None
        self.host_cname = None
        self.host_fqdn = None

    def get_host_ip(self):
        r"""Receive the Hostame. Return IP Address."""
        if self.ip_address is None and self.hostname is not None:
            self.host_ip = str(self.resolver.query(self.hostname, "A")[0])
        elif self.ip_address is not None:
            self.host_ip = self.ip_address
        return self.host_ip

    def get_ptr(self):
        r"""Receive the IP Address. Return PTR Record."""
        # if self.ip_address is None:
        #     self.ip_address = self.get_host_ip()
        self.host_ptr = str(self.reversename.from_address(self.ip_address))
        return self.host_ptr

    def get_fqdn(self):
        r"""Receive the PTR. Return FQDN."""
        if self.host_ptr is None:
            self.host_ptr = self.get_ptr()
        self.host_fqdn = str(self.resolver.query(self.host_ptr, "PTR")[0])
        return self.host_fqdn

    def get_hostname(self):
        r"""Receive the IP, get the hostname."""
        if self.host_fqdn is None:
            self.host_fqdn = self.get_fqdn()
        self.hostname = self.host_fqdn.split('.')[0]
        return self.hostname

    def get_cname(self):
        r"""Get CNAME for a host.

        Be friendly. If hostname is provided, use it first, if not, use
        the IP address to get the hostname. Then the CNAME
        """
        # if self.hostname is None:
        #     self.hostname = self.get_hostname()
        try:
            self.host_cname = str(self.resolver.query(
                self.hostname, "CNAME")[0])
        except Exception as e:
            return ("{}".format(e))
        # return self.host_cname

    def get_dns_rec(self):
        r"""Return a tuple of the DNS Record."""
        self.ip_address = self.get_host_ip()
        self.hostname = self.get_hostname()
        self.host_ptr = self.get_ptr()
        self.host_fqdn = self.get_fqdn()
        self.host_cname = self.get_cname()

        self.dns_rec = (self.hostname, self.ip_address, self.host_ptr,
                        self.host_fqdn, self.host_cname)
        return (self.dns_rec)


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
        self.writelog(20, "*** Started " + self.scriptname + " ***", 0)
        # Best practice is to remove the return statement from init
        # return (None)

    def critical(self, message, verbosity):
        """Level: Critical messages."""
        self.plevel = 50
        self.message = message
        self.verbosity = verbosity
        self.writelog(self.plevel, self.message, self.verbosity)

    def error(self, message, verbosity):
        """Level: ERROR messages."""
        self.plevel = 40
        self.message = message
        self.verbosity = verbosity
        self.writelog(self.plevel, self.message, self.verbosity)

    def warning(self, message, verbosity):
        """Level: WARNING messages."""
        self.plevel = 30
        self.message = message
        self.verbosity = verbosity
        self.writelog(self.plevel, self.message, self.verbosity)

    def info(self, message, verbosity):
        """Level: INFO messages."""
        self.plevel = 20
        self.message = message
        self.verbosity = verbosity
        self.writelog(self.plevel, self.message, self.verbosity)

    def debug(self, message, verbosity):
        """Level: DEBUG messages.

        This level will write to the logfile as well as STDOUT"""
        self.plevel = 10
        self.message = message
        self.verbosity = verbosity
        self.writelog(self.plevel, self.message, self.verbosity)

    def notset(self, message, verbosity):
        """Level: LEVEL NOT SET messages."""
        self.plevel = 0
        self.message = message
        self.verbosity = verbosity
        self.writelog(self.plevel, self.message, self.verbosity)

    def writelog(self, plevel, message, verbosity):
        """Write the message to logfile.

        This function performs the following steps
         - Defines the format for logging
         - Sets the logging level based on inputImportError: attempted relative import with no known parent package
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
        self.verbosity = verbosity
        logging.basicConfig(
            filename=self.logfile,
            level=logging.DEBUG,
            format='%(asctime)s:%(levelname)-8s:%(process)d:%(message)s',
            datefmt='%m-%d-%Y %H:%M:%S'
        )
        logging.log(self.plevel, self.message)

        if (self.plevel == 10) or (self.verbosity == 1):
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

# End class LogMe
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

    def __init__(self, keyfile=keyfile):
        """Initialize the class."""
        if os.path.exists(keyfile):
            self.authkey = open(keyfile, "r").read()
            self.f = self.Fernet(self.authkey)
        else:
            self.mylog = LogMe()
            self.mylog.info("Keyfile {} does not exit".format(keyfile), 0)
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
        if self.f is None:
            return ("No Keyfile")
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
        r"""Decrypt tokens to connect to a DB or RESTApi.

        It accepts the following encrypted tokens for decryption
        :param dbname:  - Database Name
        :param dbuser:  - Database Username
        :param dbpass:  - Database Password
        :param dbhost:  - Database Hostname
        :param dbport:  - Database Port

        :returns (dbname, dbuser, dbpass, dbhost, dbport):
        """
        if self.f is None:
            return ("No Keyfile")
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


class DBConnect:
    r"""Establish a connection to the DB of choice & RESTApi endpoint.

    This module will establish a cursor & connection to the following
    database types. If 'restapi' is specified, it will return the credentials
    needed to establish a connection.
    - mysql
    - postgresql
    - restapi
    """
    def __init__(self, dbid, dbtype, timeout=60):
        r"""Initialize the class."""
        self.dbid = dbid
        self.dbtype = dbtype
        self.timeout = timeout
        self.db_error = None
        if self.dbid not in db_creds:
            mylog = LogMe()
            self.db_error = "Invalid DBID --> {}".format(self.dbid)
            mylog.error(self.db_error, 0)
            self.cursor = None
            self.connection = None
        else:
            db_name = db_creds[self.dbid]["db_name"]
            db_user = db_creds[self.dbid]["db_user"]
            db_pass = db_creds[self.dbid]["db_pass"]
            db_host = db_creds[self.dbid]["db_host"]
            db_port = db_creds[self.dbid]["db_port"]

            dbcreds = Creds()
            (self.dbname, self.dbuser, self.dbpass, self.dbhost, self.dbport) \
                = dbcreds.decrypt_tokens(db_name, db_user, db_pass, db_host, db_port)

    def postgres(self):
        import psycopg2
        connection = psycopg2.connect(
            host=self.dbhost,
            port=int(self.dbport),
            user=self.dbuser,
            password=self.dbpass,
            dbname=self.dbname,
            connect_timeout=self.timeout
        )
        cursor = connection.cursor()
        return (cursor, connection)

    def mysql(self):
        import mysql.connector
        connection = mysql.connector.connect(
            host=self.dbhost,
            port=int(self.dbport),
            user=self.dbuser,
            password=self.dbpass,
            database=self.dbname,
            connect_timeout=self.timeout
        )
        cursor = connection.cursor()
        return (cursor, connection)

    def connect(self):
        r"""Establish a cursor and connection to the DB."""
        if (self.db_error is None):
            if (self.dbtype == "postgres"):
                (self.cursor, self.connection) = self.postgres()
            elif (self.dbtype == "mysql"):
                (self.cursor, self.connection) = self.mysql()

        return (self.cursor, self.connection)


# Get the diff / union of two lists.
class list_diff_union():
    r"""Return Difference or Union of lists.

    In this class, the two methods, diff_lists and union_lists provide
     - A difference of the left list against the right list. This means
     that elements of the left list are compared against the right list and
     those that are not present are returned.

     - A union of the left list against the right list. In this method, the
     elements of the left list are compared against the right list and only
     those that are match are returned.
     e.g.
     l1 = ['1', '2', 'b']
     r1 = ['3', '4', 'b', '1',]

    """
    def __init__(self, left_list, right_list):
        self.left_list = left_list
        self.right_list = right_list

    def diff_lists(self):
        r"""Get the difference of two lists.

        The elements in the left list is checked if they exist in the right
        list. We create a Python set of the right list to remove duplicates as
        well as speed up processing
        """
        self.set_right_list = set(self.right_list)
        self.list_diff = [x for x in self.left_list if x not in self.set_right_list]

        # list_union = [x for x in left_list if x in set_right_list]
        #return(list_diff, list_union)
        return(self.list_diff)

    def union_lists(self):
        r"""Get the union of two lists.

        The elements in the left list is checked if they exist in the right
        list. We create a Python set of the right list to remove duplicates as
        well as speed up processing
        """
        self.set_right_list = set(self.right_list)
        self.list_union = [x for x in self.left_list if x in self.set_right_list]

        # list_union = [x for x in left_list if x in set_right_list]
        # return(list_diff, list_union)
        return (self.list_union)


if __name__ == "__main__":
    print("Script can be called as a module only. Exiting...")
    exit(1)