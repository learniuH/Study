'''
python数据结构中的一些重要特殊方法包括 __init()__, __repr__(), __str()__, __eq__(), __lt__(), __len__(), __getitem__()等
这些方法定义了python对象的基本行为，例如如何创建对象，如何表示对象，如何比较对象，如何迭代对象，如何获得对象的长度等等
'''
class Student:
    def __init__(self, student_list):
        self.student_list = student_list

    def __getitem__(self, item):
        return self.student_list[item]

    def __len__(self):
        return len(self.student_list)

    def __str__(self):
        return '这是我自己定义的一个类，并且可以进行迭代，切片等等'

stu = Student(['xiaoming', 'xiaohong', 'xiaohua'])

# 获取实例对象中元素的长度
print(len(stu))

#
print(stu)