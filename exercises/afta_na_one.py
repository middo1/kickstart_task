import random
import time

def cnum(num):
    play = []
    x = 0
    while x < num:
        r = random.randint(0,num*5)
        if play.__contains__(r) == False:
            play.append(r)
            x += 1
    return play
def processplay(ply,dropt):
    v = 0   
    for x in ply:
        if dropt == x:
            v = dropt
        if dropt == x:
            ply.remove(x)
    return  ply
def checkcnum(pl):
    s = 0
    while s < len(pl):
        for b in pl:
            if b >= len(pl)*5:
                pl.remove(b)
                r = random.randint(0,(len(pl)+1)*5)
                if pl.__contains__(r) == False:
                    pl.append(r)
                else:
                    pl.append(random.randint(0,(len(pl)+1)*5))
        s += 1

    return pl
def processhplay(g,plays):
    if plays.__contains__(g) == False:
        plays.append(g)
    else:
        return False
    
    return plays

while True:
    try:
        i = int(input("Enter number of computer players: "))
        break
    except:
        print("Invalid entry, press enter to continue")


c = cnum(i)
print(c)

while True:
    try:
        o = int(input("Enter your guess: "))
        break
    except:
        print("Invalid entry, press enter to continue")



f = processhplay(o,c)
if f == False:
    while True:
        if f != False:
            c = f
            break
        else:
            try:
                o = int(input("Enter your a new guess"))
                f = processhplay(o,c)
                if f != False:
                    c = f
                    break
            except:
                print("Invalid entry, press enter to continue")


while True:
    w = 0
    t = 0
    m = 0
    for h in c:
        time.sleep(0.1)
        print("Player " + str(m + 1) + " guess was " + str(h)  )
        m += 1

        
    while c.__contains__(o) == True:
        try:
            hinp = int(input("Drop a number from 0 to 5: "))
            if hinp <= 5:
                t += hinp
                break
        except:
            print("Invalid entry, press enter to continue")


    for a in c:
        while w != len(c) - 1:
            wr = random.randint(0,5)
            print( "Player " + str(w + 1) + " drop is", wr)
            time.sleep(0.1)
            t += wr
            w += 1
    
    
    if  c.__contains__(o) == True:
        print("Your drop is " , hinp)
    j = 0
    for e in c:
        if e == t:
            print('Player ' + str(j + 1) + ' is safe!')
            j += 1
    p = processplay(c,t)
    m = 0
    print("The total drop is ",t)


    if len(p) == 1:
        print(p[0], 'is the losing number')
        break
    else:
        c = checkcnum(p)
        time.sleep(1)
        

