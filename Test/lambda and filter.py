from functools import reduce

def g(a):
    print(*filter(lambda x : x % 2 == 0, a))
    print(*filter(lambda x: x in range(len(a)), a))
    print(*map(lambda x : x**2, a))
    print(reduce(lambda x, y: x + y, a))


g(a=[1, 2, 3, 435, 2145, 245])