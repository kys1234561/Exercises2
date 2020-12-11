class dict():
    def __init__(self,dict1):
        self.dict1 = dict1

    def del_dict(self,key):
        if key in self.dict1:#has_key方法判断后面的参数是不是在对应的集合里面,在 python2中支持
            print(self.dict1.pop(key))
            #print(self.dict1)
        else:
            print('no')

    def get_dict(self,key):
        if key in self.dict1:
            print(self.dict1[key])
        else:
            print('error')

    def get_key(self):
        print(self.dict1.keys())#keys方法是字典的所有键

    def update_dict(self,dict2):
        #self.dict1 = dict(**self.dict1,**dict2)
        self.dict1.update(dict2)#update直接合并字典
        print(self.dict1.values())
        #print(self.dict1.keys())
A = dict({'1':5,'3' :56})
A.del_dict('3')
A.get_dict('4')
A.get_key()
A.update_dict({'9':56})

