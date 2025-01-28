import os

from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv
import requests
from requests_ip_rotator import ApiGateway
from randomheader import RandomHeader


# import httpx
# import asyncio
# from httpx_ip_rotator import ApiGatewayTransport

load_dotenv(find_dotenv())

KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_ACCESS_KEY')
random_headers = RandomHeader()

random_headers = random_headers.header()

BASE_URL = 'https://www.wildberries.ru/'
URL = "https://www.wildberries.ru/catalog/krasota/nogti/nakladnye-nogti-i-dekor?page="


with ApiGateway(BASE_URL, access_key_id=KEY, access_key_secret=SECRET_KEY) as g:
    session = requests.Session()
    session.headers.update(random_headers)
    session.mount(BASE_URL, g)


for item in range(10):
    result = requests.get(BASE_URL + str(item))
    try:
        result.raise_for_status()
    except Exception as error:
        print(error)
        break
    else:
        print(result.status_code)







# with ApiGatewayTransport(BASE_URL, access_key_id=KEY, access_key_secret=SECRET_KEY) as g:
#     mounts = {BASE_URL: g}
#     with httpx.Client(mounts=mounts) as client:
#         response = client.get(URL)
#         print(response.status_code)



# async def main():
    # Create gateway object and initialise in AWS
    # note: this with statement can also be async with, they do the same thing for this implementation
#     with AsyncApiGatewayTransport(BASE_URL, access_key_id=KEY, access_key_secret=SECRET_KEY) as g:
#         mounts = {
#             BASE_URL: g
#         }
#         async with httpx.AsyncClient(mounts=mounts):
#             response = await client.get(BASE_URL)
#             print(response.status_code)


# asyncio.run(main())