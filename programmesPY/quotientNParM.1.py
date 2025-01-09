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

G()
G()
V1()
D()
def boucle0():
    D()
    if ruban[X] == 0:
        0
    else:
        boucle0()
boucle0()
def boucle1():
    D()
    if ruban[X] == 0:
        0
    else:
        boucle1()
boucle1()
V1()
def boucle2():
    G()
    if ruban[X] == 0:
        0
    else:
        boucle2()
boucle2()
D()
D()

r1 =''.join(map(str,ruban[500-35:500+35]))
r2 =[' '] * 100
r2[X-500+35] = 'X'
r2 = ''.join(r2)
print(r1)
print(r2)

def boucle3():
    def boucle4():
        D()
        if ruban[X] == 0:
            G()
            0
        else:
            G()
            V0()
            def boucle5():
                G()
                if ruban[X] == 1:
                    0
                else:
                    boucle5()
            boucle5()
            G()
            def boucle6():
                G()
                if ruban[X] == 0:
                    0
                else:
                    boucle6()
            boucle6()
            D()
            D()
            if ruban[X] == 0:
                G()
                V0()
                0
            else:
                G()
                V0()
                def boucle7():
                    D()
                    if ruban[X] == 0:
                        0
                    else:
                        boucle7()
                boucle7()
                D()
                D()
                def boucle8():
                    D()
                    if ruban[X] == 1:
                        0
                    else:
                        boucle8()
                boucle8()
                boucle4()
    boucle4()
    if ruban[X] == 0:
        0
    else:
        
        r1 =''.join(map(str,ruban[500-35:500+35]))
        r2 =[' '] * 100
        r2[X-500+35] = 'X'
        r2 = ''.join(r2)
        print(r1)
        print(r2)
        
        def boucle9():
            G()
            if ruban[X] == 1:
                0
            else:
                V1()
                boucle9()
        boucle9()
        G()
        def boucle10():
            G()
            if ruban[X] == 0:
                0
            else:
                boucle10()
        boucle10()
        def boucle11():
            G()
            if ruban[X] == 1:
                0
            else:
                boucle11()
        boucle11()
        def boucle12():
            G()
            if ruban[X] == 0:
                0
            else:
                boucle12()
        boucle12()
        V1()
        def boucle13():
            D()
            if ruban[X] == 0:
                0
            else:
                boucle13()
        boucle13()
        def boucle14():
            D()
            if ruban[X] == 1:
                0
            else:
                boucle14()
        boucle14()
        def boucle15():
            D()
            if ruban[X] == 0:
                0
            else:
                boucle15()
        boucle15()
        D()
        D()
        boucle3()
boucle3()

r1 =''.join(map(str,ruban[500-35:500+35]))
r2 =[' '] * 100
r2[X-500+35] = 'X'
r2 = ''.join(r2)
print(r1)
print(r2)

