import json
# wotking with json file to python

with open("File_handling/states.json","r") as rf:
    python_data=json.load(rf)

print(python_data)

for state in python_data['states']:
    del state['rank']
    print(state['name'])

# pyton data to json file
with open("File_handling/new_states.json","w") as wf:
    json.dump(python_data,wf,indent=2)

