def test_rek(lst: list, i):
    if len(lst) == 3:
        return lst
    else:
        i = i + 1
        lst.append(i)
        return test_rek(lst, i)


print("тест рекурсии", test_rek(list(), 0))