import requests
import random

import os
from dotenv import load_dotenv


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


proxies = {
    'http': 'socks5://f"{proxy_ip}"',
    'https': 'socks5://f"{proxy_ip}"'
}

print(random_proxy_ip('proxy_list.txt'))
print(random_user_agent('user_agent.txt'))