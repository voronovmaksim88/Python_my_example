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


class Person:
    def say_hello(self):
        print("Hello")

    def say(self, message):
        print(message)


tom = Person()  # определение объекта tom
bob = Person()  # определение объекта bob
# Person() - вызов конструктора, который возвращает объект класса Person

tom.say_hello()
bob.say("my name bob")
