def func1(l):
    s = set(l)
    print(s)
    s = list(s)
    print(s)

def func2(l):
    l1 = []
    for inter  in l:
        if inter not in l1:#not是逻辑词
            l1.append(inter)
    print(l1)


list1 = [1,2,3,4,5,6,2,3,1,3]
func1(list1)
func2(list1)