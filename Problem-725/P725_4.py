"""
P725_4
"""
import math
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


def multinomial(lst):
    """
    https://stackoverflow.com/a/46378809
    """
    if not lst:
        return 1

    res, i = 1, sum(lst)
    init = lst.index(max(lst))
    for anch in lst[:init] + lst[init+1:]:
        for j in range(1,anch+1):
            res *= i
            res //= j
            i -= 1
    return res


def with_mod(num, mod):
    """
    Return Number modulo 10^MOD
    """
    return int(str(int(num))[-mod:])


if __name__ == '__main__':
    NUM_DIGITS = 2020
    MOD = 16
    SUM = 0

    for digit in range(1, 10):
        for part in partitions(digit):
            part = [*part, digit]
            for choice in range(1, len(part)+1):
                combs = itertools.combinations(part, choice)
                uniq_combs = set(combs)

                for sub_part in uniq_combs:
                    rest_part = diff(part, sub_part)
                    sub_part_counter = Counter(sub_part)
                    rest_part_counter = Counter(rest_part)
                    uniq_sub_part = set(sub_part)
                    uniq_rest_part = set(rest_part)

                    DIG_SUM = 0
                    ZEROS = (MOD) - len(sub_part)
                    for place in uniq_sub_part:
                        TERM_3 = sub_part_counter.copy()
                        TERM_3[place] -= 1
                        TERM_1 = multinomial([ZEROS, *list(TERM_3)])
                        TERM_1 = with_mod(TERM_1, MOD)
                        TERM_6 = sub_part_counter[place]
                        TERM_5 = TERM_6 * TERM_1
                    TERM_5 = with_mod(TERM_5, MOD)

                    ZEROS = (NUM_DIGITS - MOD) - len(rest_part)
                    TERM_2 = multinomial([ZEROS, *list(rest_part_counter.values())])
                    TERM_2 = with_mod(TERM_2, MOD)

                    PROD = 1
                    for term in [TERM_5, TERM_2]:
                        PROD *= term
                        PROD = with_mod(PROD, MOD)
                    # PROD /= MOD
                    print(digit, part, rest_part, sub_part, TERM_2,
                        TERM_5, sum(sub_part), PROD)
                    SUM += PROD

    NUM = int("1"*MOD)
    SUM *= NUM
    SUM = with_mod(SUM, MOD)
    print(SUM)
