import sys
def init_ruban(size, offset1=0, size2=0):
   return ([0] * offset1) + ([0] * 500) + ([1] * size) + ([0] * 2) + ([1] * size2) + ([0] * (1000 - offset1 - size - size2 - 2 - 500))
def G(X):
    return X - 1

def D(X):
    return X + 1

def V1(ruban, X):
    return ruban[:X] + [1] + ruban[X + 1:]

def V0(ruban, X):
    return ruban[:X] + [0] + ruban[X + 1:]

ruban = init_ruban(int(sys.argv[1]), size2=int(sys.argv[2]))
X = len(ruban) // 2
try:
    print(''.join(map(str,ruban[500-35:500+35])))
    print(''.join([' ']*(X-500+35) + ['X'] + [' ']*(100-(X-500+35)-1)))
    X = G(X)
    X = G(X)
    ruban = V1(ruban, X)
    X = D(X)
    def boucle0(ruban, X):
        X = D(X)
        if ruban[X] == 0:
            return ruban, X
        return boucle0(ruban, X)
    ruban, X = boucle0(ruban, X)
    def boucle1(ruban, X):
        X = D(X)
        if ruban[X] == 0:
            return ruban, X
        return boucle1(ruban, X)
    ruban, X = boucle1(ruban, X)
    ruban = V1(ruban, X)
    def boucle2(ruban, X):
        X = G(X)
        if ruban[X] == 0:
            return ruban, X
        return boucle2(ruban, X)
    ruban, X = boucle2(ruban, X)
    X = D(X)
    X = D(X)
    print(''.join(map(str,ruban[500-35:500+35])))
    print(''.join([' ']*(X-500+35) + ['X'] + [' ']*(100-(X-500+35)-1)))
    def boucle3(ruban, X):
        def boucle4(ruban, X):
            X = D(X)
            if ruban[X] == 0:
                X = G(X)
                return ruban, X
            X = G(X)
            ruban = V0(ruban, X)
            def boucle5(ruban, X):
                X = G(X)
                if ruban[X] == 1:
                    return ruban, X
                return boucle5(ruban, X)
            ruban, X = boucle5(ruban, X)
            X = G(X)
            def boucle6(ruban, X):
                X = G(X)
                if ruban[X] == 0:
                    return ruban, X
                return boucle6(ruban, X)
            ruban, X = boucle6(ruban, X)
            X = D(X)
            X = D(X)
            if ruban[X] == 0:
                X = G(X)
                ruban = V0(ruban, X)
                return ruban, X
            X = G(X)
            ruban = V0(ruban, X)
            def boucle7(ruban, X):
                X = D(X)
                if ruban[X] == 0:
                    return ruban, X
                return boucle7(ruban, X)
            ruban, X = boucle7(ruban, X)
            X = D(X)
            X = D(X)
            def boucle8(ruban, X):
                X = D(X)
                if ruban[X] == 1:
                    return ruban, X
                return boucle8(ruban, X)
            ruban, X = boucle8(ruban, X)
            return boucle4(ruban, X)
        ruban, X = boucle4(ruban, X)
        if ruban[X] == 0:
            return ruban, X
        print(''.join(map(str,ruban[500-35:500+35])))
        print(''.join([' ']*(X-500+35) + ['X'] + [' ']*(100-(X-500+35)-1)))
        def boucle9(ruban, X):
            X = G(X)
            if ruban[X] == 1:
                return ruban, X
            ruban = V1(ruban, X)
            return boucle9(ruban, X)
        ruban, X = boucle9(ruban, X)
        X = G(X)
        def boucle10(ruban, X):
            X = G(X)
            if ruban[X] == 0:
                return ruban, X
            return boucle10(ruban, X)
        ruban, X = boucle10(ruban, X)
        def boucle11(ruban, X):
            X = G(X)
            if ruban[X] == 1:
                return ruban, X
            return boucle11(ruban, X)
        ruban, X = boucle11(ruban, X)
        def boucle12(ruban, X):
            X = G(X)
            if ruban[X] == 0:
                return ruban, X
            return boucle12(ruban, X)
        ruban, X = boucle12(ruban, X)
        ruban = V1(ruban, X)
        def boucle13(ruban, X):
            X = D(X)
            if ruban[X] == 0:
                return ruban, X
            return boucle13(ruban, X)
        ruban, X = boucle13(ruban, X)
        def boucle14(ruban, X):
            X = D(X)
            if ruban[X] == 1:
                return ruban, X
            return boucle14(ruban, X)
        ruban, X = boucle14(ruban, X)
        def boucle15(ruban, X):
            X = D(X)
            if ruban[X] == 0:
                return ruban, X
            return boucle15(ruban, X)
        ruban, X = boucle15(ruban, X)
        X = D(X)
        X = D(X)
        return boucle3(ruban, X)
    ruban, X = boucle3(ruban, X)
    print(''.join(map(str,ruban[500-35:500+35])))
    print(''.join([' ']*(X-500+35) + ['X'] + [' ']*(100-(X-500+35)-1)))
except IndexError:
    print('Ruban atteint à la fin, programme terminé')
    sys.exit(1)
