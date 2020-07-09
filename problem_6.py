n = 1234567654321
def linear(n):
    # linear time
    sum_of_squares = 0
    squares_of_sums = 0
    for i in range(1, n+1):
        sum_of_squares += i**2
        squares_of_sums += i
    print(squares_of_sums**2 - sum_of_squares)
    
def formula(n):
    # constant time
    sum_of_squares = n*(n+1)*(2*n + 1)//6
    squares_of_sums = ((n)*(n + 1)//2)**2
    print(squares_of_sums - sum_of_squares)

# linear(n)
formula(n)

# derivation of sum_of_squares formula (with induction for proof of correctness, very nice): https://projecteuler.net/overview=006