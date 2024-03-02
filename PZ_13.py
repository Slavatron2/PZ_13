#В матрице найти минимальный элемент в последней строке

import random

matrix = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
print(" Исходная Матрица:")
for i in matrix:
    print(i)

stroka = matrix[-2]
min_element = min(stroka)

print("Минимальный элемент в предпоследней строке матрицы:", min_element)

