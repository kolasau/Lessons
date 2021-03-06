
a = set("hello")  # выводим в рандомном порядке и элементы не будут повторяться
print(type(a))

print(a)


b = {i ** 2 for i in range(10)}
# b = {23, 'qwrqw'}
print(type(b))
print(b)

c = set("Hello")
d = frozenset("Qwerty")  # нельзя ничего добавить

c.add('addddddddddd')
print(c)


spisok = ['a', 'r', 'f', 'i', 'e', 'd', 's', 'a', 'w']
print(spisok)
print(set(spisok))   # убирает повторяющиеся элементы


g = {32, 45, 43.23, 76}
x = 45
print(x in g)
print(len(g))  # выводим количество элементов из множества

# ___________________________________________________________________________________________________
h = {67, 12, 90}
y = {48, 123, 21}
print(h.isdisjoint(y))  # возвращает True, если множества не имеют схожих элементов
print(h == y)  # сравниваем множества

#  h.update(y) - функция для объединения множеств
#  h.intersection_update(y) - выводит схожие элементы множеств
#  h.difference_update(y) - покажет все те элементы, которые есть в h,но нет в y
"""  h.symmetric_difference_update(y) - находим все элементы, которые есть в одном, 
                                        но нет в обоих множествах, другими словами, 
                                        находим все не похожие элементы.
"""
#  h.remove(12) - удаляем элемент из множества, если не найдет элемент, то выдаст ошибку
#  h.discard() - удаляем элемент из множества, если не найдет элемент, то НЕ выдаст ошибку
#  h.pop() - удаляем первый элемент
#  h.clear() - полностью очищаем множество
