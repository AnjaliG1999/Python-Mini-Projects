#! python3
#take a list of lists of strings and display it in a well-organized table with each column right-justified

tableData = [['apples', 'oranges', 'cherries', 'banana'],
			['Alice', 'Bob', 'Carol', 'David'],
			['dogs', 'cats', 'moose', 'goose']]

colWidths = list()
for lst in tableData:
	lrg = 0
	for l in lst:
		if len(l) > lrg:
			lrg = len(l)
	colWidths.append(lrg)
print(colWidths)

for tbl in range(len(tableData[0])): #4 times
	for i in range(len(tableData)):	#3 times
		print(tableData[i][tbl].rjust(colWidths[i]), end = " ")
	print()