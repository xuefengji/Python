# class Student:
#     @property
#     def show(self):
#         return self._name
#
#     @show.setter
#     def show(self,value):
#         self._name = value
#
# # stu = Student
# # stu.show = 'kisa'
# # print(stu.show)
#
# class Stu(object):
#     def __init__(self):
#         self.name = 'Michael'
#
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#
#
# stu = Stu()
# print(stu)


class A:
    def __init__(self):
        print("__init__ called")

    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        if not hasattr(cls,"_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance




a1 = A()
a2 = A()
a3 = A()
print(a1)
print(a2)
print(a3)


