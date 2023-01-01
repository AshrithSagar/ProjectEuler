"""
P725_2
"""
import itertools


def partitions(num, init=1):
    """
    https://stackoverflow.com/a/44209393
    """
    yield (num,)
    for index in range(init, num//2 + 1):
        for part in partitions(num-index, index):
            yield (index,) + part


def ds_sum(num_digits):
    """
    Sum of all DS-numbers of N digits or less.
    """
    sum_ds = 0
    for digit in range(10):
        for part in partitions(digit):
            zeros = (num_digits-1) - len(part)
            if zeros >= 0:
                perms = itertools.permutations([*[0]*zeros, *part, digit])
                uniq_perms = set(perms)
                for perm in uniq_perms:
                    perm = [str(x) for x in perm]
                    perm_num = "".join(perm)
                    # print(perm_num)
                    sum_ds += int(perm_num)
    return sum_ds


if __name__ == '__main__':
    print(ds_sum(3))
    print(ds_sum(7))
