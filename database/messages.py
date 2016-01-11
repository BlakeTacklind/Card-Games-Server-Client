import json

with open('../common.json', 'r') as data_file:    
    data = json.load(data_file)

Messages = data["messagesCodes"]