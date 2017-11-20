SPACE = "λ"
R = 1
L = -1
qz = "qz"


def sim(inp, zeta, delta, niu):
    n = len(inp)
    tape = [SPACE] * (n + 1) + inp + [SPACE]
    q = "q1"
    t = n + 1
    while q != qz:
        a = tape[t]
        tape[t] = zeta[q][a]
        t = t + delta[q][a]
        q = niu[q][a]
    return tape
