"""
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be
less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

__author__ = 'yyao'

def sumtarget(sourcelist, num):
    result_list =[]
    hashmap = {}
    for i, var in enumerate(sourcelist):
        hashmap[var] = i

    for i1, var2 in enumerate(sourcelist):
        if num-var2 in hashmap:
            ind2 = hashmap[num -var2]
            if ind2 > i1:
                result_list.append([i1+1,ind2+1])

    return result_list

s = sumtarget([1,2,7,4,5],6)

for result in s:
    print(result)


