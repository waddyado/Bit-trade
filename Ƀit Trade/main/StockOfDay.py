import pandas as pd
import quandl
import time



def StockofDay():
    Stock1 = 'BCHARTS/ICBITUSD'
    Stock2 = 'GDAX/ETH_BTC'
    print('The stocks of the day are BCHARTS/ICBITUSD and GDAX/ETH_BTC')
    df = quandl.get(Stock1)
    dg = quandl.get(Stock2)
    g = input('Would you like to see them? (Y/N)')
    if g == 'Y':
        print(df,dg)
        time.sleep(100)
    if g == 'y':
        print(df,dg)
        time.sleep(100)
    if g == 'N':
        print('Ok')
        exitsequence()
    if g == 'n':
        print('Ok')
        exitsequence()
  


def exitsequence():
    print('Exiting in seconds')
    time.sleep(3)
    exit
    


StockofDay()

