# Uses python3

from time import perf_counter


# Here are three implementations of fib algorithm
def fib_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fib_memo(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib_memo(n-1, computed) + fib_memo(n-2, computed)
    return computed[n]


def fib_local(n):
    computed = {0: 0, 1: 1}

    def fib_inner(n):
        if n not in computed:
            computed[n] = fib_inner(n-1) + fib_inner(n-2)
        return computed[n]
    return fib_inner(n)


n = int(input())
print(fib_iter(n))


# start = perf_counter()
# print(fib_local(n))
# print("Time:", "{:.8f}".format(perf_counter() - start))
# start = perf_counter()
# print(fib_iter(n))
# print("Time:", "{:.8f}".format(perf_counter() - start))
# start = perf_counter()
# print(fib_memo(n))
# print("Time:", "{:.8f}".format(perf_counter() - start))
