# take df config json file as an input and convert it to csv file


import json
import csv
import sys
import os

# input file

df_config_json_file_directory = "DF_config_input"

# Get the absolute path to the directory
df_config_json_dir_path = os.path.abspath(df_config_json_file_directory)

# List all files in the directory
df_config_json_files = os.listdir(df_config_json_dir_path)

# Check if there are any files in the directory
if len(df_config_json_files) > 0:
    for f in df_config_json_files:
        # Check if the file's extension is one of the supported types
        if f != "dummy_file" and f.endswith(".json"):
    # Open the first file in the directory
            df_config_json_file_name = f  # Change index if you want to open a different file
            df_config_json_file_path = os.path.join(df_config_json_dir_path, df_config_json_file_name)



# output file
csv_file_path = "./DF_mapping_output/protected_object_configuration.csv"


with open(df_config_json_file_path) as f:
    data = json.load(f)
    
json_dic = data['protectedObjects']
# print(json_dic)

# open csv file

csv_file = open(csv_file_path, 'w', newline='')

# create csv writer
csvwriter = csv.writer(csv_file)

# write header

csvwriter.writerow(['name','adminStatus', 'Workflow', 'Security Template on PO(override)',])

# write rows
for row in json_dic:
    csvwriter.writerow([row['name'], row['adminStatus'], row['workflow'], row['overrideTemplate']['name']])
	
# close files
f.close()
csv_file.close()

