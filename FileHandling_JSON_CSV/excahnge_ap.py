import json
from urllib.request import urlopen

# us public data: https://datausa.io/api/data?drilldowns=Nation&measures=Population
# excahnge rate:https://open.er-api.com/v6/latest/USD

with urlopen("https://datausa.io/api/data?drilldowns=Nation&measures=Population") as response:
    data=response.read()

# converted to python object
python_data=json.loads(data)
json_str=json.dumps(python_data,indent=2)

print(json_str)