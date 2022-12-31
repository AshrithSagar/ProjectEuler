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
    T = [1, 1, 1]
    for i in range(int(1e04)):
        T = tribonacci(T)
    print(T)
