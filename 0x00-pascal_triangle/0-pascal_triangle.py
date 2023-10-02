#!/usr/bin/python3
"""developing the pascal triagle"""

def pascal_triangle(n):
    '''creates pascal's triangle'''
    if n <= 0:
        return []
    for i in range(0, n):
        val = 1
        for j in range(0, i + 1):
            print(val, end=" ")
            val = val * (i - j) // (j + 1)
        print()
