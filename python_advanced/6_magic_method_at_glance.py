
class Student:
    def __str__(self):
        return '__str__这是我自定义的一个学生类'

    def __repr__(self):
        return '__repr__这是我自定义的学生类'

stu = Student()
stu     # 直接对实例对象进行测试会调用__repr__方法

print(stu)  # print 方法会自动调用__str__方法
