from math import ceil
def factorisation(n):
    factors = []
    #  2 is the only even prime, so if we treat 2 separately we can increase factor with 2 every step.

    while n%2==0:
        n >>= 1
        factors.append(2)

    # every number n can **at most** have one prime factor greater than sqrt(n). Thus, we have the upper limit as sqrt(n). If after division with earlier primes, n is not 1, this is the prime factor greater than sqrt(n).
    for i in range(3, ceil(n**0.5) + 1, 2):
        while n%i == 0:
            n //= i
            factors.append(i)
        
    if n!=1:
        factors.append(n) 
        # it has a prime factor greater than sqrt(n)
    return factors

n = 600851475143
print(max(factorisation(n)))


# Proof: Every number n can at most have one prime factor greater than n. https://math.stackexchange.com/questions/1408476/proof-that-every-positive-integer-has-at-most-one-prime-factor-greater-than-its/1408496
