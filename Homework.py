#!/usr?bin?env python3
import math as m
print("Введите длину первой стороны")
a=int(input())
print("Введите длину второй стороны")
b=int(input())
print("Введите величину угла между сторонами (в градусах)")
A=int(input())
c=m.sqrt(pow(a,2)+pow(b,2)+2*a*b*m.cos((A/180)*m.pi))
print("Третья сторона равна: ",c)
