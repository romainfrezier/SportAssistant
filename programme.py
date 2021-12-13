from time import *
from menu import *
from sport import *


def debutant():
    for i in range(0,3):
        pompes(5)
        repos(30)
    for i in range(0,3):
        dips(5)
        repos(30)
    for i in range(0,3):
        gaignage(30)
        repos(30)
    for i in range(0,3):
        squats(10)
        repos(30)
    for i in range(0,3):
        chaise(20)
        repos(30)
    return 1

def intermediaire():
    for i in range(0,3):
        pompes(10)
        repos(45)
    for i in range(0,3):
        dips(10)
        repos(45)
    for i in range(0,3):
        gaignage(45)
        repos(45)
    for i in range(0,3):
        squats(20)
        repos(45)
    for i in range(0,3):
        chaise(35)
        repos(45)
    return 1

def avance():
    for i in range(0,3):
        pompes(15)
        repos(45)
    for i in range(0,3):
        dips(15)
        repos(45)
    for i in range(0,3):
        gaignage(60)
        repos(45)
    for i in range(0,3):
        squats(30)
        repos(45)
    for i in range(0,3):
        chaise(45)
        repos(45)
    return 1