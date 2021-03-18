import requests
import time
import re

from settings import *
from bs4 import BeautifulSoup


session = requests.Session()
session.auth = (username, password)
session.headers.update({'User-Agent': user_agent})


def login():
    response = session.get('https://lk.sut.ru/cabinet/')
    return response


def schedule(rasp, week):
    data = {'open': '1',
            'rasp': rasp,
            'week': week}

    response = session.post('https://lk.sut.ru/cabinet/project/cabinet/forms/raspisanie.php', data=data)
    return response


def start(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        lesson = soup.find('a', text='Начать занятие').get('onclick')
        numb = re.findall(r'(\d+)', str(lesson))
        schedule(numb[0], numb[1])
        return True
    except AttributeError:
        print('Невозможно начать занятие. Новая попытка через 5 минут')
        return False


def main():
    while True:
        login()
        response = session.post('https://lk.sut.ru/cabinet/project/cabinet/forms/raspisanie.php')

        if not start(response.text):
            time.sleep(300)


if __name__ == '__main__':
    main()
