def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return (x//5 + 1)*5


print(closest_mod_5(6))


# def closest_mod_5(x):
#     return (x + 4) // 5 * 5

# рекурсивное решение
# def closest_mod_5(x):
#     return x if x % 5 == 0 else closest_mod_5(x + 1)

