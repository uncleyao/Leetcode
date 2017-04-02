__author__ = 'yyao'

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},
    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''


def threeSum(nums):
    nums.sort()
    result = []
    i = 0
    while i < len(nums) -2:
        j = i+1
        k = len(nums)-1
        while j <k:
            l = [nums[i],nums[j], nums[k]]
            if sum(l) ==0:
                result.append(l)
                j+=1
                k-=1
                while j< k and nums[j] ==nums[j-1]:
                    j+=1
                while j < k and nums[k] == nums[k+1]:
                    k-=1
            elif sum(l) > 0:
                k-=1
            else: j+=1
        i+=1
        while i < len(nums) -2 and nums[i] ==nums[i-1]:
            i +=1
    return result




S = [-1, 0, 1, 2, -1, -4]
print(threeSum(S))
