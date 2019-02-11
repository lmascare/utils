"""Schema definition for TLS data."""


def table_nmap_history(*args):
    """SQL to create, insert, update, delete table nmap_history"""
    create_sql = """
    CREATE TABLE IF NOT EXISTS nmap_history (
    scanner_name        varchar(16) NOT NULL,
    command_line        varchar(128) NOT NULL,
    scanner_script      varchar(128),
    scanner_version     varchar(32),
    scan_type           varchar(32) NOT NULL,
    scan_protocol       varchar(8) NOT NULL,
    scan_services       varchar(32),
    nmap_start          timestamp,
    nmap_end            timestamp,
    elapsed_time        numeric(10,2),
    scan_start          timestamp,
    scan_end            timestamp,
    verbosity           integer,
    debug_level         integer,
    host_state          varchar(8),
    ip_address          varchar(64),
    hostname            varchar(64),
    fqdn                varchar(128),
    status              varchar(64),
    test_start          timestamp,
    test_end            timestamp,
    port_protocol       varchar(8) NOT NULL,
    port_id             integer,
    port_state          varchar(16),
    port_service        varchar(16),
    test_summary        varchar(128),
    testid              bigint,
    id                  bigserial PRIMARY KEY
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


def table_tls_ciphers_history(*args):
    """SQL to table tls_ciphers_history."""
    create_sql = """
    CREATE TABLE IF NOT EXISTS tls_ciphers_history (
    protocol            varchar(16),
    compressors         varchar(16),
    cipher_pref         varchar(16),
    least_strength      varchar(8),
    checksum            varchar(128),
    testid              bigint,
    id                  bigserial PRIMARY KEY
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


tls_tables = {
    "nmap_history": table_nmap_history,
    "tls_ciphers_history": table_tls_ciphers_history,
}

if __name__ == "__main__":
    printeger("Script tls_schema.py must be called as a module only")
    exit(1)
