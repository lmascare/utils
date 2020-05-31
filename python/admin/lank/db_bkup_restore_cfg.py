r"""Configuration file for Database Backups Status."""

from .lank_cfg import scriptname, adm_bkup, adm_restore
from . import obj_utils

brman_db = "brman"
mysql_db = "mysqldb"
dir_perms = "0o40777"

mysql = "/usr/bin/mysql"
mysqladmin = "/usr/bin/mysqladmin"
mysqlbinlog = "/usr/bin/mysqlbinlog"
mysqldump = "/usr/bin/mysqldump"

defaults_file = ".my.cnf"
check_files = [mysql, mysqldump, mysqlbinlog, mysqladmin]

connect_sql = """select curdate();"""

verify_sql = """show binary logs;"""
secure_sql = """select @@secure_file_priv;"""
logbin_index_sql = """select @@log_bin_index;"""

full_bkup_cmd = mysqldump + """ \
    --defaults-file={} \
    --single-transaction \
    --flush-logs \
    --delete-master-logs \
    --master-data=2 \
    --fields-terminated-by=, \
    --fields-enclosed-by='"' \
    --lines-terminated-by=0x0d0a \
    --tab={} \
    {} \
    > {}
"""

incr_bkup_cmd = mysqladmin + """ \
    --defaults-file={} \
    flush_logs
"""

dbs = {
    "mysqldb": {
        "dbid": "mysql",
        "dbtype": "mysql",
        "backup_dir": adm_bkup + "/mysql",
        "restore_dir": adm_restore + "/mysql",
    },
    "brman": {
        "dbid": "brman",
        "dbtype": "mysql",
        "backup_dir": adm_bkup + "/brman",
        "restore_dir": adm_restore + "/brman",
    },
    "lifecycle": {
        "dbid": "lifecycle",
        "dbtype": "mysql",
        "backup_dir": adm_bkup + "/lifecycle",
        "restore_dir": adm_restore + "/lifecycle",
    },
    "lankinc": {
        "dbid": "lankinc",
        "dbtype": "postgres",
        "backup_dir": adm_bkup + "/lankinc",
        "restore_dir": adm_restore + "/lankinc",
    },
}


if __name__ == "__main__":
    mylog = obj_utils.LogMe()
    mylog.critical("{} Should be run as a module only".format(scriptname), 0)