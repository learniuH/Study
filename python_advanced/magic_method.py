# 声明一个类
class Student:
    def __init__(self, student_list):
        self.student_list = student_list

    # 魔术方法
    def __getitem__(self, item):
        return self.student_list[item]

student = Student(['xiaoming', 'xiaohong', 'xiaohua'])

# 迭代
for stu in student.student_list:
    print(stu)

# 通过魔术方法可以让当前学生列具有序列特性
for stu in student:
    print(stu)

# 还可以使用索引的方式对类进行取值
print(student[1])

'''
总结：
    1、魔术方法可以赋予类不具有的特性
    2、摩书方法是python解释器提供的，不能随意更改魔术方法的方法名
'''