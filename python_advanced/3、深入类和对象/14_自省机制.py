'''
自省机制：
    检测一个类的内部结构
'''

class Person:
    name = 'user'

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


stu = Student('tinghua')

# 查询这个对象中包含的属性
print(stu.__dict__)     # 查找到的是实例属性, 对象包含的实例属性是不包括类对象属性的
print(Person.__dict__)

# python 中对象都具有一个特殊的属性： __dict__ 只能查询属于自身的属性
stu.__dict__['address'] = 'beijing'     # 可以通过 __dict__ 创建属性
print(stu.address)

# dir函数可以查询一个对象中的所有属性和方法，包含这个对象的父类
print(dir(stu))     # 返回的是 list