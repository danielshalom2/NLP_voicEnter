# data acqusition module 
import pandas as pd 
from init import *
import sqlite3
from sqlite3 import Error
from datetime import datetime
from icecream import ic as ic2


def time_format():
    return f'{datetime.now()}  data acq|> '

ic2.configureOutput(prefix=time_format)



def create_connection(db_file=db_name):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        pp = ('Conected to version: '+ sqlite3.version)
        ic2(pp)
        return conn
    except Error as e:
        ic2(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        ic2(e)


def init_db(database):
    # database = r"data\homedata.db"    
    tables = [
    """ CREATE TABLE IF NOT EXISTS `users` (
	`ID`	TEXT NOT NULL,
	`name`	TEXT NOT NULL,
	`phone`	TEXT NOT NULL
    );"""   
    ]
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create tables
        for table in tables:
            create_table(conn, table)
        conn.close()            
    else:
        ic2("Error! cannot create the database connection.")



def timestamp():
    return str(datetime.fromtimestamp(datetime.timestamp(datetime.now()))).split('.')[0]
    

        
def add_user_data(ID, name, phone):
    """
    Add new USER into the data table
    :param conn:
    :param :
    :return: last row id
    """
    sql = ''' INSERT INTO users(ID, name, phone)
              VALUES(?,?,?) '''
    conn = create_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute(sql, [ID, name, phone])
        conn.commit()
        re = cur.lastrowid
        conn.close()
        return re
    else:
        ic2("Error! cannot create the database connection.")                
     

def fetch_table_data_into_df(table_name, conn, filter):
    return pd.read_sql_query("SELECT * from " + table_name +" WHERE `name` LIKE "+ "'"+ filter+"'", conn)

def fetch_data(database,table_name, filter):

    TABLE_NAME = table_name
    # create a database connection
    conn = create_connection(database)
    with conn:
        
        return fetch_table_data_into_df(TABLE_NAME, conn,filter)
        
       


if __name__ == '__main__':
    if db_init:
        init_db(db_name)
        add_user_data('1','john smith', '123')
