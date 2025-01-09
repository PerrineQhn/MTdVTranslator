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
def boucle0():
    boucle0()
boucle0()
