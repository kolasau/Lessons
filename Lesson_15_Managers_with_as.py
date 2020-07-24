
with open("test.txt", "wt", encoding="Latin-1") as inFile:
    num = int(input("Please, enter any number: "))
    line = str("1 / " + str(num) + " = " + str(1 / num))
    print(line)
    inFile.write(line)

