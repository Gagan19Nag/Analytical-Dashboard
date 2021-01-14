import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="nitk", host="127.1.1.1", port="5432")
cur = conn.cursor()

cur.execute("SELECT username, role, password  from user_credentials")
rows = cur.fetchall()
print(rows)

print("Operation Completed");
