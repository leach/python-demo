def add(x, y):
    return x + y


lst = [1, 2]
a = add(*lst)


def show(**kwargs):
    print(kwargs)


def show_add(x, y):
    print(x + y)


dct = {'x': 1, 'y': 2}
show_add(**dct)
