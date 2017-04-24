class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1,n+1):
            if i % 3 ==0 and i %5 ==0:
                result.append("FizzBuzz")
            elif i %3 == 0 and i%5 != 0:
                result.append("Fizz")
            elif i % 5 == 0 and i % 3 != 0:
                result.append("Buzz")
            else:
                result.append("%d" %i)  ####that's how we append number as a string into list
        return result
        
