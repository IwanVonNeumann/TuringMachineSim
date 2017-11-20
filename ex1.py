from main import SPACE, R, L, qz, sim

# translate number from unary form to binary

A = {"I", "0", "1", SPACE}
inp = ["I", "I", "I", "I", "I"]

niu = {
    "q1": {"I": "q1", "0": "q1", SPACE: "q2"},
    "q2": {"I": "q3", "0": "q4", "1": "q4"},
    "q3": {"I": "q3", "0": "q1", "1": "q3", SPACE: "q1"},
    "q4": {"0": "q4", "1": "q4", SPACE: qz}
}

zeta = {
    "q1": {"I": "I", "0": "0", SPACE: SPACE},
    "q2": {"I": SPACE, "0": "0", "1": "1"},
    "q3": {"I": "I", "0": "1", "1": "0", SPACE: "1"},
    "q4": {"0": "0", "1": "1", SPACE: SPACE}
}

delta = {
    "q1": {"I": R, "0": R, SPACE: L},
    "q2": {"I": L, "0": L, "1": L},
    "q3": {"I": L, "0": R, "1": L, SPACE: R},
    "q4": {"0": L, "1": L, SPACE: R}
}

print(sim(inp, zeta, delta, niu))
