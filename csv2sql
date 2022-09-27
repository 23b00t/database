import csv
import sqlite3
connection = sqlite3.connect("adress.db")
pointer = connection.cursor()

sql_order = """
CREATE TABLE IF NOT EXISTS adress (
name VARCHAR(30),
surname VARCHAR(20),
birthday DATE
);"""
pointer.execute(sql_order)

pointer.execute("DELETE FROM adress")
connection.commit()

sql_order = """
INSERT INTO adress (name, surname, birthday)
VALUES (:nachname, :vorname, :geburtstag)
"""

with open("/home/nx/Documents/tt.csv") as csvfile:
	csv_reader_object = csv.reader(csvfile, delimiter=';')
	with sqlite3.connect("adress.db") as connection:
		pointer = connection.cursor()
		pointer.executemany(sql_order, csv_reader_object)

pointer.execute("SELECT * FROM adress")
content = pointer.fetchall()
print(content)

connection.commit()
connection.close()
