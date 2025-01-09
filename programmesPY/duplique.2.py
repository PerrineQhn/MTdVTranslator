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

for i in range(2+1):
  ruban[X+i] = 1
if ruban[X] == 0:
    sys.exit()
def boucle0():
    D()
    if ruban[X] == 0:
        return
    boucle0()
boucle0()
D()
def boucle1():
    V1()
    def boucle2():
        G()
        if ruban[X] == 0:
            return
        boucle2()
    boucle2()
    def boucle3():
        G()
        if ruban[X] == 1:
            return
        boucle3()
    boucle3()
    G()
    
    r1 =''.join(map(str,ruban[500-35:500+35]))
    r2 =[' '] * 100
    r2[X-500+35] = 'X'
    r2 = ''.join(r2)
    print(r1)
    print(r2)
    
    if ruban[X] == 0:
        return
    D()
    V0()
    def boucle4():
        D()
        if ruban[X] == 1:
            return
        boucle4()
    boucle4()
    def boucle5():
        D()
        if ruban[X] == 0:
            return
        boucle5()
    boucle5()
    boucle1()
boucle1()
D()
def boucle6():
    D()
    if ruban[X] == 1:
        return
    V1()
    boucle6()
boucle6()
G()
V0()
D()

r1 =''.join(map(str,ruban[500-35:500+35]))
r2 =[' '] * 100
r2[X-500+35] = 'X'
r2 = ''.join(r2)
print(r1)
print(r2)

