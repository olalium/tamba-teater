import random as r
import time

def terminal(dur):
    x = 1
    t0 = time.time()
    while True:
        i = 1
        S = ''
        if t0 < time.time() - 0.04:

            while i < 60:
                tab_space = r.randrange(0,100)
                if tab_space > 80:
                    S += int(tab_space/20)*' '
                    i += int(tab_space/20)
                else:
                    S += str(r.randrange(0,2)) #chr(0 eller 1)
                    i += 1
            print(S)
            x += 1
            t0 = time.time()
        if x > dur:
            break

def waiting():
    i = 0
    s = ''
    while i < 59:
        s += '#'
        i += 1
    print(s+'\n')
    return input('press enter for å fortsette .  .  .  .  .  .  .')

def utregning1():
    print("################## STARTER KALKULASJONER ##################")
    time.sleep(0.5)
    print("årstall: 2117\nmennesker på jorden: 12,023,794,662\nsannsynlighetsindex:aplha-34588-sigma.static\nutregningsmodulversjon:3.023.54")
    time.sleep(0.5)
    print("starter utregning")
    time.sleep(0.5)
    print("KALKULERER")
    s = "|"
    for i in range(20):
        time.sleep(r.randrange(2,10)/10)
        s+="|"
        print(s)
    print("RESULTAT : 2,7 p/strik.pinn.skad.")