import csv
surveyFile =  open('surveyfileNameGoesHere.csv', 'rb')
reader = csv.reader(surveyFile)

rownum = 0
for row in reader:
	# save the header row.
	if rownum == 0:
		header = row
	else:
		colnum: 0
		for colnum = 0 in row:
			print '%-8s: %s' % (header[colnum], col)
			colnum += 1

		rownum +=1

	surveyFile.close()
