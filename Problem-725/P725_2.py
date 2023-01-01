"""
P725_2
"""
import itertools


def partitions(n, I=1):
    """
    https://stackoverflow.com/a/44209393
    """
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p


def ds_n(N):
    """
    Sum of all DS-numbers of (exactly) N digits.
    """
    sum_ds = 0
    for d in range(10):
        for p in partitions(d):
            if len(p) == (N-1):
                perms = itertools.permutations([*p, d])
                uniq_perms = set(perms)
                print(d, uniq_perms)
                sum_ds += (2*d) * len(uniq_perms)
    return N, sum_ds


if __name__ == '__main__':
    print(ds_n(3))
    print(ds_n(2))
    print(ds_n(1))