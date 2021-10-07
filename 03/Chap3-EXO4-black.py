from turtle import *

n = int(input('Entrer n :'))

dist = 50
rayon = 15

up()
backward(dist * n//2)

for i in range(n):
    dot(rayon)
    forward(dist)

    


