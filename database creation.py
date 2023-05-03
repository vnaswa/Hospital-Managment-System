import mysql.connector as sql
conn = sql.connect(host='localhost', user='root', passwd='vaibhav#123')
cur=conn.cursor()
if conn.is_connected:
    cur.execute("create database hospital_management_system")
    print("Database created succefully")
