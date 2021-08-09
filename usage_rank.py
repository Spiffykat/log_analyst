#! /usr/bin/python3
   
import re
import sys
import csv
import operator
    
log = sys.argv[1]
users = {}
     
with open(log) as file:
	for line in file.readlines():
		if "ticky" not in line:
			continue
		pattern=re.search(r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
		msg, err, usr = pattern.group(1), pattern.group(2), pattern.group(3)
		
		if usr not in users.keys():
			users[usr] = {}
			users[usr]['INFO']=0
			users[usr]['ERROR']=0

		if msg == 'INFO':
			if usr not in users.keys():
				users[usr] = {}
				users[usr]['INFO']
			else:
				users[usr]['INFO'] += 1
		elif msg == 'ERROR':
			if usr not in users.keys():
				users[usr] = {}
				users[usr]['INFO'] =0
			else:
				users[usr]['ERROR'] +=1
		
file.close
usersList = sorted(users.items(), key=operator.itemgetter(0))

with open('user_statistics.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Username", "INFO", "ERROR"])
with open('user_statistics.csv', 'a', newline='') as user_csv:
	for key, value in usersList:
		user_csv.write(str(key) + ',' + str(value['INFO']) + ',' + str(value['ERROR'])+'\n')
