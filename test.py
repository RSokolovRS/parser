import ipaddress
from random import choice, randint
import os
from dotenv import load_dotenv, find_dotenv

from httpx import Request, URL
from requests_ip_rotator import ApiGateway, MAX_IPV4
import httpx
import asyncio


load_dotenv(find_dotenv())

KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_ACCESS_KEY')

PARSING_URL = 'https://www.avito.ru/moskva?q='
BASE_URL = 'https://www.avito.ru'
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9,ru;q=0.8",
    "cache-control": "max-age=0",
    "if-none-match": "W/\"2fba1a-vj8ZZTJXtBDfFHvTGM6hmxDjuNE\"",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
}


class AWSGatewayTransport(ApiGateway, httpx.AsyncHTTPTransport):

    async def handle_async_request(self, request: Request):
        endpoint = choice(self.endpoints)
        # Replace URL with our endpoint
        request.url = URL("https://" + endpoint + "/ProxyStage/" + request.url.path)
        # Replace host with endpoint host
        request.headers["Host"] = endpoint
        # Auto generate random X-Forwarded-For if doesn't exist.
        # Otherwise AWS forwards true IP address in X-Forwarded-For header
        x_forwarded_for = request.headers.get("X-Forwarded-For")
        if x_forwarded_for is None:
            x_forwarded_for = ipaddress.IPv4Address._string_from_ip_int(randint(0, MAX_IPV4))
        # Move "X-Forwarded-For" to "X-My-X-Forwarded-For". This then gets converted back
        # within the gateway.
        request.headers.pop("X-Forwarded-For", None)
        request.headers["X-My-X-Forwarded-For"] = x_forwarded_for
        # Run original python requests send function
        return await super().handle_async_request(request)


async def main():
    with AWSGatewayTransport(BASE_URL, access_key_secret=KEY, access_key_id=SECRET_KEY) as g:
        mounts = {
            "all://": g,
        }
        async with httpx.AsyncClient(mounts=mounts) as client:
            for index in range(5):
                res = await client.get(PARSING_URL + str(index), headers=HEADERS)
                print(res)

asyncio.run(main())