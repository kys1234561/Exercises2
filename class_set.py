class Set(set):
    def __init__(self,set):
        self.set = set

    def add_setinfo(self,keyname):
        if isinstance(keyname,(str,int)):
            self.set.add(keyname)#add方法
            print(self.set)
        else:
            print('error')

    def get_intersection(self,unioninfo):
        if isinstance(unioninfo,set):
            print(self.set & unioninfo)
        else:
            print('error')

    def get_union(self,unioninfo):
        if isinstance(unioninfo, set):
            print(self.set | unioninfo)
        else:
            print('error')
    def del_difference(self,unioninfo):
        if isinstance(unioninfo, set):
            print(self.set - unioninfo)
        else:
            print('error')

set_info =  Set({1,2,3,4,5})
set_info.add_setinfo(78)
set_info.get_intersection({1,2,3,0})
set_info.get_union({1,2,3,0})
set_info.del_difference({1,5,6,89})