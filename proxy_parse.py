import requests
import random


with open('proxy_list.txt', 'r') as file:
    text = random.choice(file.readline())
    print(text)

