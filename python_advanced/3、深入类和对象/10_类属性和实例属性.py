class A:
    # 类属性
    a = 1

    def __init__(self, b, c):
        # 实例属性
        self.b = b
        self.c = c

a = A(2,3)


'''
实例对象可以访问类属性，类对象无法访问实例属性
'''
# print(A.b, A.c)

# 对类属性的值进行修改
A.a = 11
print(A.a)
print(a.a)

# 能否使用实例对象修改类属性
a.a = 22
print(A.a)  # 实例属性无法修改类属性
print(a.a)  # 当前代码是通过实例对象新建了一个实例属性