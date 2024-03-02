# В квадратной матрице элементы на главной диагонали увеличить в 2 раза
import random

size = 4
matrix = [[random.randint(0, 10) for _ in range(size)] for _ in range(size)]

print("Исходная матрица:")
for i in matrix:
    print(i)

for i in range(size):
    matrix[i][i] *= 2

print("Измененная матрица:")
for _ in matrix:
    print(_)

