my_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
for key, value in my_dict.items():
    print(key, value)

favorite_songs = {
    'Тополиный пух': 'Иванушки international',
    'Город золотой': 'Аквариум',
    'Звезда по имени Солнце': 'Кино',
    'Space Oddity': 'David Bowie',
    'Рыба': 'Аквариум',
    'Серенада Трубадура': 'Муслим Магомаев',
}
# Извлечём и напечатаем только значения (values) каждого элемента
for singer in favorite_songs.values():
    print('Доктор, я больше не могу слушать исполнителя ' + singer)

# А в этом цикле извлечём и напечатаем только ключи (keys) словаря
for music in favorite_songs.keys():
    print('Доктор, я каждый день по три раза слушаю песню ' + music)
