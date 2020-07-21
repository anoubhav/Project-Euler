def get_divisors_sum(n):
    # Time complexity O(sqrt N)
    if n == 1:
        return 0
    divs = [1]
    sqrtn = n**0.5
    if n&1: start, step = 3, 2
    else: start, step = 2, 1

    for i in range(start, int(sqrtn) + 1, step):
        if n%i == 0:
            divs += [i, n//i]
    
    totsum = sum(divs)
    if int(sqrtn)**2 == n:
        totsum -= sqrtn

    return int(totsum)

def brute(limit):
    # Overall time complexity: O(N sqrt(N))
    ans = 0
    for i in range(2, limit):
        divsum = get_divisors_sum(i)
        if divsum <= i or divsum>limit: continue
        if get_divisors_sum(divsum) == i:
            ans += i + divsum
    return ans

# -------------------------------------------------------------------
# Using sieve (my approach). Time complexity: O(N log N)
def sieve_optimized(limit):
    # Preprocessing step takes O(N log log N) time complexity.
    n = limit
    # Filimitd all primes upto n  (including n)
    sievebound = (n-1)//2
    sieve = [-1]*(sievebound + 1)
    # sieve[0] = True
    crosslimit = (int(sievebound**0.5) - 1)
    for i in range(1, crosslimit + 1):
        if sieve[i] == -1:
            for j in range(2*i*(i+1), sievebound + 1, 2*i+1):
                sieve[j] = 2*i + 1
    return sieve

def get_divisors_sum_sieve(n, sieve):
    # Factorisaton query takes O(log N) time after preprocessing.
    number = n
    divs = []
    while n!=1:
        if n&1:
            div = sieve[(n-1)//2]
            if div == -1:
                divs.append(n)
                break
            else:
                n //= div
                divs.append(div)
        else:
            n >>= 1
            divs.append(2)

    freqdict = {}
    for prime in divs:
        freqdict[prime] = freqdict.get(prime, 0) + 1

    totsum = 1
    for prime, freq in freqdict.items():
        totsum *= ((prime**(freq+1) - 1)//(prime - 1))
    return totsum - number


def optimised(limit):
    ans = 0
    sieve = sieve_optimized(limit+1000)
    for i in range(1, limit):
        divsum = get_divisors_sum_sieve(i, sieve)
        if divsum <= i or divsum>limit: continue
        if get_divisors_sum(divsum) == i:
            ## print the amicable pairs
            # print(i, divsum) 
            ans += i + divsum
    return ans

# -------------------------------------------------------------------
# Using sieve discussions tab. Src: https://projecteuler.net/thread=21;post=299496
def sieve_fastest(limit):
    n =limit

    s = [1]*(n+1)
    s[0], s[1] = 0, 0
    total = 0

    for i in range(2, int(n**0.5)+1):
        s[i*i] += i
        for j in range(i*i+i, n+1, i):
            s[j] += i + j//i

    for i in range(2, limit):
        if s[i] < i:
            if i == s[s[i]]:
                total += s[i] + i

    return total

limit = 30000
from time import time
t = time()
print(brute(limit)) # 
print(time() - t)

t = time()
print(optimised(limit))
print(time() - t)

t = time()
print(sieve_fastest(limit))
print(time() - t)


