import sqlite3

connection = sqlite3.connect("werke.db")
pointer = connection.cursor()
pointer.execute("SELECT * FROM werke")
content = pointer.fetchall()

#pointer.execute("DELETE FROM vwerke")
#connection.commit()
pointer.execute("CREATE VIRTUAL TABLE IF NOT EXISTS temp.vwerke USING FTS5(Abbildung, KünstlerIn, Bezeichnung, Titel, Jahr, Material, Größe, Sammlung, Kommentar, Literatur)")
pointer.executemany("INSERT INTO vwerke VALUES (?,?,?,?,?,?,?,?,?,?)", content)
pointer.execute("SELECT * FROM vwerke WHERE vwerke MATCH 'Basaldella'")
con = pointer.fetchall()
print(con)
connection.close()
