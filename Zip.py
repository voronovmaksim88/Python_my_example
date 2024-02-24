
people_keys = ["name", "age", "gender"]
people_values = ["Max", 35, "men"]

people_dict = dict(zip(people_keys, people_values))
print(people_dict)

people_list = list(zip(people_keys, people_values))
print(people_list)  # создаётся список элементы которого кортежи
