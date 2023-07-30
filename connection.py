import psycopg2
import psycopg2.extras as extras
import sys

param_dic = {
    "host"      : "ofac-db.cbgdt0gpf0f7.us-east-2.rds.amazonaws.com",
    "database"  : "ofac_db",
    "user"      : "alyssonamaral",
    "password"  : "8yXuk!wRbt3f8W"
}

def connect(params_dic):
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    return conn


def single_insert(conn, insert_req): 
    cursor = conn.cursor()
    try:
        cursor.execute(insert_req)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()

def insertDf(df_base, table_name):
    conn = connect(param_dic)
    tuples = [tuple(x) for x in df_base.to_numpy()] 
    cols = ','.join(list(df_base.columns))    
    query = "INSERT INTO %s(%s) VALUES %%s" % (table_name, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("The dataframe is inserted")
    cursor.close()
