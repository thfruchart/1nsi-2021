# Créé par thfruchart, le 08/10/2021 en Python 3.7
from turtle import *

def rectangle(long, larg) :
    forward(long)
    left(90)
    forward(larg)
    left(90)
    forward(long)
    left(90)
    forward(larg)
    left(90)

speed(0)

def rosace(n):
    for i in range(n):
        rectangle(200,100)
        left(360/n)

rosace(36)
