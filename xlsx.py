#!/usr/bin/python


import csv, sys, xlrd

# file, col, write, delim, quote


print "\n xlsx / xls file to csv converter  \n"


if 1 < len(sys.argv):
	file = str(sys.argv[1])
	print "File: ", file
else:
	exit('No filename given.') 



workbook = xlrd.open_workbook(file)
worksheets = workbook.sheet_names()
print "Worksheet Names: ", worksheets

for worksheet_name in worksheets:
	worksheet = workbook.sheet_by_name(worksheet_name)

	csv_name = file+'_'+worksheet_name+'_'+'.txt'
	print "creating csv: %s" % csv_name 

	new_csv = open(csv_name, 'wb')
	wr = csv.writer(new_csv, quoting=csv.QUOTE_ALL)

	for rownum in xrange(worksheet.nrows):

		row = worksheet.row_values(rownum)
		wr.writerow([unicode(s).encode("utf-8") for s in row])

	new_csv.close()



print "\n"
