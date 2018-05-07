#!/usr/bin/python
#
# Utils is always imported first
#
import csv
import string

def main():
    from lank import utils
    from lank.vars import db_creds
    utils.init()
    recipient = ['larry.masc@gmail.com', 'larry_mario@yahoo.com']
    # recipient = 'larry_mario@yahoo.com'
    # recipient = 'larry.masc@gmail.com'
    subject = 'Test from Python'
    body = 'Test 5 to GMail and Yahoo with Mimetext and Multipart with file'
    # attachment = "NOFILE"
    attachment = "/home/lmascare/misc/earthmoon_nasa.jpg"
    # attachment = "/home/lmascare/misc/KEYS.gz"
    attachment = "NOFILE"

    # Process a CSV file and send the data as a table.
    csv_file = "/u/tmp/cities.csv"
    out_file = "/u/tmp/cities_table.html"
    with open(csv_file, "r") as csv_data:
        # csv_reader = csv.reader(csv_data, dialect="excel", delimiter=",", quotechar='"', strict=True)
        csv_reader = csv.reader(csv_data, dialect="excel",
                                delimiter=",", quotechar='"', strict=True,
                                skipinitialspace=True)
        # Begin table definition
        table = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
            text-align: left;
            background-color: powderblue;
            color: green;
        }
        </style>
        </head>
        <table>
        <caption><h1>Geo Location of cities</h1></caption>
        """
        header = next(csv_reader)
        print type(header)
        table += "<th>" + string.join(header, "</th><th>") + \
                 "</th>"
        for row in csv_reader:

            table += "<tr>" + \
                          "<td>" + \
                              string.join( row, "</td><td>" ) + \
                          "</td>" + \
                     "</tr>\n"
        # End table definition
        table += "</table>"

        table += "</html>"
    # print table
    utils.send_mail(recipient, subject, table, attachment)
    f = open(out_file, "wb")
    f.write(table)
    f.close()
    exit(0)

if __name__ == "__main__":
    main()
