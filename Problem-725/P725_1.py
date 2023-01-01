"""
P725_1
"""

def ds_sum(n_digits):
    """
    Sum of all DS-numbers of N digits or less.
    """
    sum_ds = 0

    for num in range(1, 10**n_digits):
        num_str = str(num)
        num_arr = [int(d) for d in num_str]
        max_d = max(num_arr)
        if sum(num_arr) == 2*max_d:
            # print(num)
            sum_ds += num

    return sum_ds


if __name__ == '__main__':
    print(ds_sum(3))
    print(ds_sum(7))
