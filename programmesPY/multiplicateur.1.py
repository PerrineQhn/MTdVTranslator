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
for i in range(3+1):
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
    D()
    if ruban[X] == 1:
        return
    boucle1()
boucle1()
def boucle2():
    D()
    if ruban[X] == 0:
        return
    boucle2()
boucle2()
D()
V1()
G()
def boucle3():
    G()
    if ruban[X] == 0:
        return
    boucle3()
boucle3()
def boucle4():
    G()
    if ruban[X] == 1:
        return
    boucle4()
boucle4()
def boucle5():
    V0()
    G()
    if ruban[X] == 0:
        return
    D()
    def boucle6():
        D()
        if ruban[X] == 1:
            return
        boucle6()
    boucle6()
    def boucle7():
        D()
        if ruban[X] == 0:
            return
        boucle7()
    boucle7()
    G()
    def boucle8():
        V0()
        G()
        if ruban[X] == 0:
            return
        D()
        def boucle9():
            D()
            if ruban[X] == 1:
                return
            boucle9()
        boucle9()
        def boucle10():
            D()
            if ruban[X] == 0:
                return
            boucle10()
        boucle10()
        V1()
        def boucle11():
            G()
            if ruban[X] == 0:
                return
            boucle11()
        boucle11()
        def boucle12():
            G()
            if ruban[X] == 1:
                return
            boucle12()
        boucle12()
        boucle8()
    boucle8()
    D()
    V1()
    def boucle13():
        D()
        if ruban[X] == 1:
            return
        boucle13()
    boucle13()
    G()
    def boucle14():
        G()
        if ruban[X] == 1:
            return
        V1()
        boucle14()
    boucle14()
    def boucle15():
        G()
        if ruban[X] == 1:
            return
        boucle15()
    boucle15()
    boucle5()
boucle5()
def boucle16():
    D()
    if ruban[X] == 1:
        return
    boucle16()
boucle16()
def boucle17():
    V0()
    D()
    if ruban[X] == 0:
        return
    boucle17()
boucle17()
D()

r1 =''.join(map(str,ruban[500-35:500+35]))
r2 =[' '] * 100
r2[X-500+35] = 'X'
r2 = ''.join(r2)
print(r1)
print(r2)

