import json
from pandas import json_normalize
import csv
import pprint

with open('sellers.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    data = data
    pprint.pprint(data['data']['products'][0])


# with open('sellers.csv', mode='w') as file:
#     writer = csv.DictWriter(file, fieldnames=data[0].keys())
#     writer.writeheader()
#     writer.writerows(data)