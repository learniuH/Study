class Student:
    address = 'beijing'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'{self.name}, {self.age}, {self.gender}'

    def set_info(self):
        self.age += 1

    @staticmethod
    def parse_from_string_1(stu_info):
        name, age, gender = tuple(stu_info.split(','))
        return Student(name, age, gender)

    @classmethod
    def parse_from_string_2(cls, stu_info):
        name, age, gender = tuple(stu_info.split(','))
        print(cls.address)
        return cls(name, age, gender)


# 实例方法
stu = Student('LearniuH', 18, 'male')
print(stu)

stu.set_info()
print(stu)

# 静态方法
# 类对象可以访问静态方法
stu_1 = Student.parse_from_string_1('LearniuH,20,male')
print(stu_1)

# 类方法
stu_2 = Student.parse_from_string_2('LearniuH,23,male')
print(stu_2)

'''
实例方法：
    方法中的第一个参数是 self, 实例方法可以访问类中的所有属性和方法

静态方法：
    场景：在文件中保存了一些学生的信息，需要将文件中的信息导入到类中进行处理 '学生姓名，年龄，性别'
    静态方法无法访问类中的属性
    
类方法：
    可以被类对象和实例对象调用, 类方法可以访问类属性
    
如果你当前的需求不需要创建实例对象并且不需要访问实例属性/类属性的情况可以使用静态方法
如果你当前的需求不需要创建实例对象但是需要访问类属性的情况下可以优先使用类方法
如果你需要实例对象并且需要访问类中的所有属性和方法的情况下则使用实例方法
'''
