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
for i in range(4+1):
    ruban[X+2+3+i] = 1
r1 =''.join(map(str,ruban[500-35:500+35]))
r2 =[' '] * 100
r2[X-500+35] = 'X'
r2 = ''.join(r2)
print(r1)
print(r2)
def boucle0():
    if ruban[X] == 0:
        return
    D()
    boucle0()
boucle0()
def boucle1():
    def boucle2():
        D()
        if ruban[X] == 1:
            return
        boucle2()
    boucle2()
    V0()
    D()
    if ruban[X] == 0:
        return
    def boucle3():
        G()
        if ruban[X] == 1:
            return
        boucle3()
    boucle3()
    D()
    V1()
    D()
    boucle1()
boucle1()
def boucle4():
    G()
    if ruban[X] == 1:
        return
    boucle4()
boucle4()
def boucle5():
    G()
    if ruban[X] == 0:
        return
    boucle5()
boucle5()
D()
r1 =''.join(map(str,ruban[500-35:500+35]))
r2 =[' '] * 100
r2[X-500+35] = 'X'
r2 = ''.join(r2)
print(r1)
print(r2)
