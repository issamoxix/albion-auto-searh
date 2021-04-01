import pyautogui as gui 
import time 
import requests as req
import sys
from playsound import playsound
from datetime import datetime

gui.FAILSAFE = False


date = datetime.today().strftime('%Y-%m-%d')
def get_corr(w,h,x,y):
    return (round((w*x)/100),round(h*y/100))
# coordinant by percentage
per_name = (33.52855051,24.73958333)
per_q = (62.88433382,24.73958333)
per_Q = [(64.93411420204978,29.817708333333332),(65.30014641288433,31.770833333333332),(65.44655929721816,33.463541666666664),(65.37335285505124,37.109375),(64.56808199121522,39.192708333333336)]
per_E = [(55.78330893118594,29.557291666666668),(56.07613469985359,31.901041666666668),(56.149341142020496,33.984375),(55.710102489019036,36.71875)]
per_en = (57.75988287,24.73958333)
# coordinants by pixels
w,h = gui.size()
name = get_corr(w,h,per_name[0],per_name[1])
q = get_corr(w,h,per_q[0],per_q[1])
en = get_corr(w,h,per_en[0],per_en[1])
# Search the query function
def SearchName(query):
    # print('Moving ? ')
    gui.moveTo(name)
    gui.mouseDown()
    gui.mouseUp()
    gui.hotkey('ctrl', 'a')
    gui.write(query)
    roll()
def roll():

    
    for r in per_E:
        gui.moveTo(en)
        gui.mouseDown()
        gui.mouseUp()
        gui.moveTo(get_corr(w,h,r[0],r[1]))
        gui.mouseDown()
        gui.mouseUp()
        for i in per_Q:
            gui.moveTo(q)
            gui.mouseDown()
            gui.mouseUp()
            gui.moveTo(get_corr(w,h,i[0],i[1]))
            gui.mouseDown()
            gui.mouseUp()
            time.sleep(0.1)
  

import json

with open('items2.json') as f:
  data = json.load(f)
check = int(input(': '))
man = int(input("From : "))
tal = int(input("To : "))
profiteKILLER = False
# checkprofite functino is where take one argument wich is the items index in the items array 
# it send request to the albion online project api and check for profite between the black and carleon market

def checkprofite(n):
    print('Checking for profite')
    item_id = list(data.keys())[n]
    res  = req.get(f'https://www.albion-online-data.com/api/v2/stats/prices/{item_id}?locations=Black Market,Caerleon')
    datax = json.loads(res.text)
    bm = []
    Cm = []
    for k in datax:
        if k['city'] == "Black Market":
            bm.append(k)
        else:
            Cm.append(k)

    # print(len(datax))
    # print(bm)
    # print(Cm)
    for o in range(0,len(datax)):
        for market in bm:
            
            if date in str(market['buy_price_max_date']):

                if int(market['buy_price_max']) ==0:
                    continue
                # print('Sell Price : ',market['buy_price_max'])
                for cam in Cm:
                    if date in str(cam['sell_price_min_date']):
                        # print(market['buy_price_max_date'],cam['sell_price_min_date'])
                        if cam['quality'] == market['quality'] :
                            if int(cam['sell_price_min']) == 0:
                                continue
                            profitePrice = int(market['buy_price_max']) - int(cam['sell_price_min']) -(int(market['buy_price_max'])*0.06)
                            # print('Buy Price : ',cam['sell_price_min'])
                            if int(profitePrice) >= 10000:
                                print('Item_id : ',market['item_id'])
                                print('Quality : ',market['quality'])
                                print('Black Market Price : ',int(market['buy_price_max']))
                                print('Carleon Market Price : ',int(cam['sell_price_min']))
                                print('PROFITE =====> ',int(profitePrice))
                                playsound('./oof.mp3')
                                exo = input('EXIT ?')
                                sys.exit()
                    else:
                        continue
            else:
                continue
if check ==1:
    for i in range(man,tal):
        if profiteKILLER == True:
            break
        if i >man:
            if list(data.values())[i] == list(data.values())[int(i)-1]:
                print(i,list(data.values())[i])
                checkprofite(i)
                continue
        SearchName(list(data.values())[i])
        # url=f"http://40.71.20.48/?query={list(data.values())[i]}" 
        # res = req.get(url)
        print(i,list(data.values())[i])
        checkprofite(i)

    # print(datax)

    # print(url)
# gui.hotkey('ctrl', 'v')
