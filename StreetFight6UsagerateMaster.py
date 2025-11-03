# Since Capcom's offical website only retains data from the past eight months
# the earliest data available is from February 2025


import requests
from lxml import etree
import os
import re
import json
import matplotlib.pyplot as plt
from time import sleep


def check_edition():
    url = "https://www.streetfighter.com/6/buckler/zh-hans/stats/usagerate_master"
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    'Connection' : 'close'
    }
    response = requests.get(url=url, headers= headers, timeout=10)
    text = response.text
    tree = etree.HTML(text)
    ele = tree.xpath('/html/body/div[1]/div/article[2]/aside[1]/div/section/select/option')
    date = [i.text.replace(".", "") for i in ele]
    return date

def get_json_by_web(edition):
    url = "https://www.streetfighter.com/6/buckler/api/zh-hans/stats/usagerate_master/" + edition
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    'Connection' : 'close'
    }
    response = requests.get(url, headers=headers , timeout=10)
    data = response.json()
    return data

def check_json_file(edition):
    path = os.path.abspath(__file__)
    pattern = r'.*(?=\\[^\\]+$)'
    path_dir = re.search(pattern, path).group()
    path_json = path_dir + '\\\\temporary\\\\' + 'usagerate_master' + '_' + edition + '.json'
    if os.path.exists(path_json):
        with open(path_json, 'r', encoding='utf-8') as j:
            data = json.load(j)
        return data
    else:
        data = get_json_by_web(edition)
        with open(path_json, 'w', encoding='utf-8') as j:
            json.dump(data, j, ensure_ascii=False)
        return data

class usage:

    def __init__(self, usagerate_json_list):
        self.usagerate = [i[0] for i in usagerate_json_list]
        self.date = [i[1] for i in usagerate_json_list]
        self.time_span = len(self.date)

    def sort_usagerate(self, data, category):
        if category == 'Master':
            master = data['usagerateData'][0]['val'][0]['val'] #list
            master.sort(key=lambda x : x['play_rate'], reverse=True)
            return master
        elif category == 'High_Master':
            high_master = data['usagerateData'][0]['val'][1]['val']
            high_master.sort(key=lambda x : x['play_rate'], reverse=True)
            return high_master
        elif category == 'Grand_Master':
            grand_master = data['usagerateData'][0]['val'][2]['val']
            grand_master.sort(key=lambda x : x['play_rate'], reverse=True)
            return grand_master
        elif category == 'Ultimate_Master':
            ultimate_master = data['usagerateData'][0]['val'][3]['val']
            ultimate_master.sort(key=lambda x : x['play_rate'], reverse=True)
            return ultimate_master

    def master_show(self):
        master_usagerate = [self.sort_usagerate(i, 'Master')  for i in self.usagerate]
        for i in range(len(master_usagerate)):
            print(self.date[i], end="  ")
            print(master_usagerate[i][0]['character_alpha'])
    
    def high_master_show(self):
        high_master_usagerate = [self.sort_usagerate(i, 'High_Master')  for i in self.usagerate]
        for i in range(len(high_master_usagerate)):
            print(self.date[i], end="  ")
            print(high_master_usagerate[i][0]['character_alpha'])


    
edition = check_edition()
json_list = []
for i in edition:
    json_list.append([check_json_file(i), i])
    sleep(0.1)
a = usage(json_list)
a.master_show()
a.high_master_show()

#https://www.streetfighter.com/6/buckler/assets/images/material/character/usagerate/card_gouki.jpg
