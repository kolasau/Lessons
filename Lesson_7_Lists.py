
list1 = []
list2 = [1, 56, "s", 34, 2.34, ["s", 2, 3, 4, 5, 6, "Hello"]]
print(list2)

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)

list1.append(23)
list1.append(34)
list1.insert(0, 34)
b = [24, 67]
list1.extend(b)   # добавляем список b в конец списка list1
#          index, what to put in
list1.insert(2, 1988)     # вставляем в список, указывая место вставки и затем что
list1.remove(34)     # удаляет только первый такой элемент 34
list1.pop(0)         # удаляет Итый элемент или удаляет элемент по индексу или если ничего не писать, удалит последний
print(list1.index(24))  # выводим индекс элемента из списка
print(list1.count(34))   # выводит количество заданных элементов из списка, указали 34, в списке 1 такой элемент

list1.sort()   # сортирует список в порядке возрастания
print(list1)

list1.reverse()  # переворачивает список
print(list1)

list1.clear()   # очищает список

print("-----------END-------------")





