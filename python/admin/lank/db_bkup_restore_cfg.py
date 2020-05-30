r"""Configuration file for Database Backups Status."""

from .lank_cfg import scriptname, adm_bkup, adm_restore
from . import obj_utils

brman_db = "brman"
dir_perms = "0o40777"

dbs = {
    "brman": {
        "dbid": "brman",
        "dbtype": "mysql",
        "backup_dir": adm_bkup + "/brman/",
        "restore_dir": adm_restore + "/brman/",
    },
    "lifecycle": {
        "dbid": "lifecycle",
        "dbtype": "mysql",
        "backup_dir": adm_bkup + "/lifecycle/",
        "restore_dir": adm_restore + "/lifecycle/",
    },
    "lankinc": {
        "dbid": "lankinc",
        "dbtype": "postgres",
        "backup_dir": adm_bkup + "/lankinc/",
        "restore_dir": adm_restore + "/lankinc/",
    },
}


if __name__ == "__main__":
    mylog = obj_utils.LogMe()
    mylog.critical("{} Should be run as a module only".format(scriptname), 0)