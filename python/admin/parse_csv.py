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

def process_csv():
    csvfile = 'parse.csv'
    csv_out = '/tmp/parse_output.csv'

    '''
    By default the " is the escape character for CSV and default delimiter is ,
    We also insist that 'excel' be the dialect so import and export from/to an Excel
    worksheet is compatible. It also knows how to handle the ',' so that it is not an extraneous
    column
    '''

    '''
    Here we open a CSV file for writing. Then read from another CSV file so we can manipulate the data, 
    and write it out correctly.
    '''
    f = open(csv_out, 'w')
    csvwriter = csv.writer(f, dialect='excel', delimiter = ',', quotechar = '"')

    with open(csvfile) as d:
        csv_reader = csv.reader(d, dialect='excel', delimiter = ',', quotechar = '"')
        for row in csv_reader:
            #print row
            '''
            We want to convert any JSON strings to DICT format so that it can be dumped correctly
            to the CSV file and any ',' are preserved. For that the header at row[2] or any word at row[2] should
            be skipped out and written as is. 
            '''
            #if (row[2] == 'player' or row[2] == 'blah2'):
            if (row[2] not in '^"{'):
                print row
                csvwriter.writerow(row)
            else:
                json_str = json.dumps(ast.literal_eval(row[2]))
                print (json_str)
                csvwriter.writerow(row)

'''
The fabled Main. Where it all begins.
'''
def main():
    process_csv()


if __name__ == "__main__":
    main()

