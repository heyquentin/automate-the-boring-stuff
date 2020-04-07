#!/usr/bin/env python3
# You can look at this spreadsheet in your browser by going to https://docs.google.com/spreadsheets/d/1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg/edit?usp=sharing/.
# The columns of the first sheet in this spreadsheet are “Beans per Jar,” “Jars,” and “Total Beans.” The “Total Beans” column is the product of the numbers in the “Beans per Jar”
# and “Jars” columns. However, there is a mistake in one of the 15,000 rows in this sheet. That’s too many rows to check by hand. Luckily, you can write a script that checks the totals.
import ezsheets

# TODO: Create a spreadsheet and sheet object for the Google Sheet
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss['Sheet']

totalRows = int(sheet.rowCount) # get the total number of rows

for eachRow in range(2,totalRows):
    try:
        total = int(sheet.getRow(eachRow)[0]) * int(sheet.getRow(eachRow)[1]) == int(sheet.getRow(eachRow)[2])
        if total == False:
            print('Error on row %s' %(eachRow))
    except ValueError:
        print("Something went wrong")