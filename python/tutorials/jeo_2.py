#!/usr/bin/python3

import sqlite3
connection = sqlite3.connect("jeo.db")
cursor = connection.cursor()

cursor.execute("Select id, name from category order by RANDOM() limit 1")
results = cursor.fetchall()

category_id, name = results [0]
print(name)

query = """Select text, answer, value from clue
where category=%s order by value""" % (category_id,)
cursor.execute(query)
results = cursor.fetchall()

for clue in results:
  text, answer, value = clue
  print("[$%s]" % (value,))
  print("Question: %s" % (text,))
  print("Answer: What is '%s'?\n" % (answer,))

connection.close()
