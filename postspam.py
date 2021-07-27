import time

import requests
import json
import random
import string

url = 'https://discod.gift/login/dologin'
# https://discod.gift/steam
# https://developer.mozilla.org/ru/docs/Web/HTTP/Cookies

useragents = open("useragents.txt", "r", encoding='UTF-8').read()


def get_random_lumensession(useragent):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'discod.gift',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': f'{useragent}'}

    data = requests.get('https://discod.gift/steam', headers=headers)
    data = data.headers.__dict__.get('_store')

    # Работа программиста и шамана имеет много общего — оба бормочут непонятные слова, совершают непонятные действия и не могут объяснить, как оно работает.
    return data.get('set-cookie')[1].split(';')[0].split('=')[1]


def generate_random_string():
    s = ""
    for a in range(57):
        s = s + string.ascii_letters[random.randrange(0, len(string.ascii_letters))]
    return s


def generate_headers(username, password):

    useragent = get_random_useragent()
    lumensession = get_random_lumensession(useragent)

    headers = {'Host': 'discod.gift',
               'User-Agent': f'{useragent + str(random.randrange(0, 10, 1))}',
               'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.5',
               'Accept-Encoding': 'gzip, deflate, br',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'X-Requested-With': 'XMLHttpRequest',
               'Content-Length': f'{len(username) + len(password) + 19}',
               'Origin': 'https://discod.gift',
               'DNT': '1',
               'Connection': 'keep-alive',
               'Referer': f'https://discod.gift/{generate_random_string()}',
               'Cookie': f'lumen_session={lumensession}; _TDG=https://discord.gg/QfAVpxdKXP; timezoneOffset=10800,0',
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

    # print(create_post())
    time.sleep(8)
