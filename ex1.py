__author__ = 'yyao'

def sumtarget(sourcelist, num):
    result_list =[]
    hashmap = {}
    for i, var in enumerate(sourcelist):
        hashmap[var] = i

    for i1, var2 in enumerate(sourcelist):
        if num-var2 in hashmap:
            ind2 = hashmap[num -var2]
            if ind2 > i1:
                result_list.append([i1+1,ind2+1])

    return result_list

print([1,2,7,4,5,])
s = sumtarget([1,2,7,4,5],6)

for result in s:
    print(result)


