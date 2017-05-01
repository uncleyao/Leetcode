'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''

def containsDuplicate(nums):
    if not nums:
        return False
    if len(nums)!=len(set(nums)):
        return True
    return False

nums = [1,2,3,2]
print(containsDuplicate(nums))
