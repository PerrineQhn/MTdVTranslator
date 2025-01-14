import sys
sys.setrecursionlimit(2000)
def init_ruban(params):
   size = params[0]
   size2 = params[1] if len(params) > 1 else 0
   if size2 > 0:      return ([0] * 500) + ([1] * size) + ([0] * 2) + ([1] * size2) + ([0] * (1000 - size - size2 - 2 - 500))
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

def new_join(lst):
   def helper(index):
       if index == new_len(lst):
           return ""
       return "{}".format(lst[index]) + helper(index + 1)
   return helper(0)
def new_len(lst):
   if not lst:
       return 0
   return 1 + new_len(lst[1:])

ruban = init_ruban([int(sys.argv[1]) + 1])
X = [new_len(ruban) // 2]
try:
    def boucle0():
        D(X)
        V0()
        D(X)
        if ruban[X[-1]] == 0:
            return
        return boucle0()
    boucle0()
    print(new_join(ruban[500-35:500+35]))
    print(new_join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))
    G(X)
    def boucle1():
        G(X)
        print(new_join(ruban[500-35:500+35]))
        print(new_join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))
        def boucle2():
            G(X)
            if ruban[X[-1]] == 0:
                return
            return boucle2()
        boucle2()
        G(X)
        if ruban[X[-1]] == 0:
            return
        D(X)
        V1()
        def boucle3():
            D(X)
            if ruban[X[-1]] == 0:
                return
            return boucle3()
        boucle3()
        G(X)
        V0()
        return boucle1()
    boucle1()
    D(X)
    D(X)
    print(new_join(ruban[500-35:500+35]))
    print(new_join([' ']*(X[-1]-500+35) + ['X'] + [' ']*(100-(X[-1]-500+35)-1)))
except IndexError:
    print('Ruban atteint à la fin, programme terminé')
    sys.exit(1)
