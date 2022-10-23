# home_work_1
# task_8

# Напишите программу, которая принимает на
# вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.

# print('Введите координаты точки А:') 
# x_A = float(input('X: ')) 
# y_A = float(input('Y: ')) 
# print("Введите координаты точки B:") 
# x_B = float(input('X: ')) 
# y_B = float(input('Y: ')) 
  
# from math import sqrt 
# print('Расстояние между A и B: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2))  

from functools import reduce
dot_1 = list(map(int, input('Введите координаты X и Y для точки A, через пробел: ').split())) 
dot_2 = list(map(int, input('Введите координаты X и Y для точки B, через пробел: ').split()))
def dot_range(dot_1, dot_2):
     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
     return round(rng, 2)
print(f'Расстояние между А и В: {dot_range(dot_1, dot_2)}.')