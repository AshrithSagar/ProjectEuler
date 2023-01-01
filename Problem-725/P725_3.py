"""
P725_3
"""
import itertools


def partitions(num, init=1):
    """
    https://stackoverflow.com/a/44209393
    """
    yield (num,)
    for anchor in range(init, num//2 + 1):
        for partition in partitions(num-anchor, anchor):
            yield (anchor,) + partition


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
                for sub_part in itertools.combinations(part, choice):
                    print(sub_part)
                    rest_part = list(set(part) - set(sub_part))
                    print(rest_part)

                    zeros = NUM_DIGITS - MOD - len(rest_part)
                    perms = itertools.permutations([*[0]*zeros, *rest_part])
                    uniq_perms = set(perms)
                    print(uniq_perms)
                    count = len(uniq_perms)

                    zeros = MOD - len(sub_part)
                    perms = itertools.permutations([*[0]*zeros, *sub_part])
                    uniq_perms = set(perms)
                    print(uniq_perms)
                    for perm in uniq_perms:
                        perm = [str(x) for x in perm]
                        PERM_NUM = "".join(perm)
                        SUM += int(PERM_NUM) * count
    print(SUM)
