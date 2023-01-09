"""
P717_1
"""


def primes(num):
    """
    Returns  a list of primes < n
    https://stackoverflow.com/a/3035188
    """
    sieve = [True] * num
    for index in range(3,int(num**0.5)+1,2):
        if sieve[index]:
            sieve[index*index::2*index]=[False]*((num-index*index-1)//(2*index)+1)
    return [2] + [i for i in range(3,num,2) if sieve[index]]


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
    for prime in primes(num):
        g_sum += g_function(prime)
    return g_sum


if __name__ == '__main__':
    NUM = 100

    RESULT = g_summation(NUM)
    print(RESULT)

    print(f_function(31))
