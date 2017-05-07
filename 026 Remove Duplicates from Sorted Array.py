__author__ = 'yyao'
'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Given input array nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''


def removeDup(nums):
    if not nums:
        return 0
    index = 1
    start = 1
    while start < len(nums):
        if nums[index-1] != nums[start]:
            index+=1
            nums[index-1] = nums[start]
        start+=1
    return index
