"""
P725_2
"""
import itertools


def partitions(num, init=1):
    """
    https://stackoverflow.com/a/44209393
    """
    yield (num,)
    for i in range(init, num//2 + 1):
        for part in partitions(num-i, i):
            yield (i,) + part


def ds_n(num_digits, num_non_zero = -1):
    """
    Sum of all DS-numbers of N digits.
    num_digits: Total number of digits.
    num_non_zero: Number of non-zero digits.
    """
    if num_non_zero == -1:
        num_non_zero = num_digits

    sum_ds = 0
    for digit in range(10):
        for part in partitions(digit):
            if len(part) == (num_non_zero-1):
                perms = itertools.permutations([*part, digit])
                uniq_perms = set(perms)
                for perm in uniq_perms:
                    perm = [str(x) for x in perm]
                    perm_num = "".join(perm)
                    print(perm_num)
                    sum_ds += int(perm_num)
    return num_digits, sum_ds


if __name__ == '__main__':
    print(ds_n(3))
    print(ds_n(2))
    print(ds_n(1))
