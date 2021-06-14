# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def get_pisano_period(m):
    period = [0,1]
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
            = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            period.pop(i+1)
            return period
        else:
            period.append((current*current)%10)


def fib_sum_squares(n):
    sum = 0
    period = get_pisano_period(10)
    # calculate the frequancy of the period
    length = len(period)
    freq = n//length
    mod = n % length
    period_sum = 0
    partial_period_sum = 0
    for i in range(length):
        if i < mod + 1:
            partial_period_sum += period[i]
        period_sum += period[i]
    period_sum = period_sum % 10
    # print(period_sum)
    # print(partial_period_sum)
    # print(freq)
    # print(mod)
    sum = (period_sum * (freq % 10))%10+(partial_period_sum % 10)
    return sum % 10





if __name__ == '__main__':
    n = int(stdin.read())
    # print(fibonacci_sum_squares_naive(n))
    print(fib_sum_squares(n))
