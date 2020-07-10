## My Approach
def get_divisors_count(n):
    # Time complexity: O(sqrt N). O(1) space complexity.
    count = 2
    lim = int(n**0.5)
    for i in range(2, lim + 1):
        if n%i == 0:
            count += 2
    if lim*lim == n: count -= 1  # correction for perfect square
    # include 1 and n itself.
    return count

def naive(numdivisors):
    # O(N sqrt (N))
    s = 0
    n = 1
    while True:
        s += n
        t = get_divisors_count(s)
        n += 1
        if t>numdivisors:
            return s, t

# ------------------------------------------------------------------------------------------
# Editorial solution 1: https://projecteuler.net/overview=012

def sieve_fastest(lim):
    from itertools import compress
    # Find all primes upto n  (including n). NOTE: it does not include 2; To get list, convert the return value to list.
    BA = bytearray
    n = (lim-1)//2
    prime = BA([1])*(n+1)
    prime[0] = 0 # 2*0+1 = 1 n'est pas premier

    for i in range((int(lim**0.5)+1)//2):
        if prime[i]:
            p = 2*i+1 # p is prime
            i2 = i*(i+1)<<1
            prime[i2::p]=BA(1+ (n-i2)//p )
    return compress(range(1,lim+1,2),prime)

def optimised_using_primes(numdivisors):
    # If the prime factorisation of a number n = p1^a1 * p2^a2 ...* pk^ak. The number of divisors is the number of subsets we can create from p1...p1 (repeated a1 times) p2...p2 (repeated a2 times) and so on. The number of subsets, and thus, number of divisors is given by (a1 + 1)(a2 + 1)...(ak + 1).For e.g. n = 180 = 2^2 * 3^2 * 5. number of divisors of 180 = (2 + 1)*(2 + 1)*(1 + 1) = 18.
    # Pre-compute the primes upto a certain number. Find its exponent wrt the number.

    # predetermined limit by experimenting different values of n.
    primes = list(sieve_fastest(65500))
    num = 1
    s = 0
    cnt = 0
    while cnt<=numdivisors:
        # s += num
        s = 630
        cnt = 1
        exponent = 1
        t = s
        while t%2 == 0:
            t >>= 1
            exponent += 1
        cnt*=exponent
        for p in primes:
            if p*p > t:
                cnt *= 2
                break
            exponent = 1
            while t%p == 0:
                t //= p
                exponent += 1
            cnt *= exponent
            if t == 1: break   
        num += 1
        break

    return s, cnt

numdivisors = 500
from time import time
t = time()
print(naive(numdivisors)) #3500ms
print(time() - t)

t = time()
print(optimised_using_primes(numdivisors)) #20ms
print(time() - t)