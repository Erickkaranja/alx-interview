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
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
                if i // j != j:
                    dp[i] = min(dp[i], dp[i // j] + j)
    return dp[n]
