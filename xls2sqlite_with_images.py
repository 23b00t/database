import pandas as pd
import openpyxl
import sqlite3

file_name = '/home/nx/Downloads/liste.xlsx'
sheet_name='Sheet1'

df = pd.read_excel(file_name, sheet_name=sheet_name, dtype=object)

wb = openpyxl.load_workbook(file_name)
ws = wb[sheet_name]
for img in ws._images:
    img.ref.seek(0)
    df.iat[img.anchor.to.row-1, img.anchor.to.col] = img.ref.read()

# export to sqlite
with sqlite3.connect(file_name + ".db") as con:
    df.to_sql(sheet_name, con=con)
