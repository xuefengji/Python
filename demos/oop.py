class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.__score = score

    def print_score(self):
        print(self.name,self.__score)

if __name__=='__main__':
    stu = Student('lisa',89)
    print(stu.__score)
    stu.print_score()
    print(stu.__dir__())