__author__ = 'yyao'

class Solution(object):
    def isValid(self,s):
        if len(s) %2 == 1:
            return False
        stack = []
        left =['(','[','{']
        right = [')',']','}']

        for v in s:
            if v in left:
                stack.append(v)  ##load all left parenthesis
            else:
                if not stack:
                    return False
                p = stack.pop() ##look at last left par, which should be the first right par
                if left.index(p) != right.index(v):  ##
                    return False

        return len(stack) == 0

assert Solution().isValid('({}){}') == True
assert Solution().isValid("({)}") == False
assert Solution().isValid("}}}") == False
assert Solution().isValid("(((") == False
