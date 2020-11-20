import math

a= int(input())
b= int(input())

angle= math.atan(a/b)
angle= angle* 180/ math.pi

print(round(angle))