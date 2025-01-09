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
def boucle0():
    D()
    V0()
    D()
    if ruban[X] == 0:
        0
    else:
        boucle0()
boucle0()

# Extraction de la portion visible du ruban
r1 =''.join(map(str,ruban[500-35:500+35]))
# Création de la ligne de marqueur de position
r2 =[' '] * 100
r2[X-500+35] = 'X'  # Position de la tête
r2 = ''.join(r2)
print(r1)  # Affichage du contenu
print(r2)  # Affichage de la position

G()
def boucle1():
    G()
    
    # Extraction de la portion visible du ruban
    r1 =''.join(map(str,ruban[500-35:500+35]))
    # Création de la ligne de marqueur de position
    r2 =[' '] * 100
    r2[X-500+35] = 'X'  # Position de la tête
    r2 = ''.join(r2)
    print(r1)  # Affichage du contenu
    print(r2)  # Affichage de la position
    
    def boucle2():
        G()
        if ruban[X] == 0:
            0
        else:
            boucle2()
    boucle2()
    G()
    if ruban[X] == 0:
        0
    else:
        D()
        V1()
        def boucle3():
            D()
            if ruban[X] == 0:
                0
            else:
                boucle3()
        boucle3()
        G()
        V0()
        boucle1()
boucle1()
D()
D()

# Extraction de la portion visible du ruban
r1 =''.join(map(str,ruban[500-35:500+35]))
# Création de la ligne de marqueur de position
r2 =[' '] * 100
r2[X-500+35] = 'X'  # Position de la tête
r2 = ''.join(r2)
print(r1)  # Affichage du contenu
print(r2)  # Affichage de la position

