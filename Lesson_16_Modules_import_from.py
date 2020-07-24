"""
import math
import time
import os
import random as r
try:
    import nomodule
except ImportError:
    print("Modul is not exist\n")
print(math.cos(1))
print(time.time())
print(r.random())
"""

""" Создаем module.py и прописываем функции в нем, потом импортим в рабойчий файл и вызываем функции
которые прописали в модульном файле. Вот так работают модули. Огонь!)
"""
import module
print(module.add(3, 5))
"""
если импортировать только одну функцию, то делаем вот так:
"""
from module import hi, add as a
"""
и к функции можно обращаться далее вот так:
"""
hi()
print(a(7, 10))








