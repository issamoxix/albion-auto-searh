import pyautogui as gui
import time
import local
arr= [(0,0) ,(1296, 522), (1293, 161), (1181, 185), (922, 69), (829, 219), (659, 21)]
arr2= [(0,0),(1064, 0), (1078, 0), (990, 137), (1365, 752), (1365, 732), (859, 0)]
#u is the route coorndinante from the carleon market to the black market
u = [(766, 763), (225, 499), (234, 0), (475, 128), (110, 760), (49, 767), (434, 682), (438, 547)]
uBack = [(1061, 0), (1185, 0), (849, 167), (1365, 737), (1365, 767), (1359, 759), (907, 0)]
#==========================
blackMarket = (437, 114)
m_b=[(0, 393)]
b_m=[(0,0),(1365, 211)]

openmarket = [(741, 1)]
carleonMark = (817, 36)
backmarket = [(839, 767), (352, 658), (1365, 629)]
gui.FAILSAFE = False

def calibre(positions):
    positions.append(gui.position())
    gui.click(button="right")
def Buy():
    buybtn = (909, 309)
    cbuy = (835, 519)
def test(arr,d,arrback,ar2,arb):
    for i in arr:
        if i[0] == 1:
            continue
        gui.doubleClick(i,button='right')
        print('step')
        time.sleep(d)
    print('Openning Black Market')
    gui.click(blackMarket)
    if check ==1:
        x = 1
        for i in range(man,tal):
            if x == 0:
                break
            if i >man:
                if list(local.data.values())[i] == list(local.data.values())[int(i)-1]:
                    print(i,list(local.data.values())[i])
                    x = local.checkprofite(i)
                    continue
            local.SearchName(list(local.data.values())[i])
            # url=f"http://40.71.20.48/?query={list(data.values())[i]}" 
            # res = req.get(url)
            print(i,list(local.data.values())[i])
            x = local.checkprofite(i)
    time.sleep(5)
    print('Back you go')
    for r in arrback:
        if r[0] == 0:
            continue
        gui.doubleClick(r,button='right')
        gui.moveTo(r)
        gui.click(button="right")
        print('step back')
        time.sleep(d)
    time.sleep(5)
    for f in ar2:
        gui.doubleClick(f,button='right')
        time.sleep(d)
    print("Openning Carleon Market")
    gui.click(carleonMark)
    print('Buy event here')
    time.sleep(4)
    for b in arb:
        gui.doubleClick(b,button='right')
        time.sleep(d)
    print('Ended where it started')


        
check = int(input(': '))
man = int(input("From : "))
tal = int(input("To : "))



test(m_b,3,b_m,openmarket,backmarket)
