from collections import defaultdict as dd
from math import ceil, log10
n = 20
def helper_get_factors(n):
    factors = []
    count = 0
    while n%2 == 0:
        n >>= 1
        count += 1
    if count: factors.append((2, count))

    for i in range(3, ceil(n**0.5) + 1, 2):
        count = 0
        while n%i == 0:
            n //= 3
            count += 1
        if count: factors.append((i, count))
    
    if n!=1:
        factors.append((n, 1))
    return factors

# My approach (same as 1st approach of editorial): For N to be the smallest value with this property we must ensure that in its prime factorisation it does not contain any more prime factors than is absolutely necessary. Get the prime factorisation from (2, N). Store the maximum exponent encountered for each Pi.
def smallest_multiple_naive(n):
    # Overall time complexity: O(N sqrt(N))
    factor_count = dd(int)
    # O(N)
    for num in range(2, n+1):
        # O(sqrt N)
        factors = helper_get_factors(num)
        for fac, freq in factors:
            factor_count[fac] = max(factor_count[fac], freq)

    ans = 1
    for k, v in factor_count.items():
        ans *= k**v

    return ans

# ------------------------------------------------------------------
## Approach 2. We want to find the smallest number divisible by 1...20. That is by definition the LCM(1, 2, 3, ..., 20). We know for two numbers a and b, LCM*GCD = a*b. The time complexity of Euclid's gcd algorithm is O(log ab). Src: https://stackoverflow.com/questions/3980416/time-complexity-of-euclids-algorithm. 

# So we obtain gcd pair-wise until we reach 20. # time complexity: O(n * gcd). The LCM of two numbers a and b is going to be the smallest number that has enough prime powers to be able to "contain" both a and b.
# https://projecteuler.net/thread=5;post=105775
def gcd(a, b):
    # O(log ab). Key insight: If M > N, then M mod N < M/2. The search space becomes atleast half every two iterations.

    if a:
        return gcd(b%a, a)
    return b

def lcm(a, b):
    return (a*b)//gcd(a, b)

def smallest_multiple_gcd_lcm(n):
    # O(N* log K). K is some number.
    ans = 1
    for i in range(2, n+1):
        ans = lcm(i, ans)
    return ans
    
# ------------------------------------------------------------------
# Approach 3: Get all primes upto n. For each prime, the maximum exponent is the greatest perfect power of Pi that is less than or equal to n. If n = 20, Pi = 2; 2^4 < 20 and not 2^5. So 4 is the exponent for 2. Same can be found for other primes.

# Finding the maximum exponent given a prime number is constant time. Find the prime numbers upto N can be done using sieve of eratosthenes in O(n log log n)

def sieve(n):
    isprime = [True]*(n+1)
    isprime[0] = isprime[1] = False
    for i in range(2, n+1):
        if isprime[i] and i*i <= n:
            for i in range(i*i, n+1, i):
                isprime[i] = False

    return [i for i in range(len(isprime)) if isprime[i]]

def smallest_multiple_sieve(n):
    # O(n log log n) time complexity for finding primes.
    # LCM(1, ⋯, N)=∏ p⌊log(N)log(p)⌋

    primes = sieve(n) # sorted order
    ans = 1
    check = True
    for p in primes:
        exp = 1
        if check:
            exp = int(log10(n)/log10(p))
            if exp == 1:
                check = False
        ans *= p**exp
    return ans
            
print(smallest_multiple_sieve(100000))
# from time import time
## Remember multiplication step is the one taking time. to do this analysis use modulo 10**9 + 7 to negate multiplication effects. And invermodulo the answer is required.

# # Approach 1: O(N sqrt (N))
# t1 = time()
# print('O(N sqrt(N)) solution   :', smallest_multiple_naive(n), '; Time:', time() - t1)

# # Approach 2: O(n log (ab))
# t2 = time()
# print('O(N log K) solution     :', smallest_multiple_gcd_lcm(n), '; Time:', time() - t2)

# # Approach 3: O(n log log n)
# t3 = time()
# print('O(N log log N) solution :', smallest_multiple_sieve(n), '; Time:', time() - t3)

