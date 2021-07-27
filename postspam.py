import time

import requests
import json
import random

url = 'https://discod.gift/login/dologin'
# https://discod.gift/steam
# https://developer.mozilla.org/ru/docs/Web/HTTP/Cookies

useragents = open("useragents.txt", "r", encoding='UTF-8').read()


def generate_headers(username, password):
    headers = {'Host': 'discod.gift',
               'User-Agent': f'{get_random_useragent() + str(random.randrange(0, 10, 1))}',
               'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.5',
               'Accept-Encoding': 'gzip, deflate, br',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'X-Requested-With': 'XMLHttpRequest',
               'Content-Length': f'{len(username) + len(password) + 19}',
               'Origin': 'https://discod.gift',
               'DNT': '1',
               'Connection': 'keep-alive',
               'Referer': 'https://discod.gift/3WUpPRLxtCuFWdbd4a5a8d2Jt4T5rbnAr51FGVdWpnItFkAoklXmROwQr',
               'Cookie': 'lumen_session=gBoj5ncX2RKnbMkPXU3SRCojHhHqOWlU67EhaiaO; _TDG=919ebdb693dd4e55a2c4e1cb7d87fefe; timezoneOffset=10800,0',
               'Sec-Fetch-Dest': 'empty',
               'Sec-Fetch-Mode': 'cors',
               'Sec-Fetch-Site': 'same-origin',
               'Sec-GPC': '1'
               }
    return headers


def get_random_useragent():
    s = useragents.split('\n')
    return s[random.randrange(0, len(s))]


def get_random_userdata():
    r = requests.get("https://randomuser.me/api/?format=json")
    data = json.loads(r.text)
    return data['results'][0]['login']


def create_post():
    u = get_random_userdata()["username"]
    p = get_random_userdata()["password"]
    r = requests.post(url, data=f'username={u}&password={p}', headers=generate_headers(u, p))
    return r


# r = requests.post(url, data=f'username={username}&password={password}', headers=headers)
while True:
    print(create_post())
    time.sleep(3)