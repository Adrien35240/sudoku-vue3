N = 3
N2 = N * N
N4 = N2 * N2

# les ensembles
def assignation(r, c, v): return r * N4 + c * N2 + v

def row(a): return a // N4
def col(a): return (a // N2) % N2
def val(a): return a % N2
def blk(a): return (row(a) // N) * N + col(a) // N

# les elements à couvrir
def rc(a): return row(a) * N2 + col(a)
def rv(a): return row(a) * N2 + val(a) + N4
def cv(a): return col(a) * N2 + val(a) + 2 * N4
def bv(a): return blk(a) * N2 + val(a) + 3 * N4

def sudoku(G):
    global N, N2, N4
    if len(G) == 9:    # for a 16 x 16 sudoku grid
        N, N2, N4 = 3, 9, 81
    e = 4 * N4
    univers = e + 1
    S = [[rc(a), rv(a), cv(a), bv(a)] for a in range(N4 * N2)]
    A = [e]
    for r in range(N2):
        for c in range(N2):
            if G[r][c] != 0:
                a = assignation(r, c, G[r][c] - 1)
                A += S[a]
    sol = dancing_links(univers, S + [A])
    if sol:
        for a in sol:
            if a < len(S):
                G[row(a)][col(a)] = val(a) + 1
        return G
    else:
        return False

def dancing_links(size_univers, sets):
    header = Cell(None, None, 0, None)  # constr. la structure des cellules
    col = []
    for j in range(size_univers):
        col.append(Cell(header, None, 0, None))
    for i in range(len(sets)):
        row = None
        for j in sets[i]:
            col[j].S += 1   # une entrée de plus dans cette col
            row = Cell(row, col[j], i, col[j])
    sol = []
    if solve(header, sol):
        return sol
    else:
        return None

def solve(header, sol):
    if header.R == header:  # instance vide, solution trouvée
        return True
    c = None
    j = header.R
    while j != header:
        if c is None or j.S < c.S:
            c = j
        j = j.R     # couvrir éléments dans l'ensemble r
    cover(c)
    r = c.D
    while r != c:
        sol.append(r.S)
        j = r.R
        while j != r:
            cover(j.C)
            j = j.R
        if solve(header, sol):
            return True
        j = r.L
        while j != r:
            uncover(j.C)
            j = j.L
        sol.pop()
        r = r.D
    uncover(c)
    return False

class Cell:
    def __init__(self, horiz, verti, S,C):
        self.S = S
        self.C = C
        if horiz:
            self.L = horiz.L
            self.R = horiz
            self.L.R = self
            self.R.L = self
        else:
            self.L = self
            self.R = self
        if verti:
            self.U = verti.U
            self.D = verti
            self.U.D = self
            self.D.U = self
        else:
            self.U = self
            self.D = self
    def hide_verti(self):
        self.U.D = self.D
        self.D.U = self.U

    def unhide_verti(self):
        self.D.U = self
        self.U.D = self

    def hide_horiz(self):
        self.L.R = self.R
        self.R.L = self.L

    def unhide_horiz(self):
        self.R.L = self
        self.L.R = self

def cover(c):
    assert c.C is None
    c.hide_horiz()
    i = c.D
    while i != c:
        j = i.R
        while j != i:
            j.hide_verti()
            j.C.S -= 1
            j = j.R
        i = i.D
def uncover(c):
    assert c.C is None
    i = c.U
    while i != c:
        j = i.L
        while j != i:
            j.C.S += 1
            j.unhide_verti()
            j = j.L
        i = i.U
    c.unhide_horiz()
