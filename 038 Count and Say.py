"""
At the beginning, I got confusions about what is the nth sequence. Well, my solution is accepted now, so I'm going to give some examples of nth sequence here. The following are sequence from n=1 to n=10:

 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
 10.   13211311123113112211
 """


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = "1"
        for i in range(1,n):
            string = self.singlesay(string)
        return string
        
    def singlesay(self,nums):
        result = ""
        i = 0
        while i < len(nums):
            j = i+1
            count = 1
            while j < len(nums) and nums[j]==nums[i]:
                j+=1
                count+=1
            result+=str(count)+str(nums[i])
            i = j
        return result
