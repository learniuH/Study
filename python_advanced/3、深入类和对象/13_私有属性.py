class Person:
    def __init__(self, name, money):
        self.name = name
        # 在实例属性的前面加上 __, 该属性就变成了私有属性
        self.__money = money

    # 在类的内部可以访问私有属性, 同样的在实例方法的前面加上 __, 就变成了私有方法
    def get_money(self):
        print(self.__money)

p = Person('LearniuH', 10000)
p.get_money()

'''
私有属性无法在一个类的外部使用

如何在一个类的外部取访问私有属性?
'''

# 私有属性在创建时会对当前属性的名称进行处理： _clsname__attrname
print(p._Person__money)     # 通过这样的方式可以访问到对象的私有属性
