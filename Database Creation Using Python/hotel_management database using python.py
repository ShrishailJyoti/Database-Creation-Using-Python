# Create database and table
import mysql.connector as sql

db_connection = sql.connect(host="localhost", user="root", password="")
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE DATABASE IF NOT EXISTS hotel_management")
print("database created successfully")

db_connection.database = 'hotel_management'

db_cursor.execute("""CREATE TABLE IF NOT EXISTS emp(room_info VARCHAR(4), customer_info varchar(20), booking_info VARCHAR(15))""")
print('Table created successfully')

db_cursor.execute("show databases")
for x in db_cursor:
    print(x)

db_cursor.execute("SHOW TABLES")
for x in db_cursor:
    print(x)

db_cursor.close()
db_connection.close()
