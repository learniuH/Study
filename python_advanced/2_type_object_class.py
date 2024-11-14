######################################### type object class 三者的关系 #########################################
a = 1
b = 'abc'

# type 可以判断一个对象的类型, 并且 type 也可以用于创建类
print(type(a))  # <class 'int'>

# 一切皆对象, 对象是由类创建出来的
print(type(int))    # <class 'type'>

'''
python 中的数据类型是由类型类创建出来的
python 中的类型是由 type 创建出来的
'''
print(type(b))          # <class 'str'>
print(type(str))        # <class 'type'>

'''
python 中所有的对象是由 type 创建的
'''
class Student:
    pass

class MyStudent(Student):
    pass

stu = Student()
print(type(stu))    # <class '__main__.Student'>
print(type(Student))    # <class 'type'>

my_stu = MyStudent()
print(type(my_stu))         # <class '__main__.MyStudent'>
print(type(MyStudent))      # <class 'type'>

# 探究python中的 object
print(int.__bases__)    # 查询一个类的继承关系 (<class 'object'>,)
print(str.__bases__)    # (<class 'object'>,)

print(Student.__bases__)    # (<class 'object'>,)   在 python3 中, 自定义的类如果没有写继承关系, 就默认继承 object
print(MyStudent.__bases__)  # (<class '__main__.Student'>,)

# type 创建了所有的对象, object 也是一个对象
print(type(object))     # object 也是被 type 创建的
print(type.__bases__)   # (<class 'object'>,)   type 本身也继承了 object

'''
object 是被 type 创建的
type 继承了 object 
'''

print(object.__bases__)     # ()  object 是所有类的基类

'''
1、type 创建了所有类的对象, 也包含类对象(object)
2、type 在创建object基类同时也继承了object
3、type 是由自身创建的
'''
# 探究 type 本身是被谁创建的
print(type(type))       # <class 'type'>
