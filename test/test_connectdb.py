import os
import psycopg2

HOST = os.environ.get('DB_HOST', False)
PORT = os.environ.get('DB_PORT', False)
DBNAME = os.environ.get('DB_NAME', False)
USER = os.environ.get('DB_USER', False)
PASSWORD = os.environ.get('DB_PASSWORD', False)


conn = psycopg2.connect(
    host=HOST,
    port=PORT,
    dbname=DBNAME,
    user=USER,
    password=PASSWORD
)


if __name__=='__main__':
    cur = conn.cursor()
    cur.execute("SELECT version();")
    print(cur.fetchone())
    print("Connection successful")
    conn.close()
    print("Connection closed")
