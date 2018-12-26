import sqlite3
connection = sqlite3.connect("super.db")
cursor = connection.cursor()

sql_command = """CREATE TABLE object ( rfid varchar(20) unique not null, objid integer not null, objname varchar(10) not null, price integer not null);"""
cursor.execute(sql_command)

sql_command = """INSERT INTO object (rfid, objid, objname, price) VALUES ("02000FF6D72C", 101, "Chocolate", 100);""" cursor.execute(sql_command)

sql_command = """INSERT INTO object (rfid, objid, objname, price) VALUES ("19004AC80E95", 102, "Face wash", 150);"""
cursor.execute(sql_command)

sql_command = """INSERT INTO object (rfid, objid, objname, price) VALUES ("19004AC4D84F", 101, "Chocolate", 100);""" cursor.execute(sql_command)

connection.commit()
connection.close()