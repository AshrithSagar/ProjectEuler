"""
P717_2
"""
import json

def primes_1e7():
    """
    Get primes less than 1e7.
    """
    with open("primes_1e7.json", encoding='utf-8') as file:
        primes = json.load(file)
    return primes


def f_function(prime):
    """
    .
    """
    two_power_p = 2**prime
    modend = 2**two_power_p // prime
    result = modend % two_power_p
    return result


def g_function(prime):
    """
    .
    """
    result = 0
    result = f_function(prime) % prime
    return result


def g_summation(num):
    """
    .
    """
    g_sum = 0
    for prime in primes_1e7():
        if prime < num:
            g_sum += g_function(prime)
        else:
            break
    return g_sum


if __name__ == '__main__':
    NUM = 100

    # RESULT = g_summation(NUM)
    # print(RESULT)

    print(f_function(3))
