# my solution; naive
def fibo(n):
    # Time complexity: O(log M). The ratio between consecutive fibonacci numbers approaches phi. Thus,each time we multiple by phi. So number of steps is log (M, phi)
    i, j = 1, 1
    ans = 0
    while j < n:
        j, i = i + j, j
        if not j%2: ans += j
    return ans

def editorial(n):
    # https://projecteuler.net/overview=002
    # We can get rid of the testing for even values. It is easy to prove that every third Fibonacci number is even
    i, j = 1, 1
    k = i + j
    ans = 0
    while k < n:
        ans += k
        i = j + k
        j = k + i
        k = i + j

    return ans

def editorial2(n):
    # https://projecteuler.net/overview=002
    # Even terms in fibonacci sequence obey the following recursive relation: E(n)=4*E(n-1)+E(n-2)
    i, j = 2, 8
    ans = 2
    while j < n:
        ans += j
        j, i = 4*j + i, j
    return ans

def forum1_goldenRatio(n):
# Phi (golden ratio) is the approximate ratio between two consecutive terms in a Fibonacci sequence. The ratio between consecutive even terms approaches phi^3 because each 3rd term is even. Round the results to the nearest integer when calculating the next terms. Src: https://projecteuler.net/thread=2#210

    i = 2
    phi_cube = 1.61803398875**3
    ans = 0
    while i<n:
        ans += i
        i *= phi_cube
        i = round(i)
    return ans

n = 4*10**6
print(fibo(n))
print(editorial(n))
print(editorial2(n))
print(forum1_goldenRatio(n))