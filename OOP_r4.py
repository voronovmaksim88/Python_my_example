class Person:
    name = "Ivan"  # это поле класса
    age = 10  # это тоже поле класса

    def __init__(self, name, age):  # это метод класса
        self.age = age
        self.name = name

    def set(self, name, age):  # это метод класса
        self.age = age
        self.name = name

    def about(self):
        print("Name:", self.name, "Age:", self.age)

    #  инкапсуляции в питоне как таковой нет, но можно намекнуть о ней
    def _about_name(self):
        # нижнее подчёркивание намекает  что не надо использовать этот в метод других классах наследниках
        print("Name:", self.name)

    def __about_age(self):
        # двойное нижнее подчёркивание запрещает использование метода в кассах наследниках, но запрет можно обойти
        print("Name:", self.name)


class Student(Person):  # класс Student наследует методы и поля класса Person
    course: int = 1

    def about(self):  # полиморфизм, переопределение метода родительского класса
        print("Name:", self.name, "Age:", self.age, "Course:", self.course)


vlad = Person("Vlad", 15)
print(vlad.name, end=" ")
print(vlad.age)

ivan = Person
ivan.age = 45
print(ivan.name, end=" ")
print(ivan.age)

petr = Person("Petr", 23)
petr.about()

igor = Student("Igor", 18)
igor.about()
