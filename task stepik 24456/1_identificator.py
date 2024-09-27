x = [1, 2, 3]
z = [1, 2, 3]
print(id(x))
y = x
print(id(y))
print(y is [1, 2, 3])  # False Переменная y не ссылается на другой список, хотя он и такой же.
print(y is z)  # False Переменная y не ссылается на z, хотя он и такой же.
print(y is x)  # True Переменная y ссылается на x.

x.append(4)
print(x)  # [1, 2, 3, 4]
print(y)  # [1, 2, 3, 4]
