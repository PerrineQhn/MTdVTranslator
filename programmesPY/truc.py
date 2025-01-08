import sys
def init_ruban(size):
   if sys.argv[2]:
       return ([0] * 500) + ([1] * size) + ([0] * 2) + ([1] * int(sys.argv[2])) + ([0] * (1000 - size - int(sys.argv[2]) - 2 - 500))
   else:
       return ([0] * 500) + ([1] * size) + ([0] * 2) + ([0] * (1000 - size - 2 - 500))
def G(X):
    X.append(X[-1]-1)
    X.pop(0)

def D(X):
    X.append(X[-1]+1)
    X.pop(0)

def V1():
    index = X[-1]
    ruban.pop(index)
    ruban.insert(index, 1)

def V0():
    index = X[-1]
    ruban.pop(index)
    ruban.insert(index, 0)

ruban = init_ruban(int(sys.argv[1]))
X = [len(ruban) // 2]
try:
    print(''.join(map(str,ruban[500-35:500+35])))
    print(''.join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))
    def boucle0():
        if ruban[X[-1]] == 0:
            return
        D(X)
        return boucle0()
    boucle0()
    def boucle1():
        def boucle2():
            D(X)
            if ruban[X[-1]] == 1:
                return
            print(''.join(map(str,ruban[500-35:500+35])))
            print(''.join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))
            return boucle2()
        boucle2()
        V0()
        D(X)
        if ruban[X[-1]] == 0:
            return
        def boucle3():
            G(X)
            if ruban[X[-1]] == 1:
                return
            return boucle3()
        boucle3()
        D(X)
        V1()
        D(X)
        return boucle1()
    boucle1()
    def boucle4():
        G(X)
        if ruban[X[-1]] == 1:
            return
        return boucle4()
    boucle4()
    def boucle5():
        G(X)
        if ruban[X[-1]] == 0:
            return
        return boucle5()
    boucle5()
    D(X)
    print(''.join(map(str,ruban[500-35:500+35])))
    print(''.join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))
except IndexError:
    print('Ruban atteint à la fin, programme terminé')
    sys.exit(1)
