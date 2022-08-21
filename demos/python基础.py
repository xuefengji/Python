# a = 60
# print(bin(a))
# print(True == 1)

# a = 1
# print("函数outer调用之前全局变量a的内存地址： ", id(a))
# def outer():
#     a = 2
#     print("函数outer调用之时闭包外部的变量a的内存地址： ", id(a))
#     def inner():
#         nonlocal  a   # 注意这行
#         a = 3
#         print("函数inner调用之后闭包内部变量a的内存地址： ", id(a))
#     inner()
#     print("函数inner调用之后，闭包外部的变量a的内存地址： ", id(a))
# outer()
# print("函数outer执行完毕，全局变量a的内存地址： ", id(a))


# a = 10
# # print(id(a))
# def test():
#     # global a
#     a += 1
#     print(id(a))
# test()

# name ='jack'

# def f1():
#     print(name)
#
# def f2():
#     name = 'eric'
#     # def f1():
#      #     print(name)
#     f1()
#
# f2()


# import os
#
# base = "E:\myself"
#
# file_path = os.path.join(base, "test.txt")
#
# print(file_path)
#
# print(file_path.split(base)[1][1:])
#
# os.remove(file_path)

# class A:
#     def __init__(self, name):
#         self.name = name
#         print("父类的__init__方法被执行了！")
#     def show(self):
#         print("父类的show方法被执行了！")
#
# class B(A):
#     def __init__(self, name, age):
#         super(B, self).__init__(name=name)
#         self.age = age
#
#     def show(self):
#         super(B, self).show()
#
# obj = B("jack", 18)
# obj.show()



result = [lambda x: x + i for i in range(10)]
print(result[0])