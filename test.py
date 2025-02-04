import os
import requests
import pprint

from dotenv import load_dotenv, find_dotenv
from requests_ip_rotator import ApiGateway
from randomheader import RandomHeader

load_dotenv(find_dotenv())

KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_ACCESS_KEY')

random_headers = RandomHeader()
random_headers = random_headers.header()

BASE_URL = 'https://www.wildberries.ru/'

URL = "https://catalog.wb.ru/catalog/beauty44/v2/catalog?ab_testing=false&appType=1&cat=8956&curr=rub&dest=-1255987&hide_dtype=10&lang=ru&sort=popular&spp=30&page="
TOTAL_URL = "https://catalog.wb.ru/catalog/beauty44/v2/catalog?ab_testing=false&appType=1&cat=8956&curr=rub&dest=-1255987&hide_dtype=10&lang=ru&page=1&sort=popular&spp=30"



gateway = ApiGateway(BASE_URL, access_key_id=KEY, access_key_secret=SECRET_KEY )
gateway.start()
session = requests.Session()
# session.mount(BASE_URL, gateway)



response = session.get(TOTAL_URL)
response_json = response.json()
total_pages = response_json['data']['total']
print(response.status_code)
result = total_pages / 100
print(result)



def parser_wb(URL):
    for item in range(total_pages):
        response = session.get(URL+str(item), headers=random_headers)
        list_seller = response['data']['products'][0]
        # print(list_seller)
        
    return list_seller['supplierId']

print(parser_wb(URL))
# if response.ok:
#     try:
        
#     except Exception as error:
#         print(error)
        
# else:
#     print(response.status_code)



gateway.shutdown()




    
    












gateway = ApiGateway(BASE_URL, access_key_id=KEY, access_key_secret=SECRET_KEY )
gateway.start()

# Assign gateway to session
session = requests.Session()
session.mount(BASE_URL, gateway)

# Send request (IP will be randomised)
response = session.get(URL, params={"page": 2 }, headers=random_headers)
print(response.status_code)
response_json = response.json()
total_pages = response_json['data']['total']
print(total_pages)


# Delete gateways
gateway.shutdown()



# response = requests.get(URL, headers=random_headers)
# print(response.status_code)
# response_json = response.json()

# total_pages = response_json['data']['total']
# print(total_pages)
# index_sellers = response_json['data']['products'][1]  #['supplierId']
# print(index_sellers['supplierId'])
# pprint.pprint((response_json['data']['products'][99]))