__author__ = 'yyao'

'''
Given an array and a value, remove all instances of that value in place and return the new length.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''


def removeElement(nums, val):
    if not nums:
        return 0

    left = 0
    right = len(nums)-1

    while left <=right:
        while left <= right and nums[left] != val:
            left+=1
        while left <= right and nums[right] == val:
            right-=1
        if left < right:
            left+=1
            right-=1
    return right +1


def removeElement2(nums, val):
    if not nums:
        return 0
    index = len(nums)
    for i in range(len(nums)):
        if nums[i] == val:
            index-=1

    return index



print(removeElement([1,2,3,4,5,2,1,2,2,2],1))

print(removeElement2([1,2,3,4,5,2,1,2,2,2],1))


