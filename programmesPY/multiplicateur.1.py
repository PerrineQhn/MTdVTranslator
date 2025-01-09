import sys

# Initialisation du ruban avec 1000 cases à 0
ruban = [0] * 1000
X = len(ruban) // 2

def G():
    global X
    X -= 1 # Déplacement de la tête vers la gauche

def D():
    global X
    X += 1 # Déplacement de la tête vers la droite

def V1():
    ruban[X] = 1  # Écriture d'un 1 à la position courante

def V0():
    ruban[X] = 0  # Écriture d'un 0 à la position courante

# Initialisation de la première plage de 1
for i in range(3+1):
    ruban[X+i] = 1
# Initialisation de la seconde plage de 1 (séparée par 3 cases)
for i in range(3+1):
    ruban[X+3+3+i] = 1

# Extraction de la portion visible du ruban
r1 =''.join(map(str,ruban[500-35:500+35]))
# Création de la ligne de marqueur de position
r2 =[' '] * 100
r2[X-500+35] = 'X'  # Position de la tête
r2 = ''.join(r2)
print(r1)  # Affichage du contenu
print(r2)  # Affichage de la position

def boucle0():
    if ruban[X] == 0:
        0
    else:
        D()
        boucle0()
boucle0()
def boucle1():
    D()
    if ruban[X] == 1:
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
D()
V1()
G()
def boucle3():
    G()
    if ruban[X] == 0:
        0
    else:
        boucle3()
boucle3()
def boucle4():
    G()
    if ruban[X] == 1:
        0
    else:
        boucle4()
boucle4()
def boucle5():
    V0()
    G()
    if ruban[X] == 0:
        0
    else:
        D()
        def boucle6():
            D()
            if ruban[X] == 1:
                0
            else:
                boucle6()
        boucle6()
        def boucle7():
            D()
            if ruban[X] == 0:
                0
            else:
                boucle7()
        boucle7()
        G()
        def boucle8():
            V0()
            G()
            if ruban[X] == 0:
                0
            else:
                D()
                def boucle9():
                    D()
                    if ruban[X] == 1:
                        0
                    else:
                        boucle9()
                boucle9()
                def boucle10():
                    D()
                    if ruban[X] == 0:
                        0
                    else:
                        boucle10()
                boucle10()
                V1()
                def boucle11():
                    G()
                    if ruban[X] == 0:
                        0
                    else:
                        boucle11()
                boucle11()
                def boucle12():
                    G()
                    if ruban[X] == 1:
                        0
                    else:
                        boucle12()
                boucle12()
                boucle8()
        boucle8()
        D()
        V1()
        def boucle13():
            D()
            if ruban[X] == 1:
                0
            else:
                boucle13()
        boucle13()
        G()
        def boucle14():
            G()
            if ruban[X] == 1:
                0
            else:
                V1()
                boucle14()
        boucle14()
        def boucle15():
            G()
            if ruban[X] == 1:
                0
            else:
                boucle15()
        boucle15()
        boucle5()
boucle5()
def boucle16():
    D()
    if ruban[X] == 1:
        0
    else:
        boucle16()
boucle16()
def boucle17():
    V0()
    D()
    if ruban[X] == 0:
        0
    else:
        boucle17()
boucle17()
D()

# Extraction de la portion visible du ruban
r1 =''.join(map(str,ruban[500-35:500+35]))
# Création de la ligne de marqueur de position
r2 =[' '] * 100
r2[X-500+35] = 'X'  # Position de la tête
r2 = ''.join(r2)
print(r1)  # Affichage du contenu
print(r2)  # Affichage de la position

