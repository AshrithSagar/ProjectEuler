"""
P725_3
"""
import itertools
from collections import Counter


def partitions(num, init=1):
    """
    https://stackoverflow.com/a/44209393
    """
    yield (num,)
    for anchor in range(init, num//2 + 1):
        for partition in partitions(num-anchor, anchor):
            yield (anchor,) + partition


def diff(first, second):
    """
    https://stackoverflow.com/a/63319667
    """
    second_cntr = Counter(second)
    second = set(second)
    res = []
    for i in first:
        if i not in second:
            res.append(i)
        elif i in second_cntr:
            if second_cntr[i] > 0:
                second_cntr[i] -= 1
            else:
                res.append(i)
    return res


if __name__ == '__main__':
    NUM_DIGITS = 2020
    MOD = 16
    SUM = 0

    for digit in range(1, 10):
        for part in partitions(digit):
            part = [*part, digit]
            print(part)
            for choice in range(1, len(part)+1):
                print(choice)
                combs = itertools.combinations(part, choice)
                uniq_combs = set(combs)

                for sub_part in itertools.combinations(part, choice):
                    print(sub_part)
                    rest_part = diff(part, sub_part)
                    print(rest_part)

                    ZEROS = NUM_DIGITS - MOD - len(rest_part)
                    print(ZEROS)
                    perms = itertools.permutations([*[0]*ZEROS, *rest_part])
                    print(perms)
                    uniq_perms = set(perms)
                    print(uniq_perms)
                    count = len(uniq_perms)

                    ZEROS = MOD - len(sub_part)
                    print(ZEROS)
                    perms = itertools.permutations([*[0]*ZEROS, *sub_part])
                    print(perms)
                    uniq_perms = set(perms)
                    print(uniq_perms)
                    for perm in uniq_perms:
                        perm = [str(x) for x in perm]
                        PERM_NUM = "".join(perm)
                        SUM += int(PERM_NUM) * count
    print(SUM)
