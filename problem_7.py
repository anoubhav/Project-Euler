from math import ceil
def isprime(num):
    if num == 2: return 1
    elif num%2 == 0: return 0

    for i in range(3, ceil(num**0.5) + 1, 2):
        if num%i == 0: return 0
    return 1

def naive(n):
    # Time complexity: O(N sqrt N). Space complexity: O(1)

    count = 1
    num = 3
    while count < n:
        count += isprime(num)
        num += 2
    return num-2

# -------------------------------------------------------------

def sieve(n, size = 10**6):
    # Time complexity: O(N log log N). Space complexity is O(N).
    
    # This is feasible to calculate primes upto 10^8. After which you can encounter memory errors.
    isprime = [True]*size
    isprime[0] = isprime[1] = False
    for i in range(2, size):
        if i*i>size:
            break
        if isprime[i]:
            for j in range(i*i, size, i):
                isprime[j] = 0

    count = 0
    for i, flag in enumerate(isprime):
        if flag == True:
            count += 1
        
        if count == n:
            return i


# From editorial: We do not know what answer to expect so we will try to solve this problem using trial division (naive). However, if a good upper bound for the target prime is known in advance, using a sieve of Eratosthenes is a much more efficient method.

# ------------------------------------------------------------
# Facts which can be used:
# - 1 is not a prime.
# - All primes except 2 are odd.
# - All primes greater than 3 can be written in the form **6k +/- 1.**
# - Any number n can have only one primefactor greater than sqrt(n) .
# The consequence for primality testing of a number n is: if we cannot find a number f less than or equal sqrt(n) that divides n then n is prime: the only primefactor of n is n itself

def isprime_optimised(num):
    if num == 1: return False
    elif num < 4: return True
    elif num%2 == 0 or num%3 == 0: return False
    else:
        for i in range(5, ceil(num**0.5) + 1, 6):
            if num%i==0:return False
            if num%(i+2)==0:return False
        return True

def editorial(n):
    # https://projecteuler.net/overview=007
    # When upper bound is not known, sieve is not the best solution. 
    count = 1
    num = 1
    while count < n:
        num += 2
        count += isprime(num)
    return num

n = 100001
print(naive(n)) 
# Memory allocation is taking time. NOt the computations, in case of sieve. Also, we are over calculating.
print(sieve(n, size=10**7)) 
print(editorial(n))

# Let's check the percentage of prime in first 10^n numbers.

""" 
10^n  Prime count  % prime
1     4            0.4
2     25           0.25 (1 in 4 is prime)
3     168          0.168
4     1229         0.1229
5     9592         0.09592
6     78498        0.078498
7     664579       0.0664579
8     5761455      0.05761455

"""
def sieve_prime_count(n):
    size = 10**n
    isprime = [True]*size
    isprime[0] = isprime[1] = False
    for i in range(2, size):
        if i*i>size:
            break
        if isprime[i]:
            for j in range(i*i, size, i):
                isprime[j] = 0

    count = 0
    for i, flag in enumerate(isprime):
        if flag == True:
            count += 1
    return count

def prime_gap(n):
    print('10^n', ' Prime count ', '% prime')
    for exp in range(1, n+1):
        pc = sieve_prime_count(exp)
        print(exp, '   ', pc, ' '*(8 - len(str(pc))), '  ', pc/10**exp)
# prime_gap(8)
