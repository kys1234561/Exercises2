alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]
for i in range(len(alist)-1):
    for j in range(i,len(alist)):
        if alist[i]['age'] < alist[j]['age']:
            blist = alist[i]
            alist[i] =alist[j]
            alist[j] =blist
print(alist)