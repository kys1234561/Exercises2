def str_reverse(str):
    lists = list(str)
    lists.reverse()#reverse是反向列表中元素
    new_str = ''.join(lists)#用join函数来连接函数
    print(new_str)


def str_reverse2(str):
    print(str[::-1])#等价于print(str[-1:-7:-1])
str = "string"
#str_reverse(str)
#str_reverse2(str)