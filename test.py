import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ramya@2004",
    database="college"
)

df = pd.read_sql("SELECT * FROM students", conn)

print(df)