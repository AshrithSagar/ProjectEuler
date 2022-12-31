"""
P206
"""
# 1_2_3_4_5_6_7_8_9_0
# Ends in 900.

import math
from itertools import product


def is_square(number: int) -> bool:
    """Check for square"""
    return number == math.isqrt(number) ** 2


def concat(array):
    """
    Convert from array to number
    """
    number = ""
    for digit in array:
        number += str(digit)
    return int(number)


if __name__ == '__main__':
    num = [1, -1, 2, -1, 3, -1, 4, -1, 5, -1, 6, -1, 7, -1, 8, -1, 9, 0, 0]

    for i, e in enumerate(num):
        if e == -1:
            num[i] = range(10)
        else:
            num[i] = [num[i]]
    print(*num)
    prod = product(*num)
    for x in prod:
        # print(x)
        X = concat(x)
        if is_square(X):
            print(X)
            break
