def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped
@makebold
@makeitalic
def hello():
    return "hello world"
print(hello())




def decorator1(func):
    def wrapper():
        print("前")
        func()
    return wrapper
def decorator2(func):
    def wrapper():
        func()
        print("后")
    return wrapper
@decorator1
@decorator2
def test():
    print(1234567890)
test()




def  tool(a = 'abcd'):
    def TT(_f):
        return _f.capitalize()
    def YY(fn = 'efgh'):
        return fn.capitalize()
    if a =="123":
        return TT
    else:
        return YY
print(tool()("hkkkkjk"))


def func(fn):
    def wre():
        print('123')
        print(fn())
        print('456')
    return wre
@func
def tt():
    return '中间'
tt()