#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math

print('Введите координаты точки A: ')
a_x = float(input('X: '))
a_y = float(input('Y: '))
print('Введите координаты точки B: ')
b_x = float(input('X: '))
b_y = float(input('Y: '))

distance = math.sqrt((a_x - b_x)**2 + (a_y - b_y)**2)

print(f'Расстояние между двумя точками равно {round(distance, 2)}')