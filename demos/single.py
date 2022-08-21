# @Time: 2022/4/16 21:46
# @Author: xuef
# @File: single.py
# @Desc:

# 单例模式1
# class A:
#     pass
#
# a = A()
#
# a1 = a
# a2 = a
# a3 = a
# print(id(a1))
# print(id(a2))
# print(id(a3))

# 使用 __new__ 方法
# class A:
#     def __new__(cls, *args, **kwargs):
#         print('__new__ is call')
#         if not hasattr(cls,"_instance"):
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __init__(self):
#         print('__init__ is call')
#     def __call__(self, *args, **kwargs):
#         print('call')
#
# a1 = A()
# a2 = A()
# a1()
# a3 = A()
# print(id(a1))
# print(id(a2))
# print(id(a3))


# Fa = type("FOO",(object,),{"v1":123, "func": lambda self:666})
#
# obj = Fa()
#
# print(obj.v1)
# print(obj.func())


class A:
    pass

print(type(A))









