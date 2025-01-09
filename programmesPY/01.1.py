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
            0
        else:
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
            0
        else:
            boucle2()
    boucle2()
    
    # Extraction de la portion visible du ruban
    r1 =''.join(map(str,ruban[500-35:500+35]))
    # Création de la ligne de marqueur de position
    r2 =[' '] * 100
    r2[X-500+35] = 'X'  # Position de la tête
    r2 = ''.join(r2)
    print(r1)  # Affichage du contenu
    print(r2)  # Affichage de la position
    
    global step
    if step > 0:
         input('Press Enter to continue')
         step -= 1
         boucle0()
    else:
         sys.exit()
    boucle0()
boucle0()
