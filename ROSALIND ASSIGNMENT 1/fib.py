def rec_fib(n,k):
    if n == 0:
        return 0
    if n == 1:
        return 1 
    else:
        prob = rec_fib(n-1,k) + k*rec_fib(n-2,k)
        return prob

print(rec_fib(36,3))   