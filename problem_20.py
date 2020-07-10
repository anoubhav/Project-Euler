def BigNumber(n):
    # Python can handle numbers of arbitrary size; Unlike languages like C++, where special big number libraries are required.
    from math import factorial
    num = str(factorial(n))
    ans = 0
    for i in num:
        ans += int(i)
    return str(factorial(n)), ans

def multiply(n):
    from math import log10
    # get an upper bound on the size(number of digits) of n!. log(n!, 10) < log(n^n, 10) = n log(n, 10)
    size = n*(int(log10(n)) + 1)
    digits = [0]*size
    digits[0] = 1

    for num in range(1, n+1):
        carry = 0
        for i in range(size):
            temp = digits[i]*num + carry
            carry = temp//10
            digits[i] = temp%10

    # Remove the ending zeros
    for i in range(size-1, -1, -1):
        if digits[i]!=0:
            break
    digits = digits[:i+1]
    # Print the factorial and sum of digits
    factorial = ''
    ans = 0
    for dig in range(len(digits)-1, -1, -1):
        ans += digits[dig]
        factorial += str(digits[dig])
    return factorial, ans

n = 400
ans1, ans2 = BigNumber(n), multiply(n)
assert ans1[0] == ans2[0]
print(ans1[1])
print(ans2[1])

