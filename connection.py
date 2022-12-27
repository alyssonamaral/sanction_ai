import psycopg2
import sys

param_dic = {
    "host"      : "localhost",
    "database"  : "postgres",
    "user"      : "postgres",
    "password"  : "D1o3a0397!"
}

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    return conn


def single_insert(conn, insert_req):
    """ Execute a single INSERT request """
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

def insertDf(df_base, table_name, df_base_cols):
    
    df_base_cols_list = ', '.join(df_base_cols)

    # Connecting to the database
    conn = connect(param_dic)
    # Inserting each row
    for i in df_base.index:
        tableColumnsValues = []
        tableColumnsValues.append(df_base.values[i].tolist())   
        tableColumnsValues = ', '.join(map(str, tableColumnsValues[i]))   #NEED TO TAKE THE DATE IN STRING
        print(tableColumnsValues)
  
        query = f'INSERT into {table_name} ({df_base_cols_list}) values({tableColumnsValues});'
     
        single_insert(conn, query)
    # Close the connection
    conn.close
