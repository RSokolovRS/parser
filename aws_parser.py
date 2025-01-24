import os
from dotenv import load_dotenv, find_dotenv


import httpx
import asyncio
from httpx_ip_rotator import ApiGatewayTransport

load_dotenv(find_dotenv())

KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_ACCESS_KEY')


BASE_URL = 'https://www.wildberries.ru/'
URL = "https://www.wildberries.ru/catalog/krasota/nogti/nakladnye-nogti-i-dekor?page=1"

with ApiGatewayTransport(BASE_URL, access_key_id=KEY, access_key_secret=SECRET_KEY) as g:
    mounts = {
        BASE_URL: g
    }
    with httpx.Client(mounts=mounts) as client:
        response = client.get(URL)
        print(response.status_code)



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