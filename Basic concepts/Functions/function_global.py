ok_status = True
vowels = ['a', 'e', 'i', 'o', 'u']


def chek(word):
    global ok_status
    for vowel in vowels:
        if vowel in word:
            return True
    ok_status = False
    return False


print('hello', chek('hello'))
print('ok_status', ok_status)
print('QWRT', chek("QWRT"))
print('ok_status', ok_status)
