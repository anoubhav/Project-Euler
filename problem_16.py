def mysoln(n):
    s = 0
    num = str(2**n)
    for i in num:
        s += int(i)
    return s

def oneliner(n):
    return sum(map(int, str(2**n)))

# For languages which can't handle large integers like C++, this question is solved by carrying out the multiplication using arrays to store the large number, where each element of the array represents a digit.

print(oneliner(1000))