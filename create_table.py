import csv
import sqlite3
connection = sqlite3.connect("werke.db")
pointer = connection.cursor()

sql_order = """
CREATE TABLE IF NOT EXISTS werke (
Abbildung BLOB,
KünstlerIn,
Bezeichnung,
Titel,
Jahr,
Material,
Größe,
Sammlung,
Kommentar,
Literatur
);"""
pointer.execute(sql_order)

pointer.execute("DELETE FROM werke")
connection.commit()

sql_order = """
INSERT INTO werke (Abbildung, KünstlerIn, Bezeichnung, Titel, Jahr, Material, Größe, Sammlung, Kommentar, Literatur)
VALUES (:Abbildung, :KünstlerIn, :Bezeichnung, :Titel, :Jahr, :Material, :Größe, :Sammlung, :Kommentar, :Literatur)
"""

with open("/home/nx/Downloads/exelliste.csv") as csvfile:
	csv_reader_object = csv.reader(csvfile, delimiter=';')
	with sqlite3.connect("werke.db") as connection:
		pointer = connection.cursor()
		pointer.executemany(sql_order, csv_reader_object)

pointer.execute("SELECT * FROM werke")
content = pointer.fetchall()
print(content)

connection.commit()
connection.close()
