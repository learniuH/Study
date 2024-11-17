from collections.abc import Sized
from abc import ABC, abstractmethod
# 判断对象中是否实现了计算长度的方法
class Student:
    def __init__(self, student_list):
        self.student_list = student_list

    def __len__(self, item):
        return self.student_list[item]

student = Student(['guan', 'anna'])
print(hasattr(student, '__len__'))

print(isinstance(student, Sized))



# 自己开发一个web框架，在框架中实现了缓存的功能
class Cache(ABC):
    @abstractmethod
    def get_cache(self):
        pass
    @abstractmethod
    def set_cache(self, value):
        pass

class TuLingOnline(Cache):
    def get_cache(self):
        pass

tuling = TuLingOnline()
'''
必须重写 abstractmethod里面的方法
'''