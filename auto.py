import pyautogui as gui 
import time 
from sys import argv
#use fullscreen
#quality everthing low
#my Screen  resolution  1366, 768
#name =>x=458 , y=190   (%)=>  x=33.52855051 % ,y=24.73958333 %
#q => x=859 , y=192     (%)=>  x=62.88433382 % , y=24.73958333 %
#en => x=789, y=190     (%)=>  x=57.75988287 % , y=24.73958333 %
#en0 =>                 (%)=>  x=55.78330893118594 ,y = 29.557291666666668     
#en1 =>                 (%)=>  x=56.07613469985359 ,y = 31.901041666666668     
#en2 =>                 (%)=>  x=56.149341142020496 ,y = 33.984375     
#en3 =>                 (%)=>  x=55.710102489019036 ,y = 36.71875

#q1 =>                  (%)=> x=64.93411420204978 ,y=29.817708333333332
#q2 =>                  (%)=> x=65.30014641288433 ,y=31.770833333333332
#q3 =>                  (%)=> x=65.44655929721816 ,y=33.463541666666664
#q4 =>                  (%)=> x=65.37335285505124 ,y=37.109375
#q5 =>                  (%)=> x=64.56808199121522 ,y= 39.192708333333336
print('Start')
# time.sleep(1) 
# print('COpy')
#conver from percentages to pixels
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
    print('Moving ? ')
    gui.moveTo(name)
    gui.mouseDown()
    gui.mouseUp()
    gui.hotkey('ctrl', 'a')
    gui.write(query)
    roll()
def roll():
    print('Moving ? ')
    
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
  

SearchName(' '.join([str(elem) for elem in argv[1:]]))
# gui.hotkey('ctrl', 'v')
