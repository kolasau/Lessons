# Наследование
"""class Person:
    name = "Ivan"
    age = 10

    def set(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    course = 1


igor = Student()
igor.set("Igor", 19)
print(igor.course)

vlad = Person()
vlad.set("Влад", 25)
print(vlad.name + " " + str(vlad.age))

ivan = Person()
ivan.set("Иван", 56)
print(ivan.age) """

# инкапсуляция
"""
ставим _ перед name (_set) и функция не будет использоваться в других классах 
(это как рекомендация для других разрабов)
ставим __ перед name (__set) то это уже строгое ограничение, выдаст ошибку, 
если использовать в др классах \ методах и тд.
"""
class Person:
    name = "Ivan"
    age = 10

    def set(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    course = 1


igor = Student()
igor.set("Igor", 19)
print(igor.course)

vlad = Person()
vlad.set("Влад", 25)
print(vlad.name + " " + str(vlad.age))

ivan = Person()
ivan.set("Иван", 56)
print(ivan.age)






