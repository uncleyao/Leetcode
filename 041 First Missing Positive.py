__author__ = 'yyao'


## http://www.cnblogs.com/yuzhangcmu/p/4200096.html
class Solution(object):
    def findmissing(self,nums):
        if not nums:
            return 1
        i = 0
        length = len(nums)
        while i < length:
            current = nums[i]
            if current <= 0 or current > length or nums[current-1] == current:  ##check nums[i] if nums[i]! =i+1
                i += 1
            else:
                ##check if i+1 == nums[i] it should be 1 = nums[0], 2= nums[1] ....
                ## if not we swith, so num[nums[i]-1] = nums[i]
                nums[current-1],nums[i] = nums[i],nums[current-1]


        for i in range(length):
            if nums[i] != i+1:
                return i +1
        return length +1

if __name__ == '__main__':
    assert Solution().findmissing([1,2,0]) ==3
