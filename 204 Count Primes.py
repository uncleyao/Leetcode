__author__ = 'yyao'

'''
Description:
Count the number of prime numbers less than a non-negative number, n.
'''

def countPrimes(n):
    if n <3:
        return 0
    if n == 3:
        return 1
    current = 1
    if n > 3:
        for s in range(3,n,2):
            indic = 0
            for i in range(2,s//2):
                if s % i == 0:
                    indic +=1
            if indic == 0:
                current +=1

    return current

print('1 has: ',countPrimes(1))
print('2 has: ',countPrimes(2))
print('3 has: ',countPrimes(3))
print('4 has: ',countPrimes(4))
print('5 has: ',countPrimes(100))
