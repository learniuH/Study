'''
对象的三个特征：
    1、唯一标识符
    2、类型
    3、值
'''
from tabnanny import NannyNag

from openpyxl.descriptors.nested import NestedNoneSet

a = 1
print(id(a))    # 1806219248
print(type(a))  # <class 'int'>
# print(a.__bases__)

def my_func():
    pass

print(id(my_func))
print(type(my_func))    # <class 'function'>
print(my_func)      # 输出的是一种函数对象的表现形式

class MyCalss():
    pass

print(id(MyCalss))
print(type(MyCalss))    # <class 'type'>
print(MyCalss)  # 输出的是类对象的表现形式

# None 类型全局只有一个
data_1 = None
data_2 = None
print(id(data_1) == id(data_2))

