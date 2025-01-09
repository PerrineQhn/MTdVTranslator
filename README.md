# Traducteur Machine de Turing de Del Vigna (MTdV) vers Python

## Description du Projet

Implémentation d'un traducteur de programmes écrits en Machine de Turing de Del Vigna (MTdV) vers Python, avec quatre variantes progressives ajoutant différentes contraintes sur le code Python généré.

```
├── MTdVTranslator_Question1.py    # Implémentation de base
├── MTdVTranslator_Question2.py    # Version avec return et variables locales
├── MTdVTranslator_Question3.py    # Version sans affectation ni variables locales
├── MTdVTranslator_Question4.py    # Version avec un seul argument par fonction
├── programmesTS/                  # Dossier des fichiers source MTdV
├── programmesPY/                  # Dossier des fichiers Python générés
└── executeur.sh                   # Script d'exécution automatisée
```

---

## Spécifications techniques

### Objectifs

1. Traduire les instructions de MTdV en Python tout en respectant les contraintes des différentes questions.
2. Générer des scripts Python fonctionnels capables de reproduire le comportement de la machine de Turing.

## Implémentation des Contraintes

#### Question 1 (Base)

- Pas de return dans les fonctions
- Solution : Utilisation de if/else pour la récursion
- Variables globales pour le ruban et curseur

#### Question 2 (Extensions)

- Return autorisé
- Variables locales permises
- Solution : Simplification du code avec return

#### Question 3 (Sans Affectation)

- Pas d'affectation ni variables globales
- Solution : Utilisation de listes mutables

#### Question 4 (Un Argument)

- Maximum un argument par fonction
- Solution : Variables globales pour ruban/curseur
  
## Modules

Le projet est divisé en plusieurs modules :

1. **Module d'ouverture des fichiers**
   - Charge le fichier `TS` (programme MTdV) en mémoire.
   - Vérifie la validité du fichier.

2. **Module d'extraction des données**
   - Analyse les instructions du fichier `TS`.
   - Identifie les commandes spécifiques de MTdV : `G`, `D`, `V1`, `V0`, etc.

3. **Module de génération**
   - Traduction des instructions en Python selon les contraintes spécifiées.
   - Génération d'un fichier Python respectant les contraintes des questions.

4. **Module d'exécution**
   - Exécute le fichier Python généré pour valider la traduction.

## Gestion des Données

### Structures de Données Principales

- Ruban : Liste Python de 1000 éléments
- Curseur :
  - Q1/Q2 : Variable globale X
  - Q3/Q4 : Liste mutable `[positon]`
- Code Généré : Liste de chaînes

---

## Librairies utilisées

1. **`sys`** : Gestion des arguments en ligne de commande.
2. **`os`** : Validation des fichiers et gestion des chemins.
3. **`argparse`** : Facilite la gestion des arguments en ligne de commande.
4. **`shutil`** *(optionnel)* : Pour organiser les fichiers traduits.

**Pourquoi ?**  
Ces librairies sont légères, robustes, et adaptées pour manipuler les fichiers et arguments nécessaires.

---

## Fonctionnalités

| **Fonction**                 | **Description**                                    | **Paramètres**                                                 | **Résultat attendu**                                                                 |
|-------------------------------|----------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `load_file(filepath)`         | Charge un fichier TS en mémoire.                  | `filepath`: chemin du fichier TS                              | Retourne le contenu sous forme de liste de lignes.                                   |
| `parse_instruction(lines)`    | Extrait les instructions MTdV.                    | `lines`: liste des lignes du fichier TS                       | Retourne une structure de données interprétable.                                     |
| `translate_instruction(instr)`| Traduit une instruction MTdV en Python.           | `instr`: chaîne de caractères                                 | Retourne le code Python équivalent.                                                 |
| `generate_python_file(path, code)` | Génère un fichier Python.                   | `path`: chemin de sortie<br>`code`: code Python généré        | Crée un fichier Python fonctionnel.                                                 |
| `execute_python_script(path, args)` | Exécute le script Python généré.           | `path`: chemin du fichier<br>`args`: arguments supplémentaires| Exécute le script et affiche les résultats.                                         |

---
## Utilitaire

### Script d'Exécution (executeur.sh)

```bash
sh executeur.sh MTdVTranslator_QuestionX.py script.ts [N1] [N2]
```

- Paramètres :
  - Traducteur à utiliser
  - Fichier source MTdV
  - Arguments optionnels en fonction du fichier `TS` pour l'initialisation du ruban

---

## Utilisation

### 1. Préparation

```bash
mkdir -p programmesPY
chmod +x executeur.sh
```

### 2. Exécution

Pour traduire et exécuter un fichier `TS` :

```bash
sh executeur.sh MTdVTranslator_QuestionX.py programmeTS/exemple.ts [arg1] [arg2]
```

Exemple :

```bash
sh executeur.sh MTdVTranslator_Question2.py programmesTS/addition.1.ts 14 20
```

### 3. Résultats

- Fichier Python généré dans `programmesPY/`
- Exécution automatique du programme traduit
