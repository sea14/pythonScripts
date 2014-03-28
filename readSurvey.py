import csv
with open('filegoeshere.csv', 'rb') as csvfile:
	surveyFile = csv.reader(csvfile, delimiter='	', quotechar='|')
	for row in surveyFile:
		print row
