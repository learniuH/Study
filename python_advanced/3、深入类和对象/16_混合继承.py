class Animal:
    def __init__(self, name):
        self.name = name

class RunMinin:
    def run(self):
        print(f'{self.name} is running...')



class SwimMinin:
    def swim(self):
        print(f'{self.name} is swimming...')


class FlyMinin:
    def fly(self):
        print(f'{self.name} is flying...')

class Duck(Animal, RunMinin, SwimMinin, FlyMinin):
    pass

duck = Duck('duck')
duck.run()
duck.swim()
duck.fly()

'''
当前的继承方式是一种混合继承
    1. mixin功能是单一的
    2.mixin类不继承其他的类（除了object）
    3.通过self调用子类的一些属性

mixin因为功能简单，并且没有复杂的继承关系，特别好管理
我们在使用mixin的时候尽量避免在子类中使用super

django-reset-framework中经常会使用到混合继承
'''