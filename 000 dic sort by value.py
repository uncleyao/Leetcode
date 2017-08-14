lis = ['dog','dog','cat','cat','mouse','cat']

n = len(lis)
dic = {}
for w in lis:
    if w in dic:
        dic[w]+=1
    else:
        dic[w]=1
print(dic)

items = dic.items()
items = sorted(items)
print([(key,value) for key, value in items])
