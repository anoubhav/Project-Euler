def simulate(n):
    count = 1
    while n!=1:
        if n%2:
            n *= 3
            n += 1
            n>>= 1
            count += 2
        else:
            n>>=1
            count += 1
    return count

def naive(lim):
    maxnum, maxchain = 0, 0
    for start in range(2, lim):
        t = simulate(start)
        if t > maxchain:
            maxchain = t
            maxnum = start
    return maxnum, maxchain

def LargestCollatz(n):
    # Collatz lengths, first entries are 'hand calculated'.
    # cl[i] Stores the chain lengths starting at i.
    cl = [0, 1, 2]
    for i in range(3, n):
        c = i
        length = 0
        while True:
            if c % 2 == 0:
                c = c//2
            else:
                c = 3*c+1
            length += 1

            if c < i:
                cl.append(length + cl[c])
                break
    
    maxcl = max(cl)
    return cl.index(maxcl), maxcl

def countChain(n, values):
    if n in values:
        return values[n]
    else:
        if n&1:
            values[n] = 2 + countChain((3*n+1)//2, values)
        else:
            values[n] = 1 + countChain(n>>1, values)
    return values[n]

# Src: https://projecteuler.net/overview=014
def editorial(n):
    # Using hash map; memoization
    values = {1:1}
    maxnum, maxchain = -1, -1

    # If n is even, then n → n/2 ⇒ Collatz(n) = Collatz(n/2) + 1. Therefore Collatz(2k) > Collatz(k) for all k, and we do not need to compute the chain for any k ≤ LIMIT /2. In this case, we do not need to compute the chain for any k below 500000.

    for num in range(n//2, n):
        chain = countChain(num, values)
        if chain>maxchain:
            maxchain = chain
            maxnum = num
    return maxnum


lim = 10**7
from time import time
# t = time()
# print(naive(lim)) # re-calculates every single time. 16 seconds
# print(time() - t)

# uses precomputation entirely using hash map. 1 second. Unordered dictionary is slow in python, due to overhead cost, and worst case of O(n) key lookup
t = time()
print(editorial(lim)) 
print(time() - t)

# uses precomputation to a certain extent. 1 second. Arrays are always O(1) lookup with low overhead cost.
t = time()
print(LargestCollatz(lim)) 
print(time() - t)

