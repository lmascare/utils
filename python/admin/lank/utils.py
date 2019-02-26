"""This Module contains commonly used utilities.

List of functions available in this module
 - logit         -- Complete
 - runcmd        -- Complete
 - sig_handler   -- Complete
 - timeout       -- Complete
 - db_creds      -- Complete
 - get_creds     -- Complete
 - create_key    -- Complete
 - encrypt_cred  -- Complete
"""

# ToDo
# create functions
#  - unlock_script
#  - lock_script
#  - should_i_exit
#  -
#
# in init(), keys functions
#   - add try: except to trap failures
#   - create the logfile if it doesn't exist. chmod 664
#
import logging
import sys
import os
import inspect

import subprocess
import shlex
import signal
from dns import resolver, reversename
from .vars import logdir, keyfile, key_file, dbname, dbuser, dbpass, dbport,\
    adm_tmp, smtp_user, smtp_passwd, smtp_server, smtp_port, db_creds, scriptname


def dns_queries(host_name):
    r"""DNS Query.

    This function will receive a hostname an returns a 'tuple' of
    (Host Name, IP Address, PTR Record, Original Hostname)
    https://www.adampalmer.me/iodigitalsec/2014/11/21/performing-dns-queries-python/
    :param host_name:
    :return: (host_name, host_ip, host_ptr, host_ori)
    """
    host_ip = str(resolver.query(host_name, "A")[0])
    # host_ip = str(host_ip[0])
    # print(host_ip, type(host_ip))
    host_ptr = str(reversename.from_address(host_ip))
    # print(host_ptr)
    # print("Hostname --> {} : IP --> {} : PTR --> {}".format(host_name, host_ip, host_ptr))
    fqdn = str(resolver.query(host_ptr, "PTR")[0])
    tuple_rec = (host_name, host_ip, host_ptr, fqdn)
    return(tuple_rec)


def encrypt_token(token):
    """Decrypt a token."""
    if (os.path.exists(key_file)):
        authkey = open(key_file, "rb").read()
    else:
        print("Key File '{}' does not exist".format(key_file))
        exit(1)
    from cryptography.fernet import Fernet

    # print (type(authkey))
    f = Fernet(authkey)

    # Ensure the supplied string is converted to bytes
    byte_token = str.encode(token)
    encrypted_token = (f.encrypt(byte_token)).decode()
    return (encrypted_token)


def encrypt_cred(cred):
    """
    Encrypt the supplied credential using the keyfile.

    This important function
    :param cred:
    :return encrypted_cred:
    """
    if os.path.exists(keyfile):
        authkey = open(keyfile, "r").read()

    from cryptography.fernet import Fernet
    f = Fernet(authkey)

    byte_cred = str.encode(cred)
    encrypted_cred = (f.encrypt(byte_cred)).decode()
    # print (encrypted_cred)
    return(encrypted_cred)


def encrypt_creds(dbname, dbuser, dbpass, dbport):
    """
    Encrypt the supplied credential using the keyfile.

    This important function
    :param dbname, dbuser, dbpass, dbport:
    :return encrypted(dbname, dbuser, dbpass, dbport):
    """
    if os.path.exists(keyfile):
        authkey = open(keyfile, "rb").read()
    else:
        print ("Keyfile '{}' does not exist".format(keyfile))
        exit(1)

    from cryptography.fernet import Fernet
    f = Fernet(authkey)

    byte_dbname = str.encode(dbname)
    byte_dbuser = str.encode(dbuser)
    byte_dbpass = str.encode(dbpass)
    byte_dbport = str.encode(dbport)

    encrypted_dbname = (f.encrypt(byte_dbname)).decode()
    encrypted_dbuser = (f.encrypt(byte_dbuser)).decode()
    encrypted_dbpass = (f.encrypt(byte_dbpass)).decode()
    encrypted_dbport = (f.encrypt(byte_dbport)).decode()

    return(encrypted_dbname, encrypted_dbuser, encrypted_dbpass, encrypted_dbport)


def decrypt_token(token):
    """Decrypt a token."""
    if (os.path.exists(key_file)):
        authkey = open(key_file, "rb").read()
    else:
        print ("Key File '{}' does not exist".format(key_file))
        exit(1)
    from cryptography.fernet import Fernet

    # print (type(authkey))
    f = Fernet(authkey)

    byte_token = str.encode(token)
    # Convert the bytestream back to string
    decrypted_token = (f.decrypt(byte_token)).decode()
    return (decrypted_token)


def decrypt_creds(dbname, dbuser, dbpass, dbport):
    """
    Decrypt DB creds.

    Default Creds in vars.py are decrypted and returned.
    :return db_name, db_user, db_pass, db_port:
    """
    if (os.path.exists(keyfile)):
        authkey = open(keyfile, 'rb').read()
        # print(authkey)
    else:
        print ("Key File '{}' does not exist".format(keyfile))
        exit(1)
    from cryptography.fernet import Fernet
    f = Fernet(authkey)

    byte_dbname = str.encode(dbname)
    byte_dbuser = str.encode(dbuser)
    byte_dbpass = str.encode(dbpass)
    byte_dbport = str.encode(dbport)

    db_name = (f.decrypt(byte_dbname)).decode()
    db_user = (f.decrypt(byte_dbuser)).decode()
    db_pass = (f.decrypt(byte_dbpass)).decode()
    db_port = (f.decrypt(byte_dbport)).decode()

    print("DBNAME = {} DBUSER = {} DBPASS = {} DBPORT = {}"
          .format(db_name, db_user, db_pass, db_port))

    return (db_name, db_user, db_pass, db_port)


def get_creds(dbname, dbuser, dbpass, dbport):
    """
    Decrypt creds.

    Creds are provided as arguments to this routine,
    decrypted and returned.
    :param dbname:
    :param dbuser:
    :param dbpass:
    :param dbport:
    :return db_name, db_user, db_pass, db_port:
    """
    if (os.path.exists(keyfile)):
        authkey = open(keyfile, 'rb').read()
        # print(authkey)
    else:
        print("Key File '{}' does not exist".format(keyfile))
        exit(1)

    from cryptography.fernet import Fernet
    f = Fernet(authkey)

    byte_dbname = str.encode(dbname)
    byte_dbuser = str.encode(dbuser)
    byte_dbpass = str.encode(dbpass)
    byte_dbport = str.encode(dbport)

    db_name = (f.decrypt(byte_dbname)).decode()
    db_user = (f.decrypt(byte_dbuser)).decode()
    db_pass = (f.decrypt(byte_dbpass)).decode()
    db_port = (f.decrypt(byte_dbport)).decode()
    # print("DBNAME = {} DBUSER = {} DBPASS = {} DBPORT = {}"\
    # .format(db_name, db_user, db_pass, db_port))
    return (db_name, db_user, db_pass, db_port)


def db_connect(dbid, dbtype):
    """Establish a connection to the DB.

    This connection accepts a DBID and DBTYPE. It then establishes a
    connection to the DB and returns a cursor & connection
    """
    if dbid not in db_creds.keys():
        logit("critical", "Unknown DBID --> {}".format(dbid), 0)

    dbna = db_creds[dbid]["db_name"]
    dbus = db_creds[dbid]["db_user"]
    dbpa = db_creds[dbid]["db_pass"]
    dbpo = db_creds[dbid]["db_port"]

    (dbname, dbuser, dbpass, dbport) = get_creds(dbna, dbus, dbpa, dbpo)
    if (dbtype == "mysql"):
        import pymysql
        conn = pymysql.connect(host='localhost',
                               port=int(dbport),
                               user=dbuser,
                               password=dbpass,
                               db=dbname,
                               local_infile=True
                              )
    elif (dbtype == "postgres"):
        import psycopg2
        conn = psycopg2.connect(host='localhost',
                              port=dbport,
                              user=dbuser,
                              password=dbpass,
                              dbname=dbname
                              )
    else:
        logit("critical", "Unknown DB Type --> {}".format(dbtype), 1)
    cur = conn.cursor()
    return (cur, conn)


def create_key():
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
    """
    tmp_keyfile = adm_tmp \
        + '/keyfile.' \
        + os.environ['USER'] \
        + '.' \
        + str(os.getpid())
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    # print(key, tmp_keyfile, os.environ, os.getgid())
    try:
        f = open(tmp_keyfile, "wb")
        f.write(key)
    except Exception as e:
        print ("Error Writing '{}'. Error --> {}".format(tmp_keyfile, e))
    f.close()

    os.chmod(tmp_keyfile, 0o400)
    os.chown(tmp_keyfile, os.getuid(), os.getgid())


def sig_handler(signal, frame):
    """
    Signal Handling.

    Receive signals and determine what to do with them. At this point, it
    exits with code 1

    :param signal
    :param frame # Need to research what frame is :)

    -SIGHUP signal. Similar to exit 1.
    -SIGINT signal. CTRL-C signal number 2.
    -SIGALRM signal. Alarm signal.
    -SIGTERM signal. Signal number 15.
    """
    logit("info", "Signal received -- {}".format(signal), 1)
    sys.exit(1)


signal.signal(signal.SIGHUP, sig_handler)
signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)
signal.signal(signal.SIGALRM, sig_handler)


def logit(level, message, verbosity):
    """Standardized logging.

      - This module derives the logfile name from the scriptname.
        It then appends this name to the logdir from function init()

      :param level
      :param message
      :param verbosity

      - Receives a message with a level and writes it to the to the logfile

      - Verbosity determines if output should write to log and screen
       - 1 -- Write to logfile and display to screen
         0 -- Write to logfile only

      - If it receives a level of 50 (critical), it will
       - Write to the logfile
       - Display the message on the screen
       - Exit

    Example of usage
       Ensure PYTHONPATH is set to the modules directory

       import utils
       utils.init()
       utils.logit("critical", "hello", 1)

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
        plevel = 50
    elif (level == "error"):
        plevel = 40
    elif (level == "warning"):
        plevel = 30
    elif (level == "info"):
        plevel = 20
    elif (level == "debug"):
        plevel = 10
    elif (level == "notset"):
        plevel = 0
    else:
        plevel = 50

    logging.basicConfig(filename=logfile, level=logging.DEBUG,
                        format='%(asctime)s:'
                               '%(levelname)s:'
                               '%(process)d:'
                               '%(filename)s:'
                               '%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S'
                        )
    logging.log(plevel, message)
    # print("From print : {} : {}".format(message,level))

    if ((plevel == 10) or (verbosity == 1)):
        print("{}".format(message))

    if (plevel == 50):
        print("{}".format(message))
        print("CRITICAL Level : Mandatory Exit...")
        # We ask sig_handler to handle the exit. the sys.exit(1) does not send
        # its signal. it has to be explicitly called.
        #
        sig_handler(1, 1)
        # sys.exit(1)

def init():
    """Init function.

    - Defines the log directory. Creates it if not present
    - Note that it explicitly calls os.chmod as os.mkdir with perms
      does not correctly set the permissions.
    """
    if not (os.path.isdir(logdir)):
        os.mkdir(logdir)
        os.chmod(logdir, 0o777)
    # else:
    #   print("{} exists".format(logdir))
    logit("info", "Started script '{}'".format(scriptname), 0)


def timeout(secs):
    """
    Ensure we timeout after n seconds.

    :param secs:

    This function allows us to run long queries, processes with the assurance
    that it will timeout in a given amount of time.
    We have defined - signal.signal(signal.SIGALRM, sig_handler) so after secs
    seconds, we will call sig_handler.

    Example. To run a command with a timeout of 10 seconds

    import utils
    utils.timeout(10)
    signal.pause()
    """
    logit("info", "Received request for timeout of {} seconds".format(secs), 0)
    signal.alarm(secs)


def runcmd(os_cmd):
    """Run OS commands.

    The purpose of this function is to have a standard way of
    calling OS commands. The STDIN, STDOUT and STDERR are correctly decoded
    We use shlex to split the command supplied into tokens for Popen.

    :param os_cmd
    :return: STDOUT
    :return: STDERR
    :return: Return Code

    Examples:
        utils.runcmd('ps -eaf')
        utils.runcmd('ifconfig -a')
    The commands are also logged.

    """
    args = shlex.split(os_cmd)
    # print(os_cmd, args)
    p = subprocess.Popen(args,
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE
                         )
    stdout, stderr = p.communicate()
    out = stdout.decode('utf-8')
    err = stdout.decode('utf-8')
    rc = p.returncode
    # print(out, err, rc)
    logit("info", "OS Command : {}".format(os_cmd), 0)
    return (out, err, rc)


def send_mail(recipient, subject, body, attachment):
    """Send email via gmail.com.

    Requires gmail credentials and TLS. It also sends attachments in correct
    MIME encoded format.

    If no attachment is sent, the attachment parameter should say NOFILE.

    Message body is always sent via HTML mail

    :param recipient:   # A Python list of recipients
    :param subject:
    :param body:        # Sent as plain text
    :param attachment:  # Module detects type of file and encodes accordingly
    :return:
    """
    import smtplib
    import mimetypes
    from email import encoders
    from email.message import Message
    from email.mime.audio import MIMEAudio
    from email.mime.base import MIMEBase
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Decrypt the smtp_user, smtp_passwd, smtp_server, smtp_port
    (gmuser, gmpasswd, gmserver, gmport) = get_creds(smtp_user, smtp_passwd, smtp_server, smtp_port)
    logit("info", "Sending Mail to {} with Subject {}".format(recipient, subject), 0)

    # Create the enclosing message
    TO = recipient if type(recipient) is list else [recipient]
    COMMASPACE = ","
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = gmuser
    msg['To'] = COMMASPACE.join(TO)
    msg.preamble = 'Mime Preamble'

    if (body is not ""):
        # plain_msg_body = MIMEText(body, 'plain')
        html_msg_body = MIMEText(body, 'html')
        # msg.attach(plain_msg_body)
        msg.attach(html_msg_body)
    else:
        logit("warning", "Sending with No Message Text", 0)

    if os.path.isfile(attachment):
        logit("info", "Processing {}".format(attachment), 0)
        ctype, encoding = mimetypes.guess_type(attachment)
        if ctype is None or encoding is not None:
            # Could not determine file type based on extension. So use the
            # generic encoding
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)
        if (maintype == "text"):
            logit("info", "Text Attachment", 0)
            fp = open(attachment)
            att = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif (maintype == "image"):
            logit("info", "Image Attachment", 0)
            fp = open(attachment, "rb")
            att = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif (maintype == "audio"):
            logit("info", "Audio Attachment", 0)
            fp = open(attachment, "rb")
            att = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            logit("info", "Generic Attachment", 0)
            fp = open(attachment, "rb")
            att = MIMEBase(maintype, subtype)
            att.set_payload(fp.read())
            fp.close()

            # Encode the payload using base64
            encoders.encode_base64(att)

        att.add_header("Content-Disposition", "attachment", filename="%s" % os.path.basename(attachment))
        msg.attach(att)

    elif (attachment == "NOFILE"):
        logit("info", "Attachment --> {}".format(attachment), 0)
    else:
        logit("critical", "Unknown type of Attachment --> {}".format(attachment), 0)

    # Initialize the connections
    s = smtplib.SMTP()
    s.set_debuglevel(0)
    s.connect(gmserver, gmport)
    s.ehlo()
    s.starttls()
    s.login(gmuser, gmpasswd)

    s.sendmail(gmuser, recipient, msg.as_string())
    s.close()


def get_filename():
    """Return the filename from the calling script."""
    # frame, filename, line_number, function_name, lines, index = \
    # inspect.stack()[1]
    frame, filename, blah = inspect.stack()[1]
    # print(frame,filename,line_number,function_name,lines,index)
    return filename
