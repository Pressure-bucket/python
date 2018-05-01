def _f(*args, **kwargs):
    for a, b, c in args:
        print(a, b, c)
    for d, e in kwargs.items():
        print(d, e)


_f([1, 2, 3], a='11', b='22', c='33')


def _func(name, age):
    print('%s:%s' % (name, age))


list = ['python', 18]
_func(*list)


def _function(**kwargs):
    for c, d in kwargs.items():
        print("%s:%s" % (c, d))


my_dic = {'name':'python', 'age':18}
_function(a=1)
_function(**my_dic)
