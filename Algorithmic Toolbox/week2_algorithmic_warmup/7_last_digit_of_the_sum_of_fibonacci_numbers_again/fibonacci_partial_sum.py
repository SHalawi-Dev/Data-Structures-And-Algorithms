# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum = (sum + current) % 10

        current, next = next % 10, (current + next)%10

    return sum



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
            period.append(current)


def fib_sum(n):
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

def fib_partial_sum(frm,to):
    sum = 0
    frm = fib_sum(frm-1)
    to = fib_sum(to)
    # print("from: "+str(frm)+" to: "+str(to))
    if to >= frm:
        return  to-frm
    else:
        return (to+10)-frm
    

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    # print(fibonacci_partial_sum_naive(from_, to))
    print(fib_partial_sum(from_,to))