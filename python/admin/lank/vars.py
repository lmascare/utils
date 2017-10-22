
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

""" General Purpose """
adm_home = '/u/admin'
adm_bin = adm_home + '/bin'
adm_cfg = adm_home + '/cfg'
adm_data = adm_home + '/data'
adm_etc = adm_home + '/etc'
adm_keys = adm_home + '/keys'
adm_logs = adm_home + '/logs'
adm_tmp = adm_home + '/tmp'

keyfile = adm_keys + '/keyfile'

logdir = adm_logs

""" Used for the MySQL DB """
dbuser = 'gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j61vvzAiDWKyv\
LYOAlkomZ6NXayxVmU3XLi-ZfleZaQ=='
dbname = 'gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j61vvzAiDWKyv\
LYOAlkomZ6NXayxVmU3XLi-ZfleZaQ=='
dbpass = 'gAAAAABZ6-gp2LRJGy6PUolC5lUNd_OimzJChjJDthVVCZXSDvclKLx_6QSZZ-8SJ9ra\
UErXg5M2P7vmCKGc63T0uMr8J04C6A=='
dbport = 'gAAAAABZ6-hyadloTFpJyIY9H6Ki4cikqab9GRP9EmjqXk--I6Nz3rd9mqDb_RPpzBaO\
RVq1_XDzrKOlXozOq7n90Gsuukegbw=='


# dbname = 'lifecycle'
# dbuser = 'lifecycle'
# dbpass = 'waterloo'
# dbport = 3306
