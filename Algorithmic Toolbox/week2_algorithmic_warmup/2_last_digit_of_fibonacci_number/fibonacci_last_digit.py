# Uses python3
import sys
from time import perf_counter

# This aproach is much faster because we don't need a look up array or dict
# we just need to siplify the variable to store the last digit
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current , (previous + current) % 10

    return current

# If we needed to store some sort of look up array or dict we use this aproach
def fib_memo_last_digit(n, computed={0: 0, 1: 1}):
    for _ in range(2, n+1):
        computed[_] = (computed[_-1] + computed[_-2]) % 10
    return computed[n]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))


# start = perf_counter()
# print(fib_memo_last_digit(n))
# print("Time:", "{:.8f}".format(perf_counter() - start))
# start = perf_counter()
# print(get_fibonacci_last_digit_naive(n))
# print("Time:", "{:.8f}".format(perf_counter() - start))
