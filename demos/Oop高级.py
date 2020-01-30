class Student:
    @property
    def show(self):
        return self._name

    @show.setter
    def show(self,value):
        self._name = value

# stu = Student
# stu.show = 'kisa'
# print(stu.show)

class Stu(object):
    def __init__(self):
        self.name = 'Michael'

    def __str__(self):
        return 'Student object (name: %s)' % self.name


stu = Stu()
print(stu)