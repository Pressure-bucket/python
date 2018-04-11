def _fn():
    num_list = []
    [num_list.append((a*100+b*10+c)) if (a*100+b*10+c)==(a**3+b**3+c**3) else False for a in range(1,10) for b in range(0,10) for c in range(0,10)]
    print(num_list)
_fn()