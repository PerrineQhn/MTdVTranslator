"""
Question 1.
Pour contourner l'impossibilité de l'utilisation de return, nous avons utilisé if et else.
Pour contourner l'impossibilité de l'utilisation de for, nous avons utilisé la récursivité pour gérer les boucles et les conditions.
"""

import sys


# Classe principale assurant la traduction d'un script MTdV vers un sous-ensemble Python
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
        Génère l'en-tête du programme Python avec:
        - L'initialisation du ruban (liste de 1000 cases)
        - La position initiale de la tête (au milieu du ruban)
        - Les fonctions de base de la MTdV:
            * G() : déplacement à gauche
            * D() : déplacement à droite
            * V1() : écriture d'un 1
            * V0() : écriture d'un 0
        """
        header = [
            "import sys",
            "",
            "# Initialisation du ruban avec 1000 cases à 0" "ruban = [0] * 1000",
            "X = len(ruban) // 2",
            "",
            "def G():",
            "    global X",
            "    X -= 1 # Déplacement de la tête vers la gauche",
            "",
            "def D():",
            "    global X",
            "    X += 1 # Déplacement de la tête vers la droite",
            "",
            "def V1():",
            "    ruban[X] = 1  # Écriture d'un 1 à la position courante",
            "",
            "def V0():",
            "    ruban[X] = 0  # Écriture d'un 0 à la position courante",
            "",
        ]
        self.code.extend(header)

    def generate_special(self, file):
        """
        Gère l'initialisation du ruban selon les arguments passés au script:
        - Sans argument: définit juste le nombre d'étapes par défaut
        - Un argument N1: initialise une plage de N1+1 cases à 1
        - Deux arguments N1,N2: initialise deux plages séparées de N1+1 et N2+1 cases à 1
        """
        args = len(sys.argv)
        # 0 .\MTdVTranslator.py
        # 1 .\XXX.TS
        # 2 N1
        # 3 N2

        if args == 2:
            # Définit le nombre d'étapes par défaut si un seul argument
            self.add_line("step = 14")
        elif args == 3:
            # Initialise le ruban avec des 1 sur une plage de taille x
            x = sys.argv[2]
            self.add_line("# Initialisation de la première plage de 1")
            self.add_line("for i in range({}+1):".format(x))
            self.add_line("  ruban[X+i] = 1")
        elif args == 4:
            # Initialise deux plages successives de 1 sur le ruban
            x = sys.argv[2]
            y = sys.argv[3]
            self.add_line("# Initialisation de la première plage de 1")
            self.add_line("for i in range({}+1):".format(x))
            self.add_line("    ruban[X+i] = 1")
            self.add_line(
                "# Initialisation de la seconde plage de 1 (séparée par 3 cases)"
            )
            self.add_line("for i in range({}+1):".format(y))
            self.add_line("    ruban[X+{}+3+i] = 1".format(x))

    def translate_lines(self, lines):
        """
        Traduit chaque ligne de code MTdV en instructions Python.
        Gère les commandes de base (G,D,0,1), l'affichage (I),
        les pauses (P), et les structures de contrôle (boucle, si).
        """
        for line in lines:
            # Ajout d'espaces avant parenthèses et accolades
            line = line.replace("}", " }")
            line = line.replace("(", " (")

            # Suppression des commentaires inline
            index = line.find("%")
            line = line[:index].strip() if index != -1 else line.strip()

            # Découpage de la ligne en tokens
            tokens = line.split()
            i = 0
            while i < len(tokens):
                if tokens[i] == "G":
                    # Avance à gauche
                    self.add_line("G()")

                elif tokens[i] == "D":
                    # Avance à droite
                    self.add_line("D()")

                elif tokens[i] == "1":
                    # Écrit 1 sur le ruban
                    self.add_line("V1()")

                elif tokens[i] == "0":
                    # Écrit 0 sur le ruban
                    self.add_line("V0()")

                elif tokens[i] == "I":
                    # Commande d'affichage du ruban
                    # Affiche une fenêtre de 70 cases autour de la position courante
                    self.add_line("")
                    self.add_line("# Extraction de la portion visible du ruban")
                    self.add_line("r1 =''.join(map(str,ruban[500-35:500+35]))")
                    self.add_line("# Création de la ligne de marqueur de position")
                    self.add_line("r2 =[' '] * 100")
                    self.add_line("r2[X-500+35] = 'X'  # Position de la tête")
                    self.add_line("r2 = ''.join(r2)")
                    self.add_line("print(r1)  # Affichage du contenu")
                    self.add_line("print(r2)  # Affichage de la position")
                    self.add_line("")

                elif tokens[i] == "P":
                    # Met le programme en pause selon la valeur de step
                    self.add_line("global step")
                    self.add_line("if step > 0:")
                    self.add_line("     input('Press Enter to continue')")
                    self.add_line("     step -= 1")
                    self.add_line("     boucle0()")
                    self.add_line("else:")
                    self.add_line("     sys.exit()")

                elif tokens[i] == "boucle":
                    # Début d'un bloc de boucle
                    self.boucle_name.append(
                        (self.boucle_max_value, self.current_indent)
                    )
                    self.boucle_max_value += 1
                    self.add_line("def boucle{}():".format(self.boucle_name[-1][0]))
                    self.boucle_pos += 1
                    self.current_indent += 1

                elif tokens[i] == "si":
                    # Début d'une condition
                    self.if_count += 1
                    i += 1
                    if tokens[i] == "(1)":
                        self.add_line(
                            "if ruban[X] == 1:"
                        )  # Test si la case courante contient un 1
                        self.current_indent += 1

                    elif tokens[i] == "(0)":
                        self.add_line(
                            "if ruban[X] == 0:"
                        )  # Test si la case courante contient un 0
                        self.current_indent += 1

                elif tokens[i] == "fin":
                    # Fin de boucle
                    if self.boucle_pos > 0:
                        self.add_line("0")
                        self.current_indent -= 1
                        self.add_line("else:")
                        self.else_count += 1
                        self.current_indent += 1

                elif tokens[i] == "}":
                    # Clôture d'un bloc boucle ou condition
                    if self.if_count > 0:
                        self.if_count -= 1
                        if self.boucle_pos == 0:
                            self.add_line("sys.exit()")
                            self.current_indent -= 1

                    elif self.boucle_pos > 0:
                        # Appel récursif de la boucle
                        self.add_line("boucle{}()".format(self.boucle_name[-1][0]))
                        self.else_count -= 1
                        self.current_indent -= 1

                        self.current_indent = self.boucle_name[-1][-1]
                        self.add_line("boucle{}()".format(self.boucle_name[-1][0]))
                        self.boucle_name.pop()
                        self.boucle_pos -= 1
                i += 1


if __name__ == "__main__":
    translator = MTDVTranslator()
    print(translator.translate_file(sys.argv[1]))
    translator.translate_file(sys.argv[1])
