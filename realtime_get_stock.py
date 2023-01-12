import twstock
import time

# Matching by call auction every 3 minutes
# 180 sec / 2 sec = 90 stocks 
stock_list=['2330', '2337', '2409']
for i in stock_list:
    value=twstock.realtime.get(i)
    print(value)
    time.sleep(2)

