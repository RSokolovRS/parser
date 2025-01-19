import requests
import random

def random_proxy_ip(file):
    """ метод возвращающий рандомный IP """
    with open('proxy_list.txt', 'r') as file:
        ip = random.choice(file.read().split())
        return ip

