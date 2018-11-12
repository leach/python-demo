
def logger(func):
    def inner(**kwargs):
        print("args:%s" % kwargs)
        return func(**kwargs)
    return inner


@logger
def test1(**kwargs):
    print(kwargs)


@logger
def test2(**kwargs):
    return kwargs


dct = {'x': 1, 'y': 2}
test1(**dct)
test2(**dct)

