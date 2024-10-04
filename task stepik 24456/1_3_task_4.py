def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    print(res)
    return res


s(11, 10, b=10)  # 31
# s(b=31, 0)  # error
s(21)  # 31
s(11, 10, 10)  # 41
