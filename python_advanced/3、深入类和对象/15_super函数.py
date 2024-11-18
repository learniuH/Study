'''
1、 super函数的作用: 调用'父类'的方法
2、 什么场景下使用 super 函数: 在代码重用的场景下使用
3、 super函数的运行过程: 正确的理解不是简单的调用一个类的父类，而是根据一个类中的mro顺序进行查询并调用
'''

# class A:
#     def __init__(self):
#         print('a')
#
# class B(A):
#     def __init__(self):
#         print('b')
#         # 方式一, 通过使用父类的类对象调用 init 函数
#         # A.__init__(self)
#         # 方式二, 通过super函数
#         super().__init__()
#
# b = B()


# 需要创建一个类, 让类具有多线程执行的特征
import threading

class MyThread(threading.Thread):
    def __init__(self, thread_name, user):
        self.user = user
        # 可以重用线程类中定义的属性
        super().__init__(name=thread_name)


class D:
    def __init__(self):
        print('d')

class C(D):
    def __init__(self):
        print('c')
        super().__init__()

class B(D):
    def __init__(self):
        print('b')
        super().__init__()

class A(B, C):
    def __init__(self):
        print('a')
        super().__init__()  # 并不是调用一个类的父类方法，而是调用一个类的 mro 列表顺序

a = A()
print(A.__mro__)