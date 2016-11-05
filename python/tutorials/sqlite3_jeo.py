#!/usr/bin/python3

import sqlite3

connection = sqlite3.connect("jeo.db")
cursor = connection.cursor()

cursor.execute("select name from category limit 10")
results = cursor.fetchall()

print("Example categories: \n")

for category in results:
  print(category[0])

connection.close()
