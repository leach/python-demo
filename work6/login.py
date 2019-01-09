

def login(func):
    def wraper(*args, **kwargs):
        username = input("username:")
        password = input("password:")
        if username == '' and password == '':
            return func(*args, **kwargs)
    return wraper

# @login
# def test():
#     print('test')


def test():
    print(luffy)

luffy = "the king of sea."
# test()

import logging
logging.basicConfig(filename="example.log", datefmt="%d%m%Y i:h:M", format="%(date)s,%(message)s %(lineno)s")
logging.debug("bug ")