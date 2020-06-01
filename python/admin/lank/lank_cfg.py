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
adm_bkup = adm_home + '/bkup'
adm_restore = adm_home + '/restore'

logdir = adm_logs

keyfile = adm_keys + '/keyfile'
# key_file = adm_keys + "/key_file"

host = os.uname()[1]

scriptname = os.path.basename(sys.argv[0])

maintainers = ["larry.masc@gmail.com"]

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
        "db_name": "",
        "db_user": "",
        "db_pass": "",
        "db_host": "",
        "db_port": "",
        'db_desc': ""
    },
    "mysql": {
        "db_name": "gAAAAABe0yB3ppZK15Zd38mkwpt3v26VGnUVlZ14FYAoy3uYLOpQNP9a-"
                   "1PZM_x-9zrbAidBwQxTk2j_mXzTUk2wtS-0lzO3pQ==",
        "db_user": "gAAAAABe0yB3scy6dCV7TmoKcATR-CAwVSnPGCFJiuKPHupQr9kSW4Uhf"
                   "oSIyyln8L9PTmaFR_Zxq_F4JbFK1ecfEoGdr1Ay9w==",
        "db_pass": "gAAAAABe0yB31m1zRQIS31ZVicD3LTNNISxEWljSHqD4rvYE8CphiBslD"
                   "GmOmGbMI5lvpipj2gdc7pe4k2f-4Eu2mYTa5hwpTA==",
        "db_host": "gAAAAABe0yB3zS5doTGwlqEQPDwiysvFn82WV0FkpC8ABoSxxkyb_mVhx"
                   "LXfBu1IVLvp077s9r4d65U-g1jU1HvT30BdAGZYBA==",
        "db_port": "gAAAAABe0yB3vWopPNUDllwmlI3mpPCmgAJ6BiT0KOZFpsPWNwJ-NLJCv"
                   "dgC-Vsr0YxH2h3S_KZu83azzOdCVZUejAZpcVYJWg==",
        'db_desc': "Superuser"
    },
    "brman": {
        "db_name": "gAAAAABe0xJrs18vmdArkoO77aJhv0weBrfWZTo7y2cvIgoChFMjKZLir"
                   "AFF65dGjcjaed-_iaoKt_4FPdkAWghpcYldq-cMGg==",
        "db_user": "gAAAAABe0xJrm__TbiOmcesNxmUSEroXsj0nI-L3uiGR7MQ71x1hmDM0u"
                   "VHAotiiYuUwnr1HXQuR98hGM9MhQI16e2tq40rWCQ==",
        "db_pass": "gAAAAABe0xJrhJkae86XMu7EUv0FhsSCpjA3eyOvecoLoAe6GXzEnlFaG"
                   "iKOtidS9_fbZ9rpkR_gua-ZRT6kZcPvUqyqPpCztQ==",
        "db_host": "gAAAAABe0xJrz3G0C_MJ0oWh1sUKigvwzFColOhzE6aM3yjUeE7mksBJk"
                   "m5DkedxWbh36A5Yua8-LjyB7eortzFkZPfgs9kvLQ==",
        "db_port": "gAAAAABe0xMHWxBf0r1iU1JkbyZwrQxP_RobLAQCj2fmnSd6dwOqhGmup"
                   "JydEqsn-_MNUc8_1q9pR84SI6Sa6bhMDtWyKD-1Gg==",
        'db_desc': "Backup and Restore Database (MySQL)"
    },
    "lifecycle": {
        "db_name": "gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j6"
                   "1vvzAiDWKyvLYOAlkomZ6NXayxVmU3XLi-ZfleZaQ==",
        "db_user": "gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j6"
                   "1vvzAiDWKyvLYOAlkomZ6NXayxVmU3XLi-ZfleZaQ==",
        "db_pass": "gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j6"
                   "1vvzAiDWKyvLYOAlkomZ6NXayxVmU3XLi-ZfleZaQ==",
        "db_host": "gAAAAABe0xJrz3G0C_MJ0oWh1sUKigvwzFColOhzE6aM3yjUeE7mksBJk"
                   "m5DkedxWbh36A5Yua8-LjyB7eortzFkZPfgs9kvLQ==",
        "db_port": "gAAAAABZ6-hyadloTFpJyIY9H6Ki4cikqab9GRP9EmjqXk--I6Nz3rd9m"
                   "qDb_RPpzBaORVq1_XDzrKOlXozOq7n90Gsuukegbw==",
        "db_desc": "The lifecycle Database (MySQL)"
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
                   "XFXhGCBC8I82gup9gLWIj5zGJgMjn-tVoDzL9oCNWxPGA==",
        'db_desc': "The lankinc Databse (PostgreSQL)"
    }
}
