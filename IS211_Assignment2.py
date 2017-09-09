
import urllib2
import argparse
import logging
import datetime

##function for downloading the data and storing it in variable
def downloadData(str1):
    request = urllib2.Request(str1.url)
    response = urllib2.urlopen(request)
    csvData = response.read()
    return csvData

##function to process the downloaded data and store in a dictionary
def  processData(str1):
	lines = str1.split("\n")
	my_dict = {}
	mylog = logging.getLogger('assignment2')
	for idx,line in enumerate(lines[1:]):
		try:
			id,name,date_text = line.split(',')
			lineNum = idx + 2
			date_data = datetime.datetime.strptime(date_text, '%d/%m/%Y')
			my_dict[id] = (name,date_data)
		except ValueError:
			mylog.error('Error processing line #%d for ID #%s'%(lineNum,id))
 	return my_dict

##function to search person details based on id
def displayPerson(id, personData):
	if id in personData:
		print('Person #'+ id + ' is '+ personData[id][0] + ' with a birthday of '+ personData[id][1].strftime('%Y-%m-%d'))
	else:
		print('No user found with that id')

##function to setup logger
def setup_logger():
	logging.basicConfig(filename = 'error.log', level = logging.ERROR,filemode = 'w')

	    
def main():
	setup_logger()
	parser = argparse.ArgumentParser(description= 'Download, Process and Lookup stuff')
	parser.add_argument('--url')
	url = parser.parse_args()
	csvData = downloadData(url)
	personData = processData(csvData)
	while True:
		id = raw_input('Enter an Id to lookup: ')
		if int(id) <= 0:
			exit()
		displayPerson(id,personData)

if __name__ == '__main__':
	main()