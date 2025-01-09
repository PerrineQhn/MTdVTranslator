import sys

ruban = [0] * 1000
X = len(ruban) // 2

def G():
    global X
    X -= 1

def D():
    global X
    X += 1

def V1():
    ruban[X] = 1

def V0():
    ruban[X] = 0

step = 14
G()
V1()
G()
V1()
G()
V0()
G()
V1()
G()
V1()
def boucle0():
    V0()
    G()
    V1()
    G()
    V1()
    def boucle1():
        D()
        D()
        if ruban[X] == 1:
            return
        boucle1()
    boucle1()
    V0()
    D()
    V1()
    D()
    V1()
    def boucle2():
        G()
        G()
        if ruban[X] == 1:
            return
        boucle2()
    boucle2()
    
    r1 =''.join(map(str,ruban[500-35:500+35]))
    r2 =[' '] * 100
    r2[X-500+35] = 'X'
    r2 = ''.join(r2)
    print(r1)
    print(r2)
    
    global step
    if step > 0:
         input('Press Enter to continue')
         step -= 1
         boucle0()
    else:
         sys.exit()
    boucle0()
boucle0()
