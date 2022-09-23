# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

someList = [int(i) for i in input().split()]
secondList = [(someList[i] * someList[len(someList) - 1 - i]) for i, value in enumerate(someList)]
print(secondList)