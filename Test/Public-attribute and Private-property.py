class Fun(object):
    def __init__(self):
        self.__name = 1
        self._age = 18


_f = Fun()
# 访问私有属性
print(_f._Fun__name)
# 访问公有属性
print(_f._age)