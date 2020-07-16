
def func(x):
    def add(a):
        return x + a
    return add

test = func(100)
print(test(200))

# _________________________________________________________________

def funk():
    pass
print(funk())

# ____________________________________________________________

def func2(r, w, y = 2):
    res2 = r + w
    res2 *= y
    return res2

print(func2(2, 4))


# ______________________________________________________________

def func3(*args):
    return args

print(func3(2, 4, 5))  # передается как кортеж

# _______________________________________________________________

def func4(**argss):
    return argss

print(func4(a='dict', b='123', c=5))  # передается как словарь

# _______________________________________________________________

def func5(**args1):
    return args1
print(func5(short='dicts', longer='qwerty'))  # передается как словарь

# ____________________________________________________________________

# lambda functions - анонимные функции, которые записываются в одну строчку и выполняют одну операцию
# задаем параметры: выполняем
add = lambda x, y: x + y
print(add(8, 8))
print(add("Li", "nux"))

print((lambda x, y: x * y)(2, 6))  #  тоже самое как и выше, только в одну строчку

fun = lambda *argsssss: argsssss
print(fun(2, 56, 78.76))



