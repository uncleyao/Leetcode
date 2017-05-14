__author__ = 'yyao'

"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
"""

def combination(num, target):
    num.sort()
    result = []
    get_combine(target,num,[],result)
    return result

def get_combine(target,num,current,result):
    if not num or sum(current)> target:
        return
    if sum(current)==target:
        result.append(current)
        return

    for ind,var in enumerate(num):
        get_combine(target,num[ind:],current+[var],result)



n = [2,3,6,7]
result = combination(n,7)
print(result)
