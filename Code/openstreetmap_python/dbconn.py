#!/usr/bin/python3
import psycopg2
import argparse
from config import config

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", help="run test", action="store_true")

def main():
    args = parser.parse_args()
    
    if args.test:
        connect()
    else:
        print("Hello world!")

def connect():
    conn = None
    try:
        # read connection parameters from ini file
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execure a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    
    # if err!=nil;
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    finally: 
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        

if __name__ == "__main__":
    main()
