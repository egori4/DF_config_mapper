# take df config json file as an input and convert it to csv file


import json
import csv
import sys

# input file
json_file = sys.argv[1]
# json_file = 'protected_object_configuration.json'

# output file
csv_file = sys.argv[2]
# csv_file = 'protected_object_configuration.csv'

# open json file
with open(json_file) as f:
    data = json.load(f)
    
json_dic = data['protectedObjects']
# print(json_dic)
# open csv file
csvfile = open(csv_file, 'w')

# create csv writer
csvwriter = csv.writer(csvfile)

# write header

csvwriter.writerow(['name','adminStatus', 'overrideTemplate',])

# write rows
for row in json_dic:
    csvwriter.writerow([row['name'], row['adminStatus'], row['overrideTemplate']['name']])
	
# close files
f.close()
csvfile.close()

