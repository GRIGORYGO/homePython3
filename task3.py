# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('Введите длинну масива N: '))
x = int(input('Введите число Х: '))

from random import randint
arr = []
num = 100
closusedNum = num
result = 0

for i in range(n):
    arr.append(randint(0, num - 1))
    if abs(x - arr[i]) < closusedNum:
        closusedNum = abs(x - arr[i])
        arr[i] = result

print(arr)
print(f"'Число :' {result}")