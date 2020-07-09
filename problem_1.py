n = 1000

def linearInclusionExclusion(n):
    # O(n)

    # sum of multiples of 3
    s3 = 0
    for i in range(3, n+1, 3):
        s3 += i

    # sum of mulitples of 5
    s5 = 0
    for i in range(5, n+1, 5):
        s5 += i
    
    # sum of multiples of 15
    s15 = 0
    for i in range(15, n+1, 15):
        s15 += i

    print(s3 + s5 - s15)

def arithmeticInclusionExclusion(num):
    # O(1)

    # sum of multiples of 3
    l = 3*(num//3)
    n = (l - 3)//3 + 1
    s3 = (3 + l)*n//2

    # sum of multiples of 5
    l = 5*(num//5)
    n = (l - 5)//5 + 1
    s5 = (l + 5)*n//2

    # sum of multiples of 15
    l = 15*(num//15)
    n = (l - 15)//15 + 1
    s15 = (l + 15)*n//2

    print(s3 + s5 - s15)

linearInclusionExclusion(n-1)
arithmeticInclusionExclusion(n-1)
