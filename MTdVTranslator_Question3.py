"""
Question 3.
Pour contourner l'impossibilité de l'utilisation de for, nous avons utilisé la récursivité pour gérer les boucles et les conditions.
"""

import sys


class MTDVTranslator:
    def __init__(self):
        """
        Initialise les variables nécessaires à la traduction.
        """
        # Position et informations sur les boucles
        self.boucle_pos = 0
        self.boucle_name = []
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
        """
        return "    " * self.current_indent

    def add_line(self, line):
        """
        Ajoute une ligne de code avec l'indentation appropriée.
        """
        self.code.append(self.indent() + line)

    def translate_file(self, filename):
        """
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
        Ajoute les définitions des instructions et les variables de base telles que le ruban et les déplacements.
        G() : Déplacement à gauche
        D() : Déplacement à droite
        V1() : Écriture d'un 1 sur le ruban
        V0() : Écriture d'un 0 sur le ruban
        """
        header = [
            "import sys",
            "def init_ruban(size, offset1=0, size2=0):",
            "   return ([0] * offset1) + ([0] * 500) + ([1] * size) + ([0] * 2) + ([1] * size2) + ([0] * (1000 - offset1 - size - size2 - 2 - 500))",
            "def G(X):",
            "    X.append(X[-1]-1)",
            "    X.pop(0)",
            "",
            "def D(X):",
            "    X.append(X[-1]+1)",
            "    X.pop(0)",
            "",
            "def V1(ruban, X):",
            "    index = X[-1]",
            "    ruban[-1].pop(index)",
            "    ruban[-1].insert(index, 1)",
            "",
            "def V0(ruban, X):",
            "    index = X[-1]",
            "    ruban[-1].pop(index)",
            "    ruban[-1].insert(index, 0)",
            "",
        ]
        self.code.extend(header)

    def generate_special(self, file):
        """
        Gère le traitement des arguments passés au script pour construire le ruban.
        """
        args = len(sys.argv)
        # 0 .\MTdVTranslator.py
        # 1 .\XXX.TS
        # 2 N1
        # 3 N2

        if args == 2:
            # Définit le nombre d'étapes par défaut si un seul argument
            self.add_line("ruban = [init_ruban(0)]")
            self.add_line("X = [len(ruban[-1]) // 2]")
        elif args == 3:
            # Initialise le ruban avec des 1 sur une plage de taille x
            self.add_line("ruban = init_ruban(int(sys.argv[1]), size2=0)")
            self.add_line("X = [len(ruban[-1]) // 2]")
        elif args == 4:
            # Initialise deux plages successives de 1 sur le ruban
            self.add_line("ruban = [init_ruban(int(sys.argv[1]), size2=int(sys.argv[2]))]")
            self.add_line("X = [len(ruban[-1]) // 2]")

    def translate_lines(self, lines):
        """
        Interprète chaque ligne et génère les instructions Python associées.
        """
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
                    # Avance à gauche
                    self.add_line("G(X)")

                elif tokens[i] == "D":
                    # Avance à droite
                    self.add_line("D(X)")

                elif tokens[i] == "1":
                    # Écrit 1 sur le ruban
                    self.add_line("V1(ruban, X)")

                elif tokens[i] == "0":
                    # Écrit 0 sur le ruban
                    self.add_line("V0(ruban, X)")

                elif tokens[i] == "I":
                    # Affiche l'état courant du ruban
                    self.add_line("print(''.join(map(str,ruban[-1][500-35:500+35])))")
                    self.add_line("print(''.join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))")

                elif tokens[i] == "P":
                    # Met le programme en pause
                    # Affiche l'état courant du ruban
                    self.add_line("print(''.join(map(str,ruban[-1][500-35:500+35])))")
                    self.add_line("print(''.join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))")
                    self.add_line("input('Press Enter to continue')")

                elif tokens[i] == "boucle":
                    # Début d'un bloc de boucle
                    self.boucle_name.append(self.boucle_max_value)
                    self.boucle_max_value += 1
                    self.add_line("def boucle{}(ruban, X):".format(self.boucle_name[-1]))
                    self.boucle_pos += 1
                    self.current_indent += 1

                elif tokens[i] == "si":
                    # Début d'une condition
                    self.if_count += 1
                    i += 1
                    if tokens[i] == "(1)":
                        self.add_line("if ruban[-1][X[-1]] == 1:")
                        self.current_indent += 1

                    elif tokens[i] == "(0)":
                        self.add_line("if ruban[-1][X[-1]] == 0:")
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
                        self.add_line("return boucle{}(ruban, X)".format(self.boucle_name[-1]))
                        self.current_indent -= 1
                        self.add_line("boucle{}(ruban, X)".format(self.boucle_name[-1]))
                        self.boucle_name.pop()
                        self.boucle_pos -= 1
                i += 1
        self.current_indent = 0
        self.add_line("except IndexError:")
        self.current_indent = 1
        self.add_line("print('Ruban atteint à la fin, programme terminé')")
        self.add_line("sys.exit(1)")


if __name__ == "__main__":
    translator = MTDVTranslator()
    print(translator.translate_file(sys.argv[1]))
    translator.translate_file(sys.argv[1])
