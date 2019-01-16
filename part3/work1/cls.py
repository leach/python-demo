class Parent1:
    var = 1
    pass


class Class1(Parent1):
    var = 2
    pass

class Class2(Parent1):
    var = 3
    pass

class Class3(Class1, Class2):
    var = 4
    _var = 1
    pass

    def __init__(self):
        self.name = '1'

class Class4(Class3, Class1, Class2):
    pass

if __name__ == '__main__':
    print(Class4.mro())
    print(Class4._var)
