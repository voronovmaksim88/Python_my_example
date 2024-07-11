"""
Класс — шаблон, с помощью которого удобно описывать однотипные объекты.
В классе содержатся свойства, правила создания и поведение объекта.
        Объект — экземпляр, созданный на основе шаблона.
        Атрибут — поле, хранящее значение. Содержит свойства объекта.
        Метод — функция, связанная с классом. Описывает поведение или действия объекта.
Пример класса - автомобили, его атрибутами будут: цвет, марка автомобиля, регистрационный номер.
Методами могут быть: ехать прямо, повернуть, остановиться.
Объектом класса “Автомобили” может быть конкретный автомобиль, например, Renault Logan белого цвета с номером М123РТ.
"""


# минимальный класс
class C:
    pass


print(C)


class PLC:
    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer

    def about(self):
        print("name", self.name)
        print("manufacturer", self.manufacturer)


M245 = PLC(name="M245", manufacturer="Zentec")
M245.about()
