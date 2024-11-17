class Student:
    name = 'cls_name'

    def __init__(self):
        # 实例属性
        self.name = 'obj_name'


# 类中的属性查找是从下网上查找的：先查找构造方法里面的属性，如果没有，就向上到类属性中查找
stu = Student()
print(stu.name)   # obj_name

########################################## 菱形继承 ##########################################
class D:
    name = 'name_d'

class C(D):
    name = 'name_c'

class B(D):
    name = 'name_b'

class A(B, C):
    # name = 'name_a'
    pass

a = A()
print(a.name)
print(A.__mro__)    # 属性的查找顺序：
                    # <class '__main__.A'>,
                    # <class '__main__.B'>, <class '__main__.C'>,
                    # <class '__main__.D'>, <class 'object'>

########################################## 树形继承 ##########################################
class I:
    name = 'name_i'

class H:
    name = 'name_h'

class G(I):
    name = 'name_g'

class F(H):
    name = 'name_f'

class E(F, G):
    name = 'name_e'

e = E()
print(e.name)
print(E.__mro__)    # 树形继承的属性查找与菱形继承查找顺序不同：
                    # <class '__main__.E'>,
                    # <class '__main__.F'>, <class '__main__.H'>,
                    # <class '__main__.G'>, <class '__main__.I'>,
                    # <class 'object'>