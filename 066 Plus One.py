'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

[1,2,4] ---> [1,2,5]
[9,9] ---> [1,0,0]

'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i]+= carry
            if digits[i]<10:
                carry = 0
                break
            else:
                digits[i]=0
        if carry == 1:
            digits.insert(0,1)
        return digits
