import json
from urllib.request import urlopen

# with urlopen("https://api.coingecko.com/api/v3/exchange_rates") as response:
#     data=response.read()
#     python_data=json.loads(data)

#print(python_data)

# with open("File_handling/api_data.json","w") as f:
#     json.dump(python_data,f,indent=2)

#y=json.dumps(python_data,indent=2)
#print(y)

# print("Parsed data")
# print(python_data['rates']['btc'])
# print(python_data['rates']['jpy'])
with open("File_handling/api_data.json","r") as rf:
    python_data=json.load(rf)

print(python_data['rates']['btc'])
print(python_data['rates']['jpy'])
