# coding=utf-8
'''
介绍 Python 一些常用的魔术函数和其使用
'''

#__init__函数
'''
class A:
    def __init__(self, name):  # 实例方法
        print('开始给对象赋予属性了')
        self.name = name
a = A("hello")
print(a.name)
'''




#__new__函数
'''

class A:
    def __init__(self, name, age=1):  # 实例方法
        print('开始给对象赋予属性了')
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs): # 类方法
        print('开始新建对象了')
        print('我是参数args', args)
        print('我是参数kwargs', kwargs)
        return object.__new__(cls)
        # 必须要有返回值 返回创建出来的实例


a = A('小明', age=2)
print(a.name,a.age)
'''

# 析构函数：__del__

# class A:
#    pass
#
# a = A()
# print(dir(a))


class Base(object):
    def __init__(self,name):
        print('Create Base')
        self.name = name
        print(name)

class A(Base):
    def __init__(self,name):
        # Base.__init__(self)
        # super(A, self).__init__()
        super().__init__(name)
        print('Create A')



print(A("zhang").name)



