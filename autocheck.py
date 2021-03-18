import requests
from settings import *


headers = {
    'User-Agent': user_agent
}

response = requests.get('https://lk.sut.ru/cabinet/', headers=headers, auth=(username, password))
print(response.status_code)
