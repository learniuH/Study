class A:
    pass

class B(A):
    pass

b = B()

# 判断传入的对象是否是指定的类型
# 判断的对象也参考类的继承关系
print(isinstance(b, B))
print(isinstance(b, A))

# == 是判断两个值是否相等
print(type(b) == B)
print(type(b) == A)

# is 判断的是内存地址
print(type(b) is B)
print(type(b) is A)