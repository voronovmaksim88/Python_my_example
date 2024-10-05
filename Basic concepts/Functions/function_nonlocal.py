def f():
    ok_status = True
    vowels = ["a", "u", "i", "e", "o"]

    def check(word):
        nonlocal ok_status
        # тут мы говорим взять ближайшую переменную ok_status
        # ближайшая в функции f
        for vowel in vowels:
            if vowel in word:
                return True

        ok_status = False
        return False

    print(check("abacaba"))  # True
    print(ok_status)  # True
    print(check("www"))  # False
    print(ok_status)  # False


f()
print(ok_status)  # NameError
