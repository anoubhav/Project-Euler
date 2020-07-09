from functools import reduce
def isprime_optimised(num):
    if num == 1: return False
    elif num < 4: return True
    elif num%2 == 0 or num%3 == 0: return False
    else:
        for i in range(5, int(num**0.5) + 1, 6):
            if num%i==0:return False
            if num%(i+2)==0:return False
        return True

def constantSpace(n):
    # Using the optimised primality testing algorithm. Time complexity: O(N sqrt N). Space complexity: O(1)
    ans = 0
    for i in range(2, n):
        if isprime_optimised(i): ans += i
    return ans

def sieve(n):
    # Get all primes upto n, in O(N log log N) time complexity; O(N) space complexity
    isprime = [True]*(n)
    isprime[0] = isprime[1] = False
    for num in range(2, n):
        if num*num > n:
            break
        if isprime[num]:
            for i in range(num*num, n, num):
                isprime[i] = False
    return reduce(lambda x, y : x+y, [i for i in range(2, n) if isprime[i]])

def sieve_optimized(n):
    # Find all primes upto n  (including n)
    sievebound = (n-1)//2
    sieve = [False]*(sievebound + 1)
    sieve[0] = True
    crosslimit = (int(sievebound**0.5) - 1)
    for i in range(1, crosslimit + 1):
        if not sieve[i]:
            for j in range(2*i*(i+1), sievebound + 1, 2*i+1):
                sieve[j] = True
    
    return reduce(lambda x, y : x+y, [2] + [2*i+1 for i in range(1, sievebound+1) if not sieve[i]])

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

def DP(n):
    # https://projecteuler.net/thread=10;page=5#111677
    # Did not understand it
    r = int(n**0.5)
    assert r*r <= n and (r+1)**2 > n
    V = [n//i for i in range(1,r+1)]
    V += list(range(V[-1]-1,0,-1))
    S = {i:i*(i+1)//2-1 for i in V}
    for p in range(2,r+1):
        if S[p] > S[p-1]:  # p is prime
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            for v in V:
                if v < p2: break
                S[v] -= p*(S[v//p] - sp)
    return S[n]

n = 2*10**6
# 5000ms
from time import time
# t = time()
# print(constantSpace(n)) # slower than sieve as sqrt of N is much more than log log N
# print(time() - t)

# 350ms
t = time()
print(sieve(n))
print(time() - t)

# 170ms
t = time()
print(sieve_optimized(n))
print(time() - t)

# 40ms
t = time()
print(2+sum(sieve_fastest(n)))
print(time() - t)

# 20ms
t = time()
print(DP(n))
print(time() - t)



# Key points:
# When you want to find all primes below some limit, use the sieve of Eratosthenes
# When you want to test just a handful of not too large  numbers, trial division is adequate.
# Suppose you’d want to test a few hundred numbers between 10^9 and 10^10. Then a mixed strategy is good. First use a sieve to find the primes up to 10^5, then perform trial division by these primes.


# An easy optimisation of the sieve is suggested by the discrimination of odd and
# even numbers. 