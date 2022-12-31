"""
P3
"""
import math

NUM = 600851475143
divisors = []

for x in range(1, int(math.sqrt(NUM))):
    if NUM % x == 0:
        divisors.append(x)

print(divisors)
