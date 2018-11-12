
def func(aa):
    print("func")

    def func_iner():
        a = aa()
        return aa()
    return func_iner


@func
def test():
    return 200


print(test())
