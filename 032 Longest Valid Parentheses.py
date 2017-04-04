__author__ = 'yyao'


def longest(s):
    length = len(s)
    dp = [0 for __ in range(length)]
    for i in range(1,length):
        if s[i] ==')':
            j = i - dp[i-1] -1  ##dp[i-1] is the numbers of parenthesis pair among s[i-1] so j will return the index of sth before xxxx). so it should be (
            if j>=0 and s[j] =='(':
                ## so if it's '(', dp[i] will return the number of parethese pair among s[i]
                dp[i] = dp[i-1] +2
                if j-1>=0:
                    dp[i]+=dp[j-1]   ##also it will add the ones in j-1
    return max(dp)


print(longest('()(()'))
