#!/usr/bin/env python3
"""developing the pascal triagle"""


def pascal_triangle(n):
    '''creates pascal's triangle'''
    if n <= 0:
        return []
    result = []
    for i in range(0, n):
        x = str(11 ** i)
        result.append(x)
    return result
