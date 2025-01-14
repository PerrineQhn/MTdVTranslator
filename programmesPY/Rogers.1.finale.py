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
for i in range(2+1):
    ruban[X+2+3+i] = 1

# Extraction de la portion visible du ruban
r1 =''.join(map(str,ruban[500-35:500+35]))
# Création de la ligne de marqueur de position
r2 =[' '] * 100
r2[X-500+35] = 'X'  # Position de la tête
r2 = ''.join(r2)
print(r1)  # Affichage du contenu
print(r2)  # Affichage de la position

if ruban[X] == 0:
    sys.exit()
V0()
def boucle0():
    
    # Extraction de la portion visible du ruban
    r1 =''.join(map(str,ruban[500-35:500+35]))
    # Création de la ligne de marqueur de position
    r2 =[' '] * 100
    r2[X-500+35] = 'X'  # Position de la tête
    r2 = ''.join(r2)
    print(r1)  # Affichage du contenu
    print(r2)  # Affichage de la position
    
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

# Extraction de la portion visible du ruban
r1 =''.join(map(str,ruban[500-35:500+35]))
# Création de la ligne de marqueur de position
r2 =[' '] * 100
r2[X-500+35] = 'X'  # Position de la tête
r2 = ''.join(r2)
print(r1)  # Affichage du contenu
print(r2)  # Affichage de la position

