import mysql.connector

conn = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

cursor = conn.cursor()

def execute_query(query):
    cursor.execute(query)
    data = cursor.fetchall()
    conn.commit()
    return data
