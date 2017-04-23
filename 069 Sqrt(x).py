__author__ = 'yyao'

'''
Implement int sqrt(int x).
Compute and return the square root of x.
'''

def mySqrt(x):
    newx = [i for i in range(x+1) if i*i <= x]
    return newx[-1]

print(mySqrt(0))
print(mySqrt(1))
print(mySqrt(4))
print(mySqrt(82))
print(mySqrt(100))
