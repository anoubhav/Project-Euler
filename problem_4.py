def ispalindrome(num):
    if num%10 == 0:
        return False
    # O(N)
    rev = 0
    while rev < num:
        rev = 10*rev + num%10
        num//=10
    
    if rev//10 == num or rev == num:
        return True
    else:
        return False

# Optimisations:
# -  we can assume a ≤ b
# -  we should consider counting downwards from 999 instead of counting upwards from 100.
# - stop checking a and b that would be too small to improve upon the largest palindrome found so far. (break statement)

def optimised(n):
    # O(N^3) solution worst case. Where N = 10^n.
    maxnum = 10**n - 1
    minnum = 10**(n-1)
    ans = 0
    # O(N^2)
    # The order in which we are checking is very important for fast solution.
    for num1 in range(maxnum, minnum-1, -1):
        for num2 in range(maxnum, num1-1, -1): # very important optimisation.
            prod = num1*num2
            # order is important for speed.
            if prod > ans:
                if ispalindrome(prod): 
                    ans = prod
            else: break # without this ; TLE
    return ans

def using_math():
    # O(9^3 * 90)
    # The palindrome can be written as
    # 11(9091a + 910b + 100c) = mn
    # a,b & c being 1 digit integers and m & n being 3 digit intergers.

    # Let 11 * 10 < m < 11 * 90; ( As 11*91 = 1001, 4 digits)
    for a in range(9, 0, -1):
        for b in range(9, -1, -1):
            for c in range(9, -1, -1):
                num = (9091*a + 910*b + 100*c) # a palindrome
                for divider in range(90, 9, -1):
                    if num%divider == 0:
                        # m only reduces in next iteration making n larger than 999
                        if num//divider > 999: 
                            break 
                        else:
                            result = num*11
                            return result
                    
def math_optimised():
# Src: https://projecteuler.net/thread=4#1211
    max = maxI = maxJ = 0
    i = 999
    j = 990
    while (i > 100):
        j = 990
        while (j > 100):
            product = i * j
            if (product > max):
                productString = str(product)
                if (productString == productString[::-1]):
                    max = product
                    maxI = i
                    maxJ = j
            j -= 11
        i -= 1
    return max, maxI, maxJ

numdigits = 3
# works for any n
print(optimised(numdigits))

# only works for question statement
print(using_math())
print(math_optimised())


# On checking the outputs for numdigits = 2, 3, 4, 5, 6.
# It is observed that when n is even. Answer is : 9's (n/2 times) 0's (n times) 9's (n/2 times)