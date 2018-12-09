class Singleton(object):

    def __init__(self):
        self.attr1 = "test"

    def __new__(cls):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


obj1 = Singleton()
obj2 = Singleton()

print(obj1.attr1, obj2.attr1)
print(obj1 is obj2)