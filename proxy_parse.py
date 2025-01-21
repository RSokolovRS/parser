import requests
from bs4 import BeautifulSoup
import random
import pprint

# import os
# from dotenv import load_dotenv


def random_proxy_ip(file):
    """ метод возвращающий рандомный IP """
    with open(file, 'r') as file:
        ip = random.choice(file.read().split())
        return ip


def random_user_agent(file):
    """ метод возвращающий рандомный user-agent """
    with open(file, 'r') as file:
        ua = random.choice(file.read().split('\n'))
        return ua
    

proxy_ip = random_proxy_ip('proxy_list.txt')
headers = random_user_agent('user_agent.txt')



proxies = {
    'http': 'http://f"{proxy_ip}"',
    # 'https': 'https://f"{proxy_ip}"'
}

print(type(proxy_ip))
print(type(headers))
# # url='https://www.wildberries.ru/'

# s = requests.Session()
# response = requests.get(url='https://www.wildberries.ru/catalog/krasota/nogti/nakladnye-nogti-i-dekor?page=1',headers=user_agent, proxies=proxies)

# print(response.status_code)
# s = Session()
# req = Request('GET',  url)

# prepped = s.prepare_request(req)

# print(req.headers) 



def get_location(url):
    response = requests.get(url,proxies='https://fwafaq:KjwouzQ1www@46.8.15.143:5500')
    soup = BeautifulSoup(response.text, 'lxml')
    
    ip = soup.find('div', class_="js-value-copy cc-text cc-text--h3 cc-text--bold").text.split()
   
    print(ip)



get_location('https://2domains.ru/web-tools/myip')