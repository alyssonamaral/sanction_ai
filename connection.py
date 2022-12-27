import psycopg2

# Connect to your PostgreSQL database on a remote server
conn = psycopg2.connect(host="localhost", port="5432", dbname="postgres", user="postgres", password="D1o3a0397!")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a test query
cur.execute("select * from publish_information;")

# Retrieve query results
records = cur.fetchall()

# Finally, you may print the output to the console or use it anyway you like
print(records)

conn.close()
