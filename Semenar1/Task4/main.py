"""Напишите программу, которая принимает на вход координаты двух точек и находит
 расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21"""
import math

print("Введите координаты первой точки: ")
vec1 = input().split()
print("Введите координаты второй точки: ")
vec2 = input().split()

def distance(vec1, vec2):
    distance = round(math.sqrt((int(vec2[0]) - int(vec1[0])) ** 2 + (int(vec2[1]) - int(vec1[1])) ** 2), 2)
    return distance

print(f"A({vec1[0]}, {vec1[1]}); B({vec2[0]}, {vec2[1]}) -> {distance(vec1, vec2)}")

