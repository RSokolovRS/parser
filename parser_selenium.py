import requests
import pprint

URL = "https://catalog.wb.ru/catalog/beauty44/v2/catalog?ab_testing=false&appType=1&cat=8956&curr=rub&dest=-1255987&hide_dtype=10&lang=ru&page=1&sort=popular&spp=30"

HEADERS = {'access-control-allow-credentials':'true',
'access-control-allow-headers':'Authorization, x-captcha-id',
'access-control-allow-methods':'HEAD,GET,OPTIONS',
'access-control-allow-origin':'https://www.wildberries.ru',
'content-encoding':'gzip',
'content-type':'application/json; charset=utf-8'
}


response = requests.get(URL, headers=HEADERS)
print(response.status_code)
response_json = response.json()

total_pages = response_json['data']['total']
print(total_pages)
index_sellers = response_json['data']['products'][1]  #['supplierId']
print(index_sellers['supplierId'])
pprint.pprint((response_json['data']['products'][99]))