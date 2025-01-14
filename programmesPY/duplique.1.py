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

# Initialisation de la première plage de 1
for i in range(2+1):
  ruban[X+i] = 1
r1 =new_join(ruban[500-35:500+35])
r2 =[' '] * 100
r2[X-500+35] = 'X'
r2 = new_join(r2)
print(r1) # Affichage du contenu
print(r2) # Affichage de la position
if ruban[X] == 0:
    sys.exit()
def boucle0():
    if ruban[X] == 0:
        return
    D()
    boucle0()
boucle0()
D()
r1 =new_join(ruban[500-35:500+35])
r2 =[' '] * 100
r2[X-500+35] = 'X'
r2 = new_join(r2)
print(r1) # Affichage du contenu
print(r2) # Affichage de la position
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
    r1 =new_join(ruban[500-35:500+35])
    r2 =[' '] * 100
    r2[X-500+35] = 'X'
    r2 = new_join(r2)
    print(r1) # Affichage du contenu
    print(r2) # Affichage de la position
    G()
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
r1 =new_join(ruban[500-35:500+35])
r2 =[' '] * 100
r2[X-500+35] = 'X'
r2 = new_join(r2)
print(r1) # Affichage du contenu
print(r2) # Affichage de la position
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
r1 =new_join(ruban[500-35:500+35])
r2 =[' '] * 100
r2[X-500+35] = 'X'
r2 = new_join(r2)
print(r1) # Affichage du contenu
print(r2) # Affichage de la position
