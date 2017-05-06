__author__ = 'yyao'

### https://soulmachine.gitbooks.io/algorithm-essentials/content/java/dfs/generate-parentheses.html

def generateParenthesis(n):
    result = []
    generate(n,n,'',result)
    return result

def generate(left,right,str,result):
    if left == 0 and right == 0:
        result.append(str)
        return
    if left >0:
        generate(left-1,right,str+'(',result)
        ##this part is important, you can only do right > left, b/c you should do valid parenthes
    if right > left:
        generate(left,right-1,str+')',result)

print(generateParenthesis(3))
