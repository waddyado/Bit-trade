import pandas as pd
import quandl
import time
import datetime



    






    
def check():
   
    stocks = {
        "BCHARTS/ICBITUSD",
        "BNC2/MWA_XZC_ETH",
        "BNC2/MWA_XC_XRP",
        "BNC2/MWA_ZCL_LTC",
        "BNC2/MWA_ZCL_DOGE_USD",
        "BNC2/MWA_APPC_BNB",
        "BNC2/GWA_QAU",
        "BNC2/MWA_PRL_NEO_USD",
        "BNC2/GWA_ADA"
      }       

    
     
    
    sir = 'BCHARTS/ICBITUSD'
    sir2 = 'BNC2/MWA_XZC_ETH'
    sir3 = 'BNC2/MWA_XC_XRP' 
    sir4 = 'BNC2/ZCL/LTC'
    sir5 = 'BNC2/MWA_ZCL_DOGE_USD' 
    sir6 = 'BNC2/MWA_APPC_BNB'
    
    
    if datetime.datetime.today().weekday() == 0:
        print('its monday')
        quandl.get(sir)
        time.sleep(100)
    if datetime.datetime.today().weekday() == 1:
        print('its tuesday')
        quandl.get(sir2)
        time.sleep(100)
    if datetime.datetime.today().weekday() == 2:
        print('its wednesday')
        quandl.get(sir3)
        time.sleep(100)
    if datetime.datetime.today().weekday() == 3:
        print('its thursday')
        quandl.get(sir4)
        time.sleep(100)
    if datetime.datetime.today().weekday() == 4:
        print('its friday')
        quandl.get(sir5)
        time.sleep(100)
    if datetime.datetime.today().weekday() == 5:
        print('its saturday')
        quandl.get(sir6)
        time.sleep(100)
    if datetime.datetime.today().weekday() == 6:
        print('not available on sunday')
       

    



    

check()

