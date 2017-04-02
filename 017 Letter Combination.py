__author__ = 'yyao'

digit2letters = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
}

def lettercombine(digits):
    if not digits:
        return []
    result = []
    dfs(digits,'',result)
    return result

def dfs(digits, current, result):
    ## current start with '', reuslt star with [] ,digits is the input
    if not digits:
        result.append(current)
        return

    ##
    for c in digit2letters[digits[0]]:
        dfs(digits[1:],current + c, result)

S = lettercombine('23')
print(S)
