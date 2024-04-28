def longest_common_prefix(strings):
    if not strings:
        return ""

    # Начинаем с предположения, что наибольший общий префикс - это первая строка полностью
    prefix = strings[0]

    for s in strings[1:]:
        # Пока текущий префикс не является префиксом текущей строки, укорачиваем его
        while s.find(prefix) != 0:
            prefix = prefix[0:len(prefix) - 1]
            # Если префикс укоротился до пустой строки, общего префикса нет
            if not prefix:
                return ""

    return prefix


# Пример использования
my_strings = ["ваhп", "ваhт", "ваhл"]
print(longest_common_prefix(my_strings))  # Выведет: "ваh"
