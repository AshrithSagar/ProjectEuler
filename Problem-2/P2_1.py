"""
P2
"""

def fibonacci(nth, fib):
    """
    Return nth Fibonacci number, with the sequence
    """
    nth = fib[-1] + fib[-2]
    fib.append(nth)
    return nth, fib


if __name__ == '__main__':
    fib = [1, 1]
    fib_sum = 0
    while True:
        nth_fib, fib = fibonacci(0, fib)
        if nth_fib < 4e6:
            if nth_fib%2 == 0:
                fib_sum += nth_fib
        else:
            break
    print(fib_sum)
