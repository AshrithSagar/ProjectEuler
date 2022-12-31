"""
P206_2
"""
# 1_2_3_4_5_6_7_8_9_0
# Ends in 900.

import math


if __name__ == '__main__':
    lower_bound = math.floor(math.sqrt(1e16))
    upper_bound = math.floor(math.sqrt(2e16))
    print(lower_bound, upper_bound)

    for last_digit in [3, 7]:
        for num in range(lower_bound + last_digit, upper_bound, 10):
            # print(num)
            FLAG = True
            num_square = num ** 2
            num_square = str(num_square)
            # print(num_square)
            for i in range(8):  # (9) Not required
                if int(num_square[2*i]) == int(i+1):
                    FLAG = False
                    break
            if FLAG:
                print("Square:", num_square+"00")
                break
        if FLAG:
            break
