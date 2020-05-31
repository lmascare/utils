r"""Schema file to host status of MySQL Database backups."""

def table_db_brman_status(*args):
    r"""DDL for Database Backups Status."""
    create_sql = """
    CREATE TABLE IF NOT EXISTS db_brman_status (
    dbname          varchar(16),
    type            varchar(8),
    filename        varchar(128),
    filesize        bigint,
    action          varchar(16),
    status          varchar(16),
    bkup_start      timestamp,
    bkup_end        timestamp,
    id              bigint auto_increment,
    PRIMARY KEY (id)
    );
    CREATE INDEX brman_status_bkup_date on db_brman_status(bkup_date);
    CREATE INDEX brman_status_type on db_brman_status(type);
    """

    insert_sql = None
    update_sql = None
    delete_sql = None
    select_sql = None

    return (create_sql, insert_sql, update_sql, delete_sql, select_sql)

backup_tables = {
    "db_brman_status": table_db_brman_status,
}


if __name__ == "__main__":
    from lank_cfg import scriptname
    from obj_utils import LogMe
    mylog = LogMe()
    mylog.critical("{} Should be run as a module only".format(scriptname), 0)