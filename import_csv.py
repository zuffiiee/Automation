#!/usr/bin/env python
# coding: utf-8

import csv
from datetime import date

search_url=input("Enter a domain name:")


# Opening csv file
data=open('links.csv') #,encoding='utf-8'
csv_data=csv.reader(data)
data_lines=list(csv_data)


# Creating list of all links
url_list = []
for line in data_lines[1:]:
    url_list.append(line[2])


# Creating a csv file
op_file=open('testfile.csv',mode='w',newline='')  #f = open('to_save_file.csv','a',newline='')
csv_writer=csv.writer(op_file,delimiter=',')      #csv_writer = csv.writer(f)
csv_writer.writerow(['Date','Rank'])


# Finding rank

r=[n for n, item in enumerate(url_list) if search_url in item]
try:
    rank=r[0]+1    
except IndexError:
    csv_writer.writerow([date.today(), ])
else:
    csv_writer.writerow([date.today(),rank])


# Closing file
op_file.close()

