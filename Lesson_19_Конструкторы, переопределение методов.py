class Person:
    name = "ivan"
    age = 10

    def set(self, name, age):
        self.name = name
        self.age = age
# А потом вызвать вот так:
igor24 = Person()
igor24.set("igor", 24)

# Но намного быстрее и понятнее будет вот так:
class Person:
    name = "ivan"
    age = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age
# А потом вызвать вот так:
igor24 = Person("igor", 24)