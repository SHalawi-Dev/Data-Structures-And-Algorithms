# Uses python3
import sys


# Calculating the Pisano period length
def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
            = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current % m, (previous + current) % m

    return current


def get_fibonacci_huge_naive_pisano(n, m):
    pisano_period_length = pisano_period(m)
    n = n % pisano_period_length
    return get_fibonacci_huge_naive(n, m)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive_pisano(n, m))
