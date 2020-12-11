class Student():
    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_scores(self):
        print(max(self.scores))

zm = Student('zhangming', 20, [69,88,100])
zm.get_name()
zm.get_age()
zm.get_scores()