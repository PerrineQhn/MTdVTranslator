#!/bin/bash

# Usage: sh executeur.sh MTdVTranslator_QuestionX.py programmesTS/script.ts [arg3] [arg4]
# Exemple: sh executeur.sh MTdVTranslator_Question2.py programmesTS/truc.ts 14 20

# Vérifie que le script Python à utiliser est spécifié
if [ -z "$2" ]; then
    echo "Veuillez spécifier un fichier TS à traduire."
    exit 1
fi

# Vérifie que le fichier TS à traduire existe
if [ ! -f "$2" ]; then
    echo "Le fichier TS spécifié n'existe pas."
    exit 1
fi

# Récupère le nom du fichier TS, sans extension .ts ou .TS
tsFileName=$(basename "$2")
tsFileName="${tsFileName%.*}"

# Lance la traduction en redirigeant la sortie vers un fichier .py du même nom sans l'extension
if [ -z "$3" ]; then
    python3 "$1" "$2" > "programmesPY/${tsFileName}.py"
    # Exécute le fichier Python généré
    python3 "programmesPY/${tsFileName}.py"
elif [ -z "$4" ]; then
    python3 "$1" "$2" $3 > "programmesPY/${tsFileName}.py"
    # Exécute le fichier Python généré
    python3 "programmesPY/${tsFileName}.py" $3
else
    python3 "$1" "$2" $3 $4 > "programmesPY/${tsFileName}.py"
    # Exécute le fichier Python généré
    python3 "programmesPY/${tsFileName}.py" $3 $4
fi