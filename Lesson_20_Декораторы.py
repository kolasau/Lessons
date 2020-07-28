
def decorator(func):
    def wrapper():
        print("Код до выполнения функции")
        func()
        print("Код после выполнения функции")
    return wrapper

@decorator   # - вот так используем декоратор перед функцией, котрую хотим задокументировать
def show():
    print("I am a simple function")
# show = decorator(show)
show()









