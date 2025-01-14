## Explicitation de la traduction des instructions MTdV en Python

### Question 1

1. Déplacement à gauche (G)

   - MTdV : G
   - Python : G()
   - Effet : Décrémente la position du curseur, X -= 1.

   ```python
   def G():
       global X
       X -= 1
   ```

2. Déplacement à droite (D)

   - MTdV : D
   - Python : D()
   - Effet : Incrémente la position du curseur, X += 1.

   ```python
   def D():
       global X
       X += 1
   ```

3. Écriture d’un 1 (V1)

   - MTdV : 1
   - Python : V1()
   - Effet : Place un 1 à l’emplacement courant, ruban[X] = 1.

   ```python
   def V1():
       ruban[X] = 1
   ```

4. Écriture d’un 0 (V0)

   - MTdV : 0
   - Python : V0()
   - Effet : Place un 0 à l’emplacement courant, ruban[X] = 0.

   ```python
   def V0():
       ruban[X] = 0
   ```

5. Affichage de l’état courant (I)

   - MTdV : I
   - Python :

   ```python
   r1 = ''.join(map(str, ruban[500-35:500+35]))
   r2 = [' '] * 100
   r2[X-500+35] = 'X'
   r2 = ''.join(r2)
   print(r1)
   print(r2)
   ```

   - Effet : Montre une portion du ruban et la position du curseur.

6. Pause du programme (P)

   - MTdV : P
   - Python :

   ```python
   global step
   if step > 0:
       input('Press Enter to continue')
       step -= 1
       boucle0()
   else:
       sys.exit()
   ```

   - Effet : Interrompt temporairement l’exécution selon la valeur de step.

7. Début d’une boucle (boucle)

   - MTdV : boucle
   - Python :

   ```python
   def boucleX():
   ```

   - Effet : Marque le début d’un bloc itératif, géré de façon récursive dans la fonction `boucleX`.

8. Début d’une condition (si)

   - MTdV : si (1) ou si (0)
   - Python :

   ```python
   if ruban[X] == 1:
   ```

   ou

   ```python
   if ruban[X] == 0:
   ```

   - Effet : Conditionne l’exécution selon la valeur lue sur le ruban.

9. Fin de boucle ou condition (fin)

   - MTdV : fin
   - Python :

   ```python
   0
   else:
   ```

   - Effet : Termine le bloc de boucle ou de condition et bascule vers la branche else: (fin de la structure récursive).

10. Clôture d’un bloc (})

    - MTdV : }
    - Python :

    ```python
    boucleX()
    ```

    - Effet : Relance la fonction associée à la boucle ou au bloc conditionnel.

## Question 2

La logique reste la même, mais l’arrêt de la récursivité se fait via return plutôt qu’un bloc `else:`. Il y a également l'ajout des fonctions `new_join()` pour remplacer l’utilisation explicite de `join()` dans les affichages, utilisé dans `I` et `new_len()` remplace `len()` pour calculer la longueur des listes de manière récursive.

1. Ajout des fonctions utilitaires

   1. Fonction `new_join()`

      - Utilisation : Remplace la méthode `join()` pour concaténer les éléments d’une liste en une chaîne de caractères.

      ```python
      def new_join(lst, index=0, result=""):
          if index == new_len(lst):
              return result
          return new_join(lst, index + 1, result + "{}".format(lst[index]))
      ```

   2. Fonction `new_len()`

      - Utilisation : Remplace la méthode `len()` pour calculer la longueur d’une liste de manière récursive.

      ```python
      def new_len(lst):
          if not lst:
              return 0
          return 1 + new_len(lst[1:])
      ```

       Avantage : Permet d’éviter l’utilisation d’itérations explicites, en respectant les contraintes du projet.

2. Affichage de l’état courant (I)

   - MTdV : I
   - Python :

   ```python
   r1 = new_join(ruban[500-35:500+35])
   r2 = [' '] * 100
   r2[X-500+35] = 'X'
   r2 = new_join(r2)
   print(r1)
   print(r2)
   ```

3. Début d’un bloc de boucle (boucle)

   - MTdV : boucle
   - Python :
     
   ```python
   def boucleX():
   ```

   - Particularité : `boucle_name` devient une liste simple (et non plus une liste de tuples), et `boucle_max_value` est employé pour générer des identifiants de boucles uniques.

4. Fin d’une boucle (fin)

   - MTdV : fin
   - Python :
     
   ```python
   return
   ```

   - Particularité : return met fin directement à la fonction récursive, alors que dans la version précédente, c’était géré autrement.

5. Clôture d’un bloc (})

   - MTdV : }
   - Python :
     
   ```python
   boucleX()
   ```

   - Particularité : On rappelle simplement la fonction `boucleX`. L’identifiant de boucle se récupère via `boucle_name`, puis la fonction adaptée est invoquée.

## Question 3

1. Déplacement à gauche (G)

   - MTdV : G
   - Python : G(X)
   - Effet : Décrémente la position du curseur, X -= 1.

   ```python
   def G(X):
       X.append(X[-1]-1)
       X.pop(0)
   ```

2. Déplacement à droite (D)

   - MTdV : D
   - Python : D(X)
   - Effet : Incrémente la position du curseur, X += 1.

   ```python
   def D(X):
       X.append(X[-1]+1)
       X.pop(0)
   ```

3. Écriture d’un 1 à la position du curseur (V1)

   - MTdV : 1
   - Python : V1(ruban, X)
   - Effet : Place un 1 à l’emplacement courant.

   ```python
   def V1(ruban, X):
       index = X[-1]
       ruban.pop(index)
       ruban.insert(index, 1)
   ```

4. Écriture d’un 0 à la position du curseur (V0)

   - MTdV : 0
   - Python : V0(ruban, X)
   - Effet : Place un 0 à l’emplacement courant.

   ```python
   def V0(ruban, X):
       index = X[-1]
       ruban.pop(index)
       ruban.insert(index, 0)
   ```

5. Affichage de l’état courant (I)

   - MTdV : I
   - Python :

   ```python
   print(new_join(ruban[500-35:500+35]))
   print(new_join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))
   ```

   - Effet : Montre une portion du ruban et la position du curseur.

6. Pause du programme (P)

   - MTdV : P
   - Python :

   ```python
   print(new_join(ruban[500-35:500+35]))")
   print(new_join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))
   input('Press Enter to continue')
   ```

   - Effet : Interrompt temporairement l’exécution et afficher une portion du ruban et la position du curseur. Appuyer sur ***Enter*** pour continuer l'exécution

7. Début d’une boucle (boucle)

   - MTdV : boucle
   - Python :

   ```python
   def boucleX(ruban, X):
   ```

   - Effet : Marque le début d’un bloc itératif, géré de façon récursive dans la fonction `boucleX`.

8. Début d’une condition (si)

   - MTdV : si (1) ou si (0)
   - Python :

   ```python
   if ruban[X[-1]] == 1:
   ```

   ou

   ```python
   if ruban[X[-1]] == 0:
   ```

   - Effet : Conditionne l’exécution selon la valeur lue sur le ruban.

9. Fin de boucle ou condition (fin)

   - MTdV : fin
   - Python :

   ```python
   return
   ```

   - Effet : Terminer directement la fonction récursive.

10. Clôture d’un bloc (})

    - MTdV : }
    - Python :

    ```python
    boucleX(ruban, X)
    ```

    - Effet : Relance la fonction associée à la boucle ou au bloc conditionnel.

## Question 4

La plupart du code reste identique au celui de la question 3 sauf les fonctions suivantes :

1. Écriture d’un 1 à la position du curseur (V1)

   - MTdV : 1
   - Python : V1()
   - Effet : Place un 1 à l’emplacement courant.

   ```python
   def V1():
       index = X[-1]
       ruban.pop(index)
       ruban.insert(index, 1)
   ```

2. Écriture d’un 0 à la position du curseur (V0)

   - MTdV : 0
   - Python : V0()
   - Effet : Place un 0 à l’emplacement courant.

   ```python
   def V0():
       index = X[-1]
       ruban.pop(index)
       ruban.insert(index, 0)
   ```

3. Début d’une boucle (boucle)

   - MTdV : boucle
   - Python :

   ```python
   def boucleX(ruban, X):
   ```

- Effet : Marque le début d’un bloc itératif, géré de façon récursive dans la fonction `boucleX`.

1. Clôture d’un bloc (})

   - MTdV : }
   - Python :

   ```python
   boucleX(ruban, X)
   ```

2. `new_join()`

- Integrétion de la fonction `helper()` qui gère la récursion.
  
```python
def new_join(lst):
    def helper(index):
        if index == new_len(lst):
            return ""
        return "{}".format(lst[index]) + helper(index + 1)
    return helper(0)
```
