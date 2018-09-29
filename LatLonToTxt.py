from pygeocoder import Geocoder
import csv
import time
import pandas as pd

cscfile = 'team.csv'
CSVfields = ['text', 'location']
location = []
for d in csv.DictReader(open('finaltweets.csv', encoding="utf-8"), delimiter=','):
    location.append(d['location'])
print(location)

lat = ''
lon = ''
loc_arr = []
loc_arr_final = []
i=0
for l in location:
    lon = l.split(',')[0]
    lat = l.split(',')[1]
    if i<300:
        try:
            results = Geocoder('AIzaSyDlF-Z6QHzTRC28kqnfZvRV60NFg3Pmpmg').reverse_geocode(float(lat[1:-1]),float(lon[1:-1]))
            loc_arr = str(results).split(',')
        except:
            loc_arr.append('')
        loc_arr_final.append(loc_arr)
        i=i+1
    else:
        continue

with open('location_data_dump_neu.csv', "w", encoding="utf-8") as csv_file:
         for row in loc_arr_final:
           print(row)
           writer = csv.writer(csv_file, delimiter=',')
           writer.writerow(row)