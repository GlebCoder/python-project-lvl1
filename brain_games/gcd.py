#!usr/bin/env python
# it is an algorithm to find the greatest common denominator for two integers


def gcd(n1, n2):
    # Finding the minimum number to make sure x <= y
    if n1 <= n2:
        x = n1
        y = n2
    else:
        x = n2
        y = n1
    
    result = 1
    index = x
    while index >= 1:
        if ((y % index) == 0) and ((x % index) == 0):
            result = index
            return print(result)
        index -= 1
    