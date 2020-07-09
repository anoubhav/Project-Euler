def naive(n):
    # Time complexity: O(N^2)
    for a in range(1, n//3):
        for b in range(a+1, n//2):
            c = n - a - b
            if (a**2 + b**2) == c**2:
                print(a, b, c)
                return a*b*c

# -------------------------------------------------------------------------------

def math():
    # O(N)

    # Solve the equations a + b + c = 1000 and a^2 + b^2 = c^2 by eliminating c.
    # a = 1000*(500-b) / (1000 - b). Since a needs to be a natural number (given)

    for b in range(1, 500):
        if (1000*(500-b))%(1000-b) == 0:
            a = (1000*(500-b))//(1000-b)
            c = 1000 - a - b
            return a*b*c
print(math())

# -------------------------------------------------------------------------------
## General solution (Much faster than naive. Works upto 10^10. Naive is slow after 10^3)

def gcd(b, a):
    if a:
        return gcd(a, b%a)
    return b

def paramterisation(s):
    # https://projecteuler.net/overview=009
    # - For all pythagorean triplets, gcd(a, b) = gcd(b, c) = gcd(a, b)
    # - For primitive pythagorean triplet, gcd(a, b) = 1.
    # - Primitive pythogorean triplets can be represented as a = m^2 - n^2, b = 2*m*n, c = m^2 + n^2
    # - Many more facts about pythagorean triplets, check out editorial. Very cool.
    ans = []
    s2 = s//2
    mlimit = int(s2**0.5) + 1
    for m in range(2, mlimit):
        s2m = s2//m
        while s2m%2:
            s2m>>=1
        if m%2: k = m+1
        else: k = m+2

        while k<2*m and k<=s2m:
            if s2m%k == 0 and gcd(m, k) == 1:
                d = s2//(k*m)
                n = k - m
                a = (m**2 - n**2)*d
                b = 2*m*n*d
                c = (m**2 + n**2)*d
                ans.append((a, b, c))
                # return a*b*c
            k += 2
    return ans

n = 10**8
answers = paramterisation(n)
for triplet in answers:
    print(*triplet)
# print(naive(n)) # very slow after 10^4.
