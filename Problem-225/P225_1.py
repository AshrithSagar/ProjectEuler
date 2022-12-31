"""
P225
"""

def tribonacci(t_seq):
    """
    Generate nth tribonacci
    """
    t_new = t_seq[-1] + t_seq[-2] + t_seq[-3]
    t_seq.append(t_new)
    return t_seq


if __name__ == '__main__':
    trib_seq = [1, 1, 1]
    for i in range(int(16225)):
        # print(i)
        trib_seq = tribonacci(trib_seq)
    print(trib_seq)

    non_div = []
    for odd_num in range(3, int(5e03), 2):
        FLAG = True
        for trib in trib_seq:
            if trib % odd_num == 0:
                FLAG = False
                break
        if FLAG:
            # print(odd_num)
            non_div.append(odd_num)
    print(non_div)
    print("124th odd number is", non_div[124 - 1])
