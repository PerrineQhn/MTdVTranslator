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

for i in range(5+1):
  ruban[X+i] = 1
def boucle0():
    D()
    V0()
    D()
    if ruban[X] == 0:
        0
    else:
        boucle0()
boucle0()

r1 =''.join(map(str,ruban[500-35:500+35]))
r2 =[' '] * 100
r2[X-500+35] = 'X'
r2 = ''.join(r2)
print(r1)
print(r2)

G()
def boucle1():
    G()
    
    r1 =''.join(map(str,ruban[500-35:500+35]))
    r2 =[' '] * 100
    r2[X-500+35] = 'X'
    r2 = ''.join(r2)
    print(r1)
    print(r2)
    
    def boucle2():
        G()
        if ruban[X] == 0:
            0
        else:
            boucle2()
    boucle2()
    G()
    if ruban[X] == 0:
        0
    else:
        D()
        V1()
        def boucle3():
            D()
            if ruban[X] == 0:
                0
            else:
                boucle3()
        boucle3()
        G()
        V0()
        boucle1()
boucle1()
D()
D()

r1 =''.join(map(str,ruban[500-35:500+35]))
r2 =[' '] * 100
r2[X-500+35] = 'X'
r2 = ''.join(r2)
print(r1)
print(r2)

