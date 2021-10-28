import json

#1) json.loads(json_string) json string to python object
#2) json.dumps(python_object,indent=2) python object to json string
#3) json.load(json_file) json file to python object
#4) json.dump(python_data,writeFP,indent=2) python data to json file

# json string to python dict
# json_str='{"name":"Raghu","age":30,"email":null,"present":false}'

# y= json.loads(json_str)
# print(y)
# print(type(y))

# # python obj to json string
# python_dict=y
# json_str1=json.dumps(python_dict)

# print(json_str1)
# print(type(json_str1))

json_str='''
{
    "people":[
        {"name":"Raghu","email":"raghu@gmail.com"},
        {"name":"Rahul","email":"rahul2@gmail.com"},
        {"name":"Abhijit","email":"abhijit3@gmail.com"}
    ]
}

'''

python_data=json.loads(json_str)

for person in python_data['people']:
    print(person['email'])

print(type(python_data))
print()

# python to json str
json_str1=json.dumps(python_data,indent=2)
print(json_str1)