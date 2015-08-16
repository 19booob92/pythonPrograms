FOREIGN_KEY_COL = 3

counter = 666

mergedColumn = ""
out = []

with open("example_insert.sql") as file:
	position = 0;
	commasCounter = 0;

	content = file.read()

	rows = content.split("),")
	
	for row in rows:
		cols = row.split(",");
		cols[FOREIGN_KEY_COL] = str(counter)
		counter+=1
		
		mergedColumn = ",".join(cols)
		out.append(mergedColumn)

	with open("output.sql", "w")	as outputFile:
		outputFile.write("),".join(out))
		
	outputFile.close()

file.close()						 	
