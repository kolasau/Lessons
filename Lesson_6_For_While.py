# Цикл while:
i = 0
while i < 10:
    print(i)
    i += 1

# Цикл for:
# continue - пропускает итерацию
# break - останавливает цикл
for x in "Hello World":
    if x == "a":
        break
    print(x * 3, end='')
else:
    print("\nNo a in x")




