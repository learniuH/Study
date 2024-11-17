'''
鸭子类型：
    在多个类中实现同一个方法，那么这些类可以看成同一个类型
'''

class Cat:
    def say(self):
        print('我是猫...')

class Dog:
    def say(self):
        print('我是狗...')


class Duck:
    def say(self):
        print('我是鸭子...')

animal = Dog
animal().say()

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


class Student:
    def __init__(self, student_list):
        self.student_list = student_list

    def __getitem__(self, item):
        return self.student_list[item]

cls_student = Student(['nihao', 'wohao', 'dajiahao'])
new_student = ['haha']

student_tuple = ('liming', )
new_student.extend(student_tuple)
print(new_student)

new_student.extend(cls_student)
print(new_student)

'''
只要多个类实现了同一个方法，那么就可以归为一类
'''

class Animal:
    def run(self):
        print('动物在跑')

class Dog(Animal):
    def run(self):
        print('狗在跑')

class Cat(Animal):
    def run(self):
        print('猫在跑')

'''
在多个类同时继承了一个类并且对父类中的方法进行了重写
    在每个类中调用的同一个方法会返回不同的行为
    
    这种情况就是多态
'''

