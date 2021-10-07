from turtle import *

n = int(input('Entrer n :'))

rayon = 200//n
dist = 3 * rayon
up()
backward(dist * n//2)

for i in range(n):
    if i%2 ==0 :
        dot(rayon,'red')
    else :
        dot(rayon,'green')
    forward(dist)

    


