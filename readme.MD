# About

The script takes DefenseFlow configuration in json format as an input and convert it to csv file.
Tested on Version 4.7

# Version management

v1.0

Script parses DefenseFlow config and maps 'PO name','adminStatus', 'overrideTemplate'

# How to run

1. Put defenseflow config to /DF_config_input directory  

2. Run the script

python3 dp_config_mapper.py 

3. Output file in csv format will be created in DF_mapping_output directory
