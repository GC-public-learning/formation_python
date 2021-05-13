#coding:utf-8

""" database
------------------

1. install sqlite3

2. in this project the db file with its content is already created because i have 
already done the manips. if you want to restart without db file you can erase
the file "db1.sqlite" and recreate it with these instructions. otherwise skip the
following instructions :

	- open sqlite3 in the folder in which you want to create de db file

		command lines
		-----------------
		.save dbname -> to make a file with the db
		.open dbname -> to open the db
		.read namescriptsql -> make the tables (create.sql)
		.read namescriptsql -> add records (insert.sql) (optional)

"""

import sqlite3

connection = sqlite3.connect("db/db1.sqlite")
cursor = connection.cursor()


""" select
------------------------"""
login_player1 = ("user1",) # tuple !


# secure request
cursor.execute("SELECT * FROM players WHERE login = ?", login_player1)

# get a list with all rows selected for 1 record
print(cursor.fetchone()) # 

# get a specific row from 1 record
cursor.execute("SELECT * FROM players WHERE login = ?", login_player1)
rows = cursor.fetchone()

print(rows[0])
print(rows[1])
print(rows[2])
print(rows[3])

# get many records (get a list of list)
cursor.execute("SELECT * FROM players")
records = cursor.fetchall()

# handle each record and element
for rec in records:
	for row in rec:
		print(row, end =' ')
	print()


""" insert
------------------------"""
new_user = ("max", "passmax", 1000)

#cursor.execute("""INSERT INTO players (login, passwd, score) 
	#VALUES (?,?,?)""",new_user)

# save
#connection.commit()

# return before the last commit
connection.rollback()



""" CONVENTIONAL WAY !! 
-------------------------"""
try:
	connection2 = sqlite3.connect("db/db1.sqlite")
	cursor2 = connection2.cursor()

	cursor2.execute("SELECT * FROM players")

	records2 = cursor2.fetchall()

	for rec in records2:
		for row in rec:
			print(row, end =' ')
		print()

except Exception as e:
	print("Error : ", e)

finally:
	connection2.close()







