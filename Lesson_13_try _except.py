

# таким образом мы пропускаем исключение
# try:
#   print(10 / 0)
# except ZeroDivisionError:
#  pass
#   print("End")

# x = int(input())
# y = int(input())
# try:
#    res = x / y
# except ZeroDivisionError:
#    print("You can't divide by zero")
#    res = 0
# print(res)

try:
    x = int(input("Enter number: "))
except ValueError:
    print("Oops...")
    x = "This is not a number"
else:
    print("Done! :D ")
# finally: 100% всегда выполняется, не важно, есть ошибка или нет!
print("Result is: " + str(x) + "\nPress Shift + F10 to try again (only PyCharm)")








