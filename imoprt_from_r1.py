import math  # импортируем модуль для работы с математикой
import time  # импортируем модуль для работы со временем
import os  # импортируем модуль для работы с операционной системой


try:
    import nomodule
except ImportError:
    print("no module")

print(math.e)
print(math.pi)
print(math.cos(0))

print(time.time())  # число секунд прошедших с 1 января 1970, 00:00:00
seconds = time.time()
local_time = time.ctime(seconds)
print('local time', local_time)

print(os.getcwd())  # the pass to the program file


