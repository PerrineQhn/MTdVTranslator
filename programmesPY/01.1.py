import sys
sys.setrecursionlimit(2000)
def init_ruban(size, size2=0):
   return ([0] * 500) + ([1] * size) + ([0] * 2) + ([1] * size2) + ([0] * (1000 - size - size2 - 2 - 500))

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

def new_join(lst, index=0, result=""):
   if index == new_len(lst):
       return result
   return new_join(lst, index + 1, result + "{}".format(lst[index]))

def new_len(lst):
   if not lst:
       return 0
   return 1 + new_len(lst[1:])

ruban = [0] * 1000
X = new_len(ruban) // 2

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
    r1 =new_join(ruban[500-35:500+35])
    r2 =[' '] * 100
    r2[X-500+35] = 'X'
    r2 = new_join(r2)
    print(r1) # Affichage du contenu
    print(r2) # Affichage de la position
    global step
    if step > 0:
         input('Press Enter to continue')
         step -= 1
         boucle0()
    else:
         sys.exit()
    boucle0()
boucle0()
