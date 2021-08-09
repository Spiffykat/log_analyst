#! /usr/bin/python3
   
import re
import sys
import csv
import operator
    
log = sys.argv[1]
errors = {}
     
with open(log) as file:
	for line in file.readlines():
		if "ERROR" not in line:
			continue
		pattern=r"ticky: (ERROR):? ([\w' ]*)[\[[#0-9]*\]?]? ?"
		result=re.search(pattern, line)
		if result is None:
			continue
		err = result[2]
		errors[err] = errors.get(err, 0)+1
    
print(errors)

error_list = sorted(errors.items(), key=operator.itemgetter(0))
error_list.insert(0,('ERROR','Count'))

with open('error_messages.csv','w',newline='') as csvfile:
	for key,value in error_list:
		csvfile.write(str(key)+''+str(value)+'\n')


