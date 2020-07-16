
d = {
    'name1': 'Maksim',
    'name2': 'Ivan',
    'name3': 'Petya',
    'name4': 'Vasya'
}

print(d['name3'])
print(d)

dict1 = dict(short="dict", longer="dictionary")
dict1['short'] = 234
print(dict1)

sposob2 = dict([(23, 43), (43, 56)])
print(sposob2)

sposob3 = dict.fromkeys(['a', 'b', 'c'], 'znachenie dlya vseh')
print(sposob3)

d2 = {f: f ** 2 for f in range(7)}
print(d2)

# ----------КЛЮЧ------ЗНАЧЕНИЕ------------
person = {
    'name': {
        'last_name': 'Kolasau',
        'first_name': 'Ivan',
        'middle_name': 'Petrovich'
    },
    'address': ['Downtown', 'House 45', 'fr-800'],
    'phone': {
        'home_phone': '+7895485455',
        'mobile_phone': '+84681351551',
        'work_phone': '+3333333333333'
    }
}
# ------------где!?----что?!!------------
print(person['name']['first_name'])
person['address'][1] = 'House 1234'   # таким образом можно присваивать новые данные
# ------------где!?----что?!!------------
print(person['address'][1])
# ------------где!?----что?!!------------
print(person['phone']['work_phone'])

