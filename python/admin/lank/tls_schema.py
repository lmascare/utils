"""Schema definition for TLS data."""

from lank import utils

def tls_host_profile():
    """SQL to create, insert, update, delete table."""
    create_sql = """
    CREATE TABLE tls_host_profile (
    scanner_type        varchar(16) NOT NULL,
    command_line        varchar(128) NOT NULL,
    scan_type           varchar(32) NOT NULL,
    scan_protocol       varchar(8) NOT NULL,
    scan_service        int(8),
    scan_start          datetime,
    scan_end            datetime,
    host_state          varchar(8),
    scan_reason         varchar(64),
    ip_address          varchar(64),
    hostname            varchar(64),
    fqdn                varchar(128),
    )
    ;
    """

    insert_sql = """

    """

    update_sql = """
    
    """

    delete_sql = """
    
    """

    return (create_sql, insert_sql, update_sql, delete_sql)

if __name__ == "__main__":
    print ("tls_schema.py must be called as a module only")
    exit(1)