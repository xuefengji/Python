class Student(object):
    count = 0
    def __init__(self,name,score):
        self.name = name
        self.__score = score

    def print_score(self):
        print(self.name,self.__score)

class Animal(object):
    def __init__(self,name):
        self.name = name

    def run(self):
        print('%s is run' %self.name)

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__('Dog1')
        # Animal.__init__(Animal,'Dog')
        # self.name = name


if __name__=='__main__':
    # stu = Student('lisa',89)
    # stu.print_score()
    # print(stu.__dir__())
    dog = Dog()
    dog.run()