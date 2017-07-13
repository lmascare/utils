#!/usr/bin/python

'''

'''

'''
Importing CSV module is a given. Why ast? The JSON string in a CSV file cannot be converted to JSON type unless it
is first converted to dict using ast
'''
import csv
import ast
import json

csvfile = 'parse.csv'

with open(csvfile) as d:
    csv_reader = csv.reader(d, dialect='excel', delimiter = ',', quotechar = '"')
    for row in csv_reader:
        #print row
        if (row[2] == 'player' or row[2] == 'blah2'):
            print row
        else:
            json_str = json.dumps(ast.literal_eval(row[2]))
            print (json_str)

