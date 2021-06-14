# Uses python3
import sys

# This algorithm takes too much time
# it's approximatly O(a+b)
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

# This is the Euclidean approach to compute GCD
# it's appr O(log(a.b))
def euclidean_gcd(a, b):
    # The following print to visualize
    # print(str(a)+"  "+str(b))
    if b == 0:
        return a
    else:
        return euclidean_gcd(b, a % b)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    if a==0 or b ==0:
        print(1)
    elif a > b:
        print(euclidean_gcd(a, b))
    elif b > a:
        print(euclidean_gcd(b, a))
    else:
        print(a)
