#!/usr/bin/python3
'''calculating minimum number of operations to execute.'''


def minOperations(n):
    '''creates a function to get minimum operation.
       args:
           n (int): integer input.
       Returns:
           the minimum numder of operation.
    '''
    if n <= 1:
        return 0
    i = 2
    prime_factors = []
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        prime_factors.append(n)
    if prime_factors == [1, n]:
        return (sum(prime_factors) - 1)
    else:
        return sum(prime_factors)
