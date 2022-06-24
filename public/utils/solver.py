from dancing_links import dancing_links

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
