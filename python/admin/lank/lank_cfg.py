"""
Variables to be used across the board everywhere.

Variables available are
    General purpose
        - logdir
        - adm_bin, adm_cfg,  adm_data
        - adm_etc, adm_keys, adm_logs
        - adm_tmp

    Permissions
        - shared group (wheel) & mode 750 for cfg, data, etc, keys
        - Mode 1777 for tmp, logs
        - Files created in etc, keys should have mode 640 and root:wheel

    For MySQL
        - dbname, dbuser, dbpass, dbport,
"""
import os
import sys

""" General Purpose """
adm_home = '/u/admin'
adm_bin = adm_home + '/bin'
adm_cfg = adm_home + '/cfg'
adm_data = adm_home + '/data'
adm_etc = adm_home + '/etc'
adm_keys = adm_home + '/keys'
adm_logs = adm_home + '/logs'
adm_tmp = adm_home + '/tmp'

logdir = adm_logs

keyfile = adm_keys + '/keyfile'
key_file = adm_keys + "/key_file"

host = os.uname()[1]

scriptname = os.path.basename(sys.argv[0])

smtp_server = 'gAAAAABaRnjQLl5_SHGQZOsI-NLA5aRwMsLIhs2y1_QlMuy1tXkhtIzhEVklYJ1A1lN7bjS0Qf4V0sPJlR_xZZFpZK7mqN0fbQ=='
smtp_port = 'gAAAAABaRnk-OlKdVvdVddkPEo76iKqyHKYv530XmgLF_38_2jZjlkYPxL20wWVZBPxtCoYBUUL4sxlzoq4EPVQQos6aPIsojg=='
smtp_user = 'gAAAAABaRner9zdw5UhBqJpvLIPuQnsF2rbB9I1ZGT6Xw4MfgMhePzoS7_8LH8mtzwukNQqkayTHJUp_A3tq9xCiDHo8nn51eyIEFQk0MRcSYF-jbBfJCp0='
smtp_passwd = 'gAAAAABaRncp-P5SkWyKz9P9ddUxtB38uoenTMRQa-dJlch3CWHDX6bLpW_89QYcndJDwfVmz2XLGjsc1U5DEknjlqdmC73QpQ=='

""" Used for the MySQL DB """
dbname = 'gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j61vvzAiDWKyv\
LYOAlkomZ6NXayxVmU3XLi-ZfleZaQ=='
dbuser = 'gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j61vvzAiDWKyv\
LYOAlkomZ6NXayxVmU3XLi-ZfleZaQ=='
dbpass = 'gAAAAABZ6-gp2LRJGy6PUolC5lUNd_OimzJChjJDthVVCZXSDvclKLx_6QSZZ-8SJ9ra\
UErXg5M2P7vmCKGc63T0uMr8J04C6A=='
dbport = 'gAAAAABZ6-hyadloTFpJyIY9H6Ki4cikqab9GRP9EmjqXk--I6Nz3rd9mqDb_RPpzBaO\
RVq1_XDzrKOlXozOq7n90Gsuukegbw=='


# DB Credentials for several databases in Python DICT format

db_creds = {
    "stock": {
        "db_name": "gAAAAABZ7KLVM0iwLz2RXncIEWUKUFO4mRsxsKfX_l5beQzSy2a1q-4kuQ\
xM62R-AGgtmUs588GJTOplpvZSj57Nfot68EIwKw==",
        "db_user": "gAAAAABZ7KLVM0iwLz2RXncIEWUKUFO4mRsxsKfX_l5beQzSy2a1q-4kuQ\
xM62R-AGgtmUs588GJTOplpvZSj57Nfot68EIwKw==",
        "db_pass": "gAAAAABZ7KLVM0iwLz2RXncIEWUKUFO4mRsxsKfX_l5beQzSy2a1q-4kuQ\
xM62R-AGgtmUs588GJTOplpvZSj57Nfot68EIwKw==",
        "db_port": "gAAAAABZ6-hyadloTFpJyIY9H6Ki4cikqab9GRP9EmjqXk--I6Nz3rd9mq\
Db_RPpzBaORVq1_XDzrKOlXozOq7n90Gsuukegbw=="
    },
    "lifecycle": {
        "db_name": "gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j61\
vvzAiDWKyvLYOAlkomZ6NXayxVmU3XLi-ZfleZaQ==",
        "db_user": "gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j61\
vvzAiDWKyvLYOAlkomZ6NXayxVmU3XLi-ZfleZaQ==",
        "db_pass": "gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j61\
vvzAiDWKyvLYOAlkomZ6NXayxVmU3XLi-ZfleZaQ==",
        "db_port": "gAAAAABZ6-hyadloTFpJyIY9H6Ki4cikqab9GRP9EmjqXk--I6Nz3rd9mq\
Db_RPpzBaORVq1_XDzrKOlXozOq7n90Gsuukegbw=="
    },
    "dmzdb": {
        "db_name": "gAAAAABcV1tIN02hM6Ncdmig5Wi7_IgtgYVPqowYi_zpCb1zZS0yqehsp\
Ci-HooAR-5Nf0uWC71SYJPuVLRhs1MlXApvXTi54g==",
        "db_user": "gAAAAABcV1tIrYidvtXvqLpUwzdxsoouIWVHrs78wjG_Imf3_Unv651rA\
KzQ77ipr51CtGdpwxa88iOisAk7PG_WdX4NYyo2KA==",
        "db_pass": "gAAAAABcV1tIfJn2agR2Siq4kt9QG_BQaC6ZSj4rscE0GzKr2m7p9JQB8\
TEqRW9LXIJbg7C4khNbkYjqUJDOCyFDHtmwYqvb6w==",
        "db_port": "gAAAAABcV1tIHRR9s_Qy5zsUcQl0zdPWdUNWqX50fbskmqoIQwPC2rlT9\
7-oGP0ZsIlBpKonSJdx1IkOO8bA_CAXAkQI-DTuyg=="
    },
    "lankinc": {
            "db_name": "gAAAAABdeuYBYt4NLdETOqd14nD72EZ6eTdnwBN9lN1IKjltS8ppp"
                       "OilkrYSo56yTnYe3e7vUfn0PwuMZbu_VGdcOyb49c5HWw==",
            "db_user": "gAAAAABdeuYBmv1xDnI3SpUkbIdA1nVom-Fg3WEfzQ5e79pBrozhL"
                       "-C0IvkeyyTqFt9IRPz_FIWxh-I8Iv_nkUUnDuVgfvPtVg==",
            "db_pass": "gAAAAABdeuYB9ZGz4AVxvrGZWx9kt5hijWeOj5yf1NuSwve5l4ae3"
                       "W4IT7v2qtHWzgAJ__E3ULnHAUlg6Om4LHxplYSuOotBww==",
            "db_host": "gAAAAABdeuYBxLk8ILDkW3qeZbOj7Ua-GpsSOdcS8sk301lu9-dHn"
                       "Ahttn_GyeQZPwbEhlqWUXq8Y8j2ur2ha9jIgl-bjcs_cA==",
            "db_port": "gAAAAABdeuYBRymQMctazkIogKVGwRCJ8FFru-M8Q1xqd6PTyHI4j"
                       "XFXhGCBC8I82gup9gLWIj5zGJgMjn-tVoDzL9oCNWxPGA=="
        }
}
