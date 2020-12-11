class my():
    def __init__(self,name,sex,age,address):
        self.name = name
        self.sex = sex
        self.age = age
        self.address = address

    def display(self):
        print('姓名：',self.name)
        print('性别：',self.sex)
        print('年龄：',self.age)
        print('家庭地址：',self.address)

my = my('BOB','男',18,2323)
my.display()