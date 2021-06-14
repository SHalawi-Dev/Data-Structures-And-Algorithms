# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


# This is the Euclidean approach to compute GCD
# it's appr O(log(a.b))
def euclidean_gcd(a, b):
    # The following print to visualize
    # print(str(a)+"  "+str(b))
    if b == 0:
        return a
    else:
        return euclidean_gcd(b, a % b)


# LCM is defined as follows
# lcm(a,b) = a*b/gcd(a,b)
def euclidean_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    elif a > b:
        return a*b/(euclidean_gcd(a, b))
    elif b > a:
        return a*b/(euclidean_gcd(b, a))
    else:
        return a


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(int(euclidean_lcm(a, b)))
