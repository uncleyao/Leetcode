__author__ = 'yyao'

########
##Write a funtion to find the longest common prefix string among an array of strings
########
def longestCommonPrefix(strin):
    if not strin:
        return ''

    for i in range(len(strin[0])):
        for str in strin:
            if len(str) <=i or strin[0][i] != str[i]:
                return strin[0][:i]

    return strin[0]


str  = longestCommonPrefix(['hello','helloa','helloo'])
print(str)
