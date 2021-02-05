#I was a Teaching Assitant for various Intro to Maya courses in 2020 and 2021
#The professor wanted to use google drive to house students assignments and I had to make a folder for each student
#In the larger classes this became tedious, so I wrote a script to do it for me based on a csv of the roster from the schools portal
#It creates folders with all the students names on my desktop so I can just upload that to the drive

import csv
import os
  
# Parent Directory path 
parent_dir = "C:/Users/theon/Desktop/Student Folders"
  
with open('roster.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	list2 = [(row.split()[0] + row.split(",")[1]) for row in csvfile]
	for x in list2:
		if len(x.split(",")) > 1:
			folder_name = x.split(",")[1] + x.split(",")[0]
			folder_name = str.replace(folder_name, '\"\"', ' ')
			print(folder_name)
			path = os.path.join(parent_dir, folder_name) 
			os.mkdir(path)
		# print(x)
	# for row in spamreader:
	# 	print(', '.join(row))