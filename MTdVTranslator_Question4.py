"""
Question 4.
"les fonctions ne peuvent avoir au plus qu'un unique argument"
"""

import sys


class MTDVTranslator:
    def __init__(self):
        """
        Initialise les variables nécessaires à la traduction.
        """
        # Compteur pour la position courante des boucles
        self.boucle_pos = 0
        # Stocke les noms des boucles, leur position et leur indentation
        self.boucle_name = []
        # Compteur pour nommer les boucles
        self.boucle_max_value = 0

        # Compteurs pour conditions
        self.if_count = 0
        self.else_count = 0

        # Indentation courante
        self.current_indent = 0

        # Stockage du code généré
        self.code = []

    def indent(self):
        """
        Gère l'indentation selon self.current_indent.
        Retourne le nombre approprié d'espaces selon le niveau d'imbrication.
        """
        return "    " * self.current_indent

    def add_line(self, line):
        """
        Ajoute une ligne de code avec l'indentation appropriée.
        """
        self.code.append(self.indent() + line)

    def translate_file(self, filename):
        """
        Traduit le script MTdV en Python.
        Lit le fichier, filtre les lignes et lance la génération du script Python.
        """
        with open(filename, "r", encoding="latin-1") as f:
            content = f.read()
        lines = []
        # Gestion des lignes vides et des commentaires
        for line in content.split("\n"):
            line = line.strip()
            if not line or line.startswith("%") or line == "#":
                continue
            lines.append(line)
        # Ajout l'en-tête, l'initialisation spéciale et traduit le contenu
        self.generate_header()
        self.generate_special(filename)
        self.translate_lines(lines)
        return "\n".join(self.code)

    def generate_header(self):
        """
        Génère les fonctions de base pour la Machine de Turing:
        - init_ruban(): Crée un ruban avec des plages de 1 selon les paramètres
        - G(X): Déplace le curseur à gauche en modifiant la liste X
        - D(X): Déplace le curseur à droite en modifiant la liste X
        - V1(ruban, X): Écrit un 1 à la position courante
        - V0(ruban, X): Écrit un 0 à la position courante

        Note: Toutes les modifications se font via des opérations sur des listes
        pour éviter les affectations directes.
        """
        header = [
            "import sys",
            "",
            "# Fonction d'initialisation du ruban avec gestion des arguments",
            "def init_ruban(size):",
            "   if sys.argv[2]:",
            "       return ([0] * 500) + ([1] * size) + ([0] * 2) + ([1] * int(sys.argv[2])) + ([0] * (1000 - size - int(sys.argv[2]) - 2 - 500))",
            "   else:",
            "       return ([0] * 500) + ([1] * size) + ([0] * 2) + ([0] * (1000 - size - 2 - 500))",
            "# Déplacement à gauche via modifications de liste",
            "def G(X):",
            "    X.append(X[-1]-1)",
            "    X.pop(0)",
            "",
            "# Déplacement à droite via modifications de liste",
            "def D(X):",
            "    X.append(X[-1]+1)",
            "    X.pop(0)",
            "",
            "# Écriture d'un 1 via pop/insert pour éviter l'affectation",
            "def V1():",
            "    index = X[-1]",
            "    ruban.pop(index)",
            "    ruban.insert(index, 1)",
            "",
            "# Écriture d'un 0 via pop/insert pour éviter l'affectation",
            "def V0():",
            "    index = X[-1]",
            "    ruban.pop(index)",
            "    ruban.insert(index, 0)",
            "",
        ]
        self.code.extend(header)

    def generate_special(self, file):
        """
        Gère l'initialisation du ruban selon les arguments passés au script:
        - Sans argument: définit juste le nombre d'étapes par défaut
        - Un argument N1: initialise une plage de N1+1 cases à 1
        - Deux arguments N1,N2: initialise deux plages séparées de N1+1 et N2+1 cases à 1

        Note: X est initialisé comme une liste à un élément pour permettre sa modification sans affectation.
        """
        args = len(sys.argv)
        # 0 .\MTdVTranslator.py
        # 1 .\XXX.TS
        # 2 N1
        # 3 N2

        if args == 2:
            # Définit le nombre d'étapes par défaut si un seul argument
            self.add_line("ruban = init_ruban(0)")
            self.add_line("X = [len(ruban) // 2]")
        elif args == 3:
            # Initialise le ruban avec des 1 sur une plage de taille x
            self.add_line("ruban = init_ruban(int(sys.argv[1]))")
            self.add_line("X = [len(ruban) // 2]")
        elif args == 4:
            # Initialise deux plages successives de 1 sur le ruban
            self.add_line("ruban = init_ruban(int(sys.argv[1]))")
            self.add_line("X = [len(ruban) // 2]")

    def translate_lines(self, lines):
        """
        Traduit chaque ligne de code MTdV en instructions Python.
        Gère les commandes de base (G,D,0,1), l'affichage (I),
        les pauses (P), et les structures de contrôle (boucle, si).
        Utilise un bloc try/except pour gérer proprement la sortie du
        programme quand le curseur sort des limites du ruban.
        """
        # Protection contre les dépassements de ruban
        self.add_line("try:")
        self.current_indent = 1
        for line in lines:
            # Ajout d'espaces avant parenthèses et accolades
            line = line.replace("}", " }")
            line = line.replace("(", " (")

            # Suppression des commentaires
            index = line.find("%")
            line = line[:index].strip() if index != -1 else line.strip()

            # Découpage de la ligne en tokens
            tokens = line.split()
            i = 0
            while i < len(tokens):
                if tokens[i] == "G":
                    # Déplacement gauche via liste mutable
                    self.add_line("G(X)")

                elif tokens[i] == "D":
                    # Déplacement droite via liste mutable
                    self.add_line("D(X)")

                elif tokens[i] == "1":
                    # Ecrit 1 sur le ruban via pop/insert
                    self.add_line("V1()")

                elif tokens[i] == "0":
                    # Ecrit 0 sur le ruban via pop/insert
                    self.add_line("V0()")

                elif tokens[i] == "I":
                    # Affiche l'état courant du ruban et la position du curseur
                    self.add_line("print(''.join(map(str,ruban[500-35:500+35])))")
                    self.add_line(
                        "print(''.join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))"
                    )

                elif tokens[i] == "P":
                    # Met le programme en pause
                    # Affiche l'état courant du ruban et la position du curseur
                    self.add_line("print(''.join(map(str,ruban[500-35:500+35])))")
                    self.add_line(
                        "print(''.join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))"
                    )
                    self.add_line("input('Press Enter to continue')")

                elif tokens[i] == "boucle":
                    # Début d'un bloc de boucle
                    self.boucle_name.append(self.boucle_max_value)
                    self.boucle_max_value += 1
                    self.add_line("def boucle{}():".format(self.boucle_name[-1]))
                    self.boucle_pos += 1
                    self.current_indent += 1

                elif tokens[i] == "si":
                    # Début d'une condition
                    self.if_count += 1
                    i += 1
                    if tokens[i] == "(1)":
                        # Test si la case courante est égale à 1
                        self.add_line("if ruban[X[-1]] == 1:")
                        self.current_indent += 1

                    elif tokens[i] == "(0)":
                        # Test si la case courante est égale à 0
                        self.add_line("if ruban[X[-1]] == 0:")
                        self.current_indent += 1

                elif tokens[i] == "fin":
                    # Fin d'une boucle
                    if self.boucle_pos > 0:
                        self.add_line("return")
                        self.current_indent -= 1

                elif tokens[i] == "}":
                    # Clôture d'un bloc boucle ou condition
                    if self.if_count > 0:
                        self.if_count -= 1
                        if self.boucle_pos == 0:
                            self.add_line("sys.exit()")
                            self.current_indent -= 1

                    elif self.boucle_pos > 0:
                        self.add_line("return boucle{}()".format(self.boucle_name[-1]))
                        self.current_indent -= 1
                        self.add_line("boucle{}()".format(self.boucle_name[-1]))
                        self.boucle_name.pop()
                        self.boucle_pos -= 1
                i += 1

        # Gestion des erreurs de limite de ruban
        self.current_indent = 0
        self.add_line("except IndexError:")
        self.current_indent = 1
        self.add_line("print('Ruban atteint à la fin, programme terminé')")
        self.add_line("sys.exit(1)")


if __name__ == "__main__":
    translator = MTDVTranslator()
    print(translator.translate_file(sys.argv[1]))
    translator.translate_file(sys.argv[1])
