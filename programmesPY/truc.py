import sys
def init_ruban(size, offset1=0, size2=0):
   return ([0] * offset1) + ([0] * 500) + ([1] * size) + ([0] * 2) + ([1] * size2) + ([0] * (1000 - offset1 - size - size2 - 2 - 500))
def G(X):
    X.append(X[-1]-1)
    X.pop(0)

def D(X):
    X.append(X[-1]+1)
    X.pop(0)

def V1(ruban, X):
    index = X[-1]
    ruban[-1][index] = 1

def V0(ruban, X):
    index = X[-1]
    ruban[-1][index] = 0

ruban = [init_ruban(int(sys.argv[1]), size2=int(sys.argv[2]))]
X = [len(ruban[-1]) // 2]
try:
    print(''.join(map(str,ruban[-1][500-35:500+35])))
    print(''.join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))
    def boucle0(ruban, X):
        if ruban[-1][X[-1]] == 0:
            return
        D(X)
        return boucle0(ruban, X)
    boucle0(ruban, X)
    def boucle1(ruban, X):
        def boucle2(ruban, X):
            D(X)
            if ruban[-1][X[-1]] == 1:
                return
            print(''.join(map(str,ruban[-1][500-35:500+35])))
            print(''.join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))
            return boucle2(ruban, X)
        boucle2(ruban, X)
        V0(ruban, X)
        D(X)
        if ruban[-1][X[-1]] == 0:
            return
        def boucle3(ruban, X):
            G(X)
            if ruban[-1][X[-1]] == 1:
                return
            return boucle3(ruban, X)
        boucle3(ruban, X)
        D(X)
        V1(ruban, X)
        D(X)
        return boucle1(ruban, X)
    boucle1(ruban, X)
    def boucle4(ruban, X):
        G(X)
        if ruban[-1][X[-1]] == 1:
            return
        return boucle4(ruban, X)
    boucle4(ruban, X)
    def boucle5(ruban, X):
        G(X)
        if ruban[-1][X[-1]] == 0:
            return
        return boucle5(ruban, X)
    boucle5(ruban, X)
    D(X)
    print(''.join(map(str,ruban[-1][500-35:500+35])))
    print(''.join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))
except IndexError:
    print('Ruban atteint à la fin, programme terminé')
    sys.exit(1)
