import pandas as pd
import quandl
import time
from tkinter import *

def StockofDay():
    Stock1 = 'BCHARTS/ICBITUSD'
    Stock2 = 'GDAX/ETH_BTC'
    print('The stocks of the day are BCHARTS/ICBITUSD and GDAX/ETH_BTC')
    df = quandl.get(Stock1)
    dg = quandl.get(Stock2)
    g = input('Would you like to see them? (Y/N)')
    if g == 'Y':
        print(df,dg)
    if g == 'y':
        print(df,dg)
    if g == 'N':
        print('Ok')
    if g == 'n':
        print('Ok')





def main():

   master = Tk()

   label1 = Label(master, text='Arco Computing')
   label1.pack()

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
   
   print('')
   print('')
   bob = print('If you would like help with stock names read help.txt')
   print(bob)
   df = input('What stock will it be? : ')    
    

   for item in stocks:
        if df == "BCHARTS/ICBITUSD" in stocks:
           dL = quandl.get(df)
           print(dL.head())
           main()
           
        if df == "BNC2/MWA_XZC_ETH" in stocks:
           dL = quandl.get(df)
           print(dL.head())
           main()
           
       
   
        if df == "BNC2/MWA_XZC_XRP" in stocks:
           dL = quandl.get(df)
           print(dL.head())
           main()


   
        if df == "BNC2/MWA-ZCL_LTC" in stocks:
           dL = quandl.get(df)
           print(dL.head())
           main()
 

        if df == "BNC2/MWA_ZCL_DOGE_USD" in stocks:
           dL = quandl.get(df)
           print(dL.head())
           main()

   
        if df == "BNC2/MWA_APPC_BNB" in stocks:
           dL = quandl.get(df)
           print(dL.head())
           main()


        if df ==  "BNC2/GWA_QAU" in stocks:
           dL = quandl.get(df)
           print(dL.head())
           main()


        if df ==  "BNC2/MWA_PRL_NEO_USD"  in stocks:
           dL = quandl.get(df)
           print(dL.head())
           main()


        if df ==  "BNC2/GWA_ADA"  in stocks:
           dL = quandl.get(df)
           print(dL.head())
           main()
        

           
        else:
           backmain()

       
   
   
       
       
       


def backmain():
    print('not a valid stock please pick a new one')
    time.sleep(2)
    main()
          
   



main()

