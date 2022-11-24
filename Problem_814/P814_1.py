"""
Brute force approach.
"""
import numpy as np
import itertools

n = 1 # input("Enter n:")
S_n = 0

# Arr = np.zeros(4*n, dtype=int)
Arr = []
# 0 => Down
# 1 => Left
# 2 => Right
# 3 => Diagonally opposite

for i in range(4*n):
    Arr.append([1, 2, 3])

Arr = itertools.product(*Arr)
for comb in Arr:
    n_match = 0
    for i, e in enumerate(comb):
        if (e == 2 and comb[((i+1)%(4*n))] == 1):
            n_match += 1
        elif (i < 2*n and e == 3 and comb[(i+2*n)] == 3):
            n_match += 1

    if n_match == n:
        S_n += 1

print("S({}) = {}".format(n, S_n))
