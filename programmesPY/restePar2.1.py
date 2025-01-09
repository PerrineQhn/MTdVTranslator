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
def boucle0():
    D()
    D()
    if ruban[X] == 0:
        return
    boucle0()
boucle0()
G()
G()
G()
def boucle1():
    if ruban[X] == 0:
        return
    V0()
    G()
    boucle1()
boucle1()
def boucle2():
    D()
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

