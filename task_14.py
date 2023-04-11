#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

IntNamber= int (input("Введите число: "))
i=0
namber=0
for i in range(IntNamber):
    namber= 2**i
    if namber<=IntNamber:
        print(f"{namber} ")
    else:
        quit()