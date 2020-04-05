#! Python 3
import sys, openpyxl

# TODO: Set up the argument variables
if len(sys.argv) > 1:
    rowNum = int(sys.argv[1]) # the row at which to insert
    insertNum = (int(sys.argv[2]) + 1) # how many blank rows to insert
    fileName = sys.argv[3] # the filename

print('As per your wish, at row %s of %s, insert %s blank lines' % (rowNum, fileName, insertNum))

# TODO: Read in the file
wb = openpyxl.load_workbook('%s' %(fileName))
sheet = wb.active
maxColumn = sheet.max_column
maxRow = sheet.max_row

# TODO: Show a column before the insert
print('I didn\'t have a copy of Excel handy when I made this so I\'m just going to print out one of the columns to prove this thing inserts blank lines')
print('When you see None, that means it\'s a blank line')
print('')
print('Before the insert')
for eachRow in range(1,maxRow):
    print(eachRow, sheet.cell(row=eachRow, column=2).value)
    # cellVal = sheet['A'+str(i)]
    # print(cellVal.value)

# TODO: insert the blank rows
for j in range(1,insertNum):
    sheet.insert_rows(rowNum)

# TODO: Show after the insert
print('')
print('After the insert')
newMaxRow = int(sheet.max_row)
for eachRow in range(1,newMaxRow):
    print(eachRow, sheet.cell(row=eachRow, column=2).value)

# TODO: close the file
wb.close()