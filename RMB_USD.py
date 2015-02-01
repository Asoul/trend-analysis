#!/bin/python
# -*- coding: utf-8 -*-

import csv

# "美元/人民幣","7.7520","0.0075","0.0968","0:05"

records = []

for year in range(2007, 2016):
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                csvfile = open('./data/'+str(year)+str(month).zfill(2)+str(day).zfill(2)+'.csv', 'rb')
            except IOError:
                continue

            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                if len(row) > 0 and row[0] == '美元/人民幣':
                    record = [str(year)+'/'+str(month)+'/'+str(day), float(row[1])]
                    records.append(record)

with open('RMB_USD2007-2015.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    for record in records:
        csvwriter.writerow(record)