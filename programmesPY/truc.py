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
for i in range(2+1):
    ruban[X+i] = 1
# Initialisation de la seconde plage de 1 (séparée par 3 cases)
for i in range(3+1):
    ruban[X+2+3+i] = 1

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
    def boucle2():
        D()
        if ruban[X] == 1:
            0
        else:
            
            # Extraction de la portion visible du ruban
            r1 =''.join(map(str,ruban[500-35:500+35]))
            # Création de la ligne de marqueur de position
            r2 =[' '] * 100
            r2[X-500+35] = 'X'  # Position de la tête
            r2 = ''.join(r2)
            print(r1)  # Affichage du contenu
            print(r2)  # Affichage de la position
            
            boucle2()
    boucle2()
    V0()
    D()
    if ruban[X] == 0:
        0
    else:
        def boucle3():
            G()
            if ruban[X] == 1:
                0
            else:
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
        0
    else:
        boucle4()
boucle4()
def boucle5():
    G()
    if ruban[X] == 0:
        0
    else:
        boucle5()
boucle5()
D()

# Extraction de la portion visible du ruban
r1 =''.join(map(str,ruban[500-35:500+35]))
# Création de la ligne de marqueur de position
r2 =[' '] * 100
r2[X-500+35] = 'X'  # Position de la tête
r2 = ''.join(r2)
print(r1)  # Affichage du contenu
print(r2)  # Affichage de la position

