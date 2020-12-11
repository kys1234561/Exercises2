class Listinfo():
    def __init__(self, list1):
        self.list1 = list1

    def add_key(self,keyname):
        if isinstance(keyname,(str,int)):#isinstance函数判断变量是否是后面的类型之一
            self.list1.append(keyname)
            return self.list1
        else:
            return "error"

    def get_key(self,num):
        if num >=0 and num <len(self.list1):
            return self.list1[num]
        else:
            return 'error'

    def update_list(self,list2):
        self.list1.extend(list2)
        return self.list1

    def del_key(self):
        if len(self.list1) >= 0:
            return self.list1.pop(-1)#pop函数起删除功能
        else:
            return 'error'
list_info = Listinfo([44,222,111,333,454,'sss','333'])
print(list_info.add_key(000))
print(list_info.get_key(5))
print(list_info.update_list([0,'9']))
print(list_info.del_key())
'''a = [1,2,3,4,5,6,7]
print(a.pop(-1))
print(a)'''

