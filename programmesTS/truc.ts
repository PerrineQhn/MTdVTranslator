% les nombres doivent �tre s�par�s par un moins un 0

I
                                                         %  00111001111100
                                                         %    X
% d�placement de l'oeil � l'extr�mit� droite du 1er nombre
boucle 
  si (0) fin }
  D
}
                                                         %  00111001111100
                                                         %       X
% l'oeil est sur un 0
boucle
  boucle 
    D
    si (1) fin }
    I
  }

                                                         %  00111001111100
                                                         %         X

  % l'oeil est sur le b�ton le plus � gauche du 2nd nombre
  % remplacement par un 0
  0
                                                         %  00111000111100
                                                         %         X

  % �tait-ce le dernier b�ton du 2nd nombre ? si oui, arr�t de la boucle
  D
  si (0) fin }
  % ajout d'un b�ton � la fin du 1er nombre
  boucle 
    G
    si (1) fin }
  }
  D
  1
                                                         %  00111100111100
                                                         %       X

  % positionnement de l'oeil sur le premier 0 qui suit le premier nombre
  D
                                                         %  00111100111100
                                                         %       X
} 

% positionnement de l'oeil au d�but du r�sultat
boucle 
  G
  si (1) fin }
}
boucle 
  G
  si (0) fin }
}
D

I

#