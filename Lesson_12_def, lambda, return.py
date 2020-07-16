
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

