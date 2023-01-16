import twstock
import time
import pandas as pd
from bs4 import BeautifulSoup
import re
from json2html import *
import json

def insert_html(value):
    soup = BeautifulSoup(open('stock.html'), 'html.parser')
    # p_tag = soup.new_tag("p")
    # p_tag.string = value['realtime']['latest_trade_price']
    # soup.body.append(p_tag)
    json_type=json.dumps(value)
    soup.body.append(json2html.convert(json = json.loads(json_type)))
    print()
    # with open("stock.html", "w") as file:
    #     file.write(str(soup))

if __name__ == '__main__':
    # Matching by call auction every 3 minutes
    # 180 sec / 2 sec = 90 stocks 
    stock_list = pd.read_csv('stock_id.csv',sep=',', usecols=['stock_id'], squeeze=True)
    for i in stock_list:
        value=twstock.realtime.get(re.sub('.TW|O','',i))
        print(value)
        insert_html(value)
        time.sleep(2)

