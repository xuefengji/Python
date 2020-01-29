class Student:
    @property
    def show(self):
        return self._name

    @show.setter
    def show(self,value):
        self._name = value

stu = Student
stu.show = 'kisa'
print(stu.show)