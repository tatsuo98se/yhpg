class Result:
    def __init__(self):
        self.success = 0
        self.fail = 0

class Hexagon:
    def __init__(self, location):
        self.sides = []
        self.location = location

class Visitor:
    def __init__(self, name, root):
        self.name = name
        self.root = root
        self.trace = []

    def stroll(self, start, angle):
        now = start
        self.trace.append(now.location)
        for direction in self.root:
            now = now.sides[(direction + angle)%6]
            self.trace.append(now.location)

f = {}
for c in range(ord('a'), ord('w')+1):
    f[chr(c)] = Hexagon(chr(c))

f['Z'] = Hexagon('Z')

f['a'].sides = [f['Z'], f['b'], f['f'], f['Z'], f['Z'], f['Z']]
f['b'].sides = [f['Z'], f['c'], f['g'], f['f'], f['a'], f['Z']]
f['c'].sides = [f['Z'], f['d'], f['h'], f['g'], f['b'], f['Z']]
f['d'].sides = [f['Z'], f['e'], f['i'], f['h'], f['c'], f['Z']]
f['e'].sides = [f['Z'], f['Z'], f['Z'], f['i'], f['d'], f['Z']]
f['f'].sides = [f['b'], f['g'], f['k'], f['j'], f['Z'], f['a']]
f['g'].sides = [f['c'], f['h'], f['l'], f['k'], f['f'], f['b']]
f['h'].sides = [f['d'], f['i'], f['m'], f['l'], f['g'], f['c']]
f['i'].sides = [f['e'], f['Z'], f['n'], f['m'], f['h'], f['d']]
f['j'].sides = [f['f'], f['k'], f['o'], f['Z'], f['Z'], f['Z']]
f['k'].sides = [f['g'], f['l'], f['p'], f['o'], f['j'], f['f']]
f['l'].sides = [f['h'], f['m'], f['q'], f['p'], f['k'], f['g']]
f['m'].sides = [f['i'], f['n'], f['r'], f['q'], f['l'], f['h']]
f['n'].sides = [f['Z'], f['Z'], f['Z'], f['r'], f['m'], f['i']]
f['o'].sides = [f['k'], f['p'], f['t'], f['s'], f['Z'], f['j']]
f['p'].sides = [f['l'], f['q'], f['u'], f['t'], f['o'], f['k']]
f['q'].sides = [f['m'], f['r'], f['v'], f['u'], f['p'], f['l']]
f['r'].sides = [f['n'], f['Z'], f['w'], f['v'], f['q'], f['m']]
f['s'].sides = [f['o'], f['t'], f['Z'], f['Z'], f['Z'], f['Z']]
f['t'].sides = [f['p'], f['u'], f['Z'], f['Z'], f['s'], f['o']]
f['u'].sides = [f['q'], f['v'], f['Z'], f['Z'], f['t'], f['p']]
f['v'].sides = [f['r'], f['w'], f['Z'], f['Z'], f['u'], f['q']]
f['w'].sides = [f['Z'], f['Z'], f['Z'], f['Z'], f['v'], f['r']]
f['Z'].sides = [f['Z'], f['Z'], f['Z'], f['Z'], f['Z'], f['Z']]

visitors = []
visitors.append(Visitor('B', [0, 0, 4]))
visitors.append(Visitor('D', [0, 4, 4]))
visitors.append(Visitor('I', [0, 0, 0]))

visitors.append(Visitor('J', [0, 0, 1]))
visitors.append(Visitor('L', [0, 0, 5]))
visitors.append(Visitor('N', [0, 1, 2]))
visitors.append(Visitor('O', [0, 1, 3]))
visitors.append(Visitor('S', [0, 5, 0]))
visitors.append(Visitor('Y', [0, 1, 4, 5]))
visitors.append(Visitor('Z', [0, 1, 0]))

def is_chars_all_included(lhs, rhs):
    for c in list(lhs):
        if not rhs.count(c):
            return False

    return True

def detect_shape(data):
    for v in visitors:
        for c in list(data):
            for d in range(6):
                v.stroll(f[c],d)
                if is_chars_all_included(v.trace, data):
                    return v.name
                v.trace = []
    return '-'


result = Result()
result.success = result.fail = 0

def test(data, expect):
    if detect_shape(data) == expect:
        result.success += 1
    else:
        result.fail += 1


test( "glmq", "B" )
test( "fhoq", "-" )
test( "lmpr", "N" )
test( "glmp", "Y" )
test( "dhkl", "J" )
test( "glpq", "D" )
test( "hlmq", "O" )
test( "eimq", "I" )
test( "cglp", "S" )
test( "chlq", "Z" )
test( "glqr", "L" )
test( "cdef", "-" )
test( "hijk", "-" )
test( "kpqu", "B" )
test( "hklm", "B" )
test( "mqrw", "B" )
test( "nrvw", "B" )
test( "abfj", "B" )
test( "abcf", "B" )
test( "mrvw", "D" )
test( "ptuv", "D" )
test( "lmnr", "D" )
test( "hklp", "D" )
test( "himr", "D" )
test( "dhil", "D" )
test( "hlpt", "I" )
test( "stuv", "I" )
test( "bglq", "I" )
test( "glmn", "J" )
test( "fghm", "J" )
test( "cdgk", "J" )
test( "lpst", "J" )
test( "imrw", "J" )
test( "dinr", "J" )
test( "cdin", "L" )
test( "eghi", "L" )
test( "cdeg", "L" )
test( "bgko", "L" )
test( "eimr", "L" )
test( "jotu", "L" )
test( "kotu", "N" )
test( "lqtu", "N" )
test( "cdim", "N" )
test( "klot", "N" )
test( "kloq", "N" )
test( "kmpq", "N" )
test( "qrvw", "O" )
test( "mnqr", "O" )
test( "kopt", "O" )
test( "mnpq", "S" )
test( "bfko", "S" )
test( "chin", "S" )
test( "hmnq", "Y" )
test( "nqrw", "Y" )
test( "bchi", "Z" )
test( "inrw", "Z" )
test( "cfgj", "Z" )
test( "jnpv", "-" )
test( "flmp", "-" )
test( "adpw", "-" )
test( "eilr", "-" )
test( "bejv", "-" )
test( "enot", "-" )
test( "fghq", "-" )
test( "cjms", "-" )
test( "elov", "-" )
test( "chlm", "D" )
test( "acop", "-" )
test( "finr", "-" )
test( "qstu", "L" )
test( "abdq", "-" )
test( "jkln", "-" )
test( "fjkn", "-" )
test( "ijmn", "-" )
test( "flqr", "-" )

print("Success: {0.success}, Fail: {0.fail}".format(result))