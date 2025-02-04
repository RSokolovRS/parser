import json
from pandas import json_normalize
import csv
import pprint


def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    
    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)


csv_to_json('sellers.csv', 'processed_sellers.json')



# with open('sellers.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     data = data
#     pprint.pprint(data['data']['products'][0])


# with open('sellers.csv', mode='w') as file:
#     writer = csv.DictWriter(file, fieldnames=data[0].keys())
#     writer.writeheader()
#     writer.writerows(data)