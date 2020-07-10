def combinatorics(n):
    # O(N) to calculate factorial
    from math import factorial
    a = factorial(2*n)
    b = factorial(n)
    return (a//(b*b))

def memoization(x, y):
    # O(N^2)
    if memo[x][y]!=-1:
        return memo[x][y]
    else:
        if x == n or y == n:
            return 1
        else:
            memo[x + 1][y] = memoization(x + 1, y)
            memo[x][y +1] = memoization(x, y + 1)
            return memo[x + 1][y] + memo[x][y + 1]

def iteration(n):
    # O(N^2) time complexity; O(N^2) space complexity
    # By inspection, the number of routes from (0, 0) to (m, n) is equal to the number of routes from (0, 0) to (m − 1, n) plus the number of routes from (0, 0) to (m, n − 1). 
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[0][i] = 1
        dp[i][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n][n]

n = 100
print(combinatorics(n)) # 1ms; O(N) time and O(1) space

memo = [[-1]*(n+1) for _ in range(n+1)]
print(memoization(0, 0)) # 1ms; O(N^2) time and space

print(iteration(n)) # 1ms; O(N^2) time and space
    