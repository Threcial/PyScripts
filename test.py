import requests
import os
import re
import json


def get_json(edition):
    url = "https://www.streetfighter.com/6/buckler/api/zh-hans/stats/usagerate_master/" + edition
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    'Connection' : 'close'
    }
    response = requests.get(url, headers=headers , timeout=10)
    data = response.json()
    return data

def save_json(json_file, edition):
    path = os.path.abspath(__file__)
    pattern = r'.*(?=\\[^\\]+$)'
    path_dir = re.search(pattern, path).group()
    path_json = path_dir + '\\\\temporary\\\\' + 'usagerate_master' + '_' + edition + '.json'
    if os.path.exists(path_json):
        return 1
    with open(path_json, 'w', encoding='utf-8') as j:
        json.dump(json_file, j, ensure_ascii=False)

def sort_usagerate(data):
    master = data['usagerateData'][0]['val'][0]['val'] #list
    high_master = data['usagerateData'][0]['val'][1]['val']
    grand_master = data['usagerateData'][0]['val'][2]['val']
    ultimate_master = data['usagerateData'][0]['val'][3]['val']
    master.sort(key=lambda x : x['play_rate'], reverse=True)
    high_master.sort(key=lambda x : x['play_rate'], reverse=True)
    grand_master.sort(key=lambda x : x['play_rate'], reverse=True)
    ultimate_master.sort(key=lambda x : x['play_rate'], reverse=True)
    return master, high_master, grand_master, ultimate_master

edition = "202509"
#https://www.streetfighter.com/6/buckler/assets/images/material/character/usagerate/card_gouki.jpg

data = get_json(edition)
save_json(data, edition)
master, high_master, grand_master, ultimate_master = sort_usagerate(data)
for i in master:
    print(i['character_alpha'])
