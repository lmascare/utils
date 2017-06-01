#!/usr/bin/python
#

from obj_utils import dbname, dbpass, dbuser, dbport

import pymysql


'''
Open a connection to the DB
'''
def db_connect(dbname,dbuser,dbpass,dbport):
    conn = pymysql.connect(host='localhost',
                           port=dbport,
                           user=dbuser,
                           passwd=dbpass,
                           db=dbname,
                           local_infile=True
                          )
    cur = conn.cursor()
    return (cur, conn)

'''
Create a Table
'''
def create_table(cur, conn):
    sql = """
    CREATE TABLE host_info (
        hostname    varchar(128) primary key,
        hostgroup   varchar(128) not null
                          )   
    """
    cur.execute(sql)
    cur.close()
    conn.close()

'''
BULK Loading
'''
def bulk_load(cur, conn, loader_file):
    print(loader_file)
    sql = """
    load data local infile '""" + loader_file + """' into table host_info 
    fields terminated by ','
    ignore 1 lines
    """
    # print(sql)
    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()


'''
Run DB query
'''
def db_query(cur, conn):
    sql = 'select * from hostinfo'
    cur.execute(sql)

    print(cur.description)
    print()

    for row in cur:
        print(row)

    cur.close()
    conn.close()

'''
The start of it all
'''
def main():
    (conn_cursor, conn) = db_connect(dbname, dbuser, dbpass, dbport)
    #db_query(conn_cursor, conn)
    #create_table(conn_cursor, conn)

    loader_file = '/home/lmascare/misc/mysql/host.csv'

    bulk_load(conn_cursor, conn, loader_file)

# Where we run it all
if __name__ == "__main__":
    main()

