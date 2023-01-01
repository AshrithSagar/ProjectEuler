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


def with_mod(num, mod):
    """
    Return Number modulo 10^MOD
    """
    return int(str(num)[-mod:])


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

                    TERM_1 = math.comb(MOD-1, len(sub_part))
                    TERM_2 = math.comb(NUM_DIGITS-MOD, len(rest_part))

                    TERM_3 = 1
                    for index in uniq_sub_part:
                        count = sub_part_counter[index]
                        TERM_3 *= math.factorial(count)

                    TERM_4 = 1
                    for index in uniq_rest_part:
                        count = rest_part_counter[index]
                        TERM_4 *= math.factorial(count)

                    PROD = 1
                    PROD_1 = TERM_1 // TERM_3
                    PROD_2 = TERM_2 // TERM_4
                    PROD *= with_mod(TERM_1, MOD)
                    PROD *= with_mod(TERM_2, MOD)
                    PROD *= sum(sub_part)
                    PROD = with_mod(PROD, MOD)
                    print(digit, part, rest_part, sub_part, TERM_1, TERM_2,
                        TERM_3, TERM_4, PROD_1 ,PROD_2, sum(sub_part), PROD)
                    SUM += PROD

    NUM = int("1"*MOD)
    SUM *= NUM
    SUM = with_mod(SUM, MOD)
    print(SUM)
