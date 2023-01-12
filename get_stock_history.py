import yfinance as yf
import pandas as pd

# Initialise the data 
long_MA = 10
short_MA = 5
initial_wealth = '10000'
stock = '3231.TW'
period = '30d'
start_date =  '2022-10-01'
end_date = '2023-01-09'
interval = '1d'
totalprofit = 0

stock_list = pd.read_csv('stock_id.csv',sep=',', usecols=['stock_id'], squeeze=True)
# yfinance get stock price
for i in stock_list:
    df = yf.download(i, "2021-01-01")
    df.to_csv('stock_history_data/'+i+'.csv')

