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
def boucle0():
    boucle0()
boucle0()
