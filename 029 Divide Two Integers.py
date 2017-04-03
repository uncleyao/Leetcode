__author__ = 'yyao'

'''
Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.
'''

def divide(dividend,divisor):

    MAX_INT = 2147483647
    sign  = 1
    if (dividend > 0 and divisor >0) or (dividend < 0 and divisor < 0):
        sign = -1

    dividend = abs(dividend)
    divisor = abs(divisor)

    result = 0
    while divisor <= dividend:
        dividend -= divisor
        result+=1

    while sign > 0:
        return min( result, MAX_INT)
    while sign < 0:
        return max( -result, -MAX_INT)

print(divide(5,-1))
print(divide(10,2))
print(divide(10,-3))
