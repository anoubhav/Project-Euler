def iteration(digits):
    a, b = 1, 1
    index = 2
    while len(str(b))<digits:
        a, b = b, a + b
        index += 1
    return index

# Src: https://projecteuler.net/thread=25;post=132866. "The beauty of this solution is that the use of logarithms negates the need for exponentiation or dealing with extremely large values"

def general_formula(digits):
    # The nth term of the fibonacci sequence is given by Binet's formula.
    # floor(log10(round(((phi**n) - (1-phi)**n)/ sqrt5))) + 1 >= digits?

    # (1 - phi)**n can be approximated as 0 for  large n (0.XXX power large n ~ 0). This leaves us with log10( (phi**n)/ sqrt5) ) > digits - 1
    # n log phi - log sqrt 5 > digits - 1
    # n > ( 999 + log sqrt 5 )/ log phi
    
    # set the precision of division, phi, sqrt 5.
    from decimal import Decimal, getcontext
    getcontext().prec = 50
    sqrt5 = Decimal(5).sqrt()
    phi = (1 + sqrt5)/Decimal(2.0)

    from math import ceil, log10
    return ceil((digits - 1 + log10(sqrt5))/log10(phi))



digits = 6000
from time import time
t = time()
print(iteration(digits)) # 6 seconds for 6000 digits
print(time() - t)

t = time()
print(general_formula(digits)) # 5 ms for 6000 digits
print(time() - t)