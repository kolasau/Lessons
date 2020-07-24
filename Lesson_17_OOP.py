
# это класс. сюда впихиваем параметры или функции

class Person:
    name = "Ivan"
    age = 10

    def set(self, name, age):  # def - функция  set - метод
        self.name = name
        self.age = age

# а это объект
maks = Person()
maks.set("Maksim", 31)
print(maks.name + "\n" + str(maks.age) + "\n")

vlad = Person()
vlad.name ="Vlad"
vlad.age = 45
print(vlad.name)
print(str(vlad.age) + "\n")

ivan = Person()
print(ivan.name)
