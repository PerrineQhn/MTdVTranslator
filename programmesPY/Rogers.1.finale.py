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

for i in range(3+1):
    ruban[X+i] = 1
for i in range(4+1):
    ruban[X+3+3+i] = 1

r1 =''.join(map(str,ruban[500-35:500+35]))
r2 =[' '] * 100
r2[X-500+35] = 'X'
r2 = ''.join(r2)
print(r1)
print(r2)

if ruban[X] == 0:
    sys.exit()
V0()
def boucle0():
    
    r1 =''.join(map(str,ruban[500-35:500+35]))
    r2 =[' '] * 100
    r2[X-500+35] = 'X'
    r2 = ''.join(r2)
    print(r1)
    print(r2)
    
    D()
    if ruban[X] == 0:
        0
    else:
        V0()
        def boucle1():
            D()
            if ruban[X] == 0:
                0
            else:
                boucle1()
        boucle1()
        def boucle2():
            D()
            if ruban[X] == 0:
                0
            else:
                boucle2()
        boucle2()
        V1()
        D()
        V1()
        V1()
        def boucle3():
            G()
            if ruban[X] == 0:
                0
            else:
                boucle3()
        boucle3()
        def boucle4():
            G()
            if ruban[X] == 0:
                0
            else:
                boucle4()
        boucle4()
        boucle0()
boucle0()
D()

r1 =''.join(map(str,ruban[500-35:500+35]))
r2 =[' '] * 100
r2[X-500+35] = 'X'
r2 = ''.join(r2)
print(r1)
print(r2)

