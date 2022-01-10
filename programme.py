from time import *
from menu import *
from sport import *

# Dictionnaire des exercices disponibles
map_exercices = {
    "pompes" : pompes,
    "dips" : dips,
    "gainage" : gainage,
    "chaise" : chaise,
    "squats" : squats,
    "repos" : repos
}

# Fonction du programme personalisé
def personnalise(programme):
    print(programme)
    for exercice in programme: # pour chaque exercice du programme personalisé...
        for i in range(int(exercice["nbSerie"])): # ...on fait un certain nombre de série...
            values = list(exercice.values())
            map_exercices[exercice["nom"]](values[2]) # ...de cet exercice
    time.sleep(0.5)
    setText("Bravo")
    time.sleep(2)
    return 1

# Fonction du programme pour sportif débutant, de base dans la rasp
def debutant():
    for i in range(0,3):
        pompes(5)
        repos(30)
    for i in range(0,3):
        dips(5)
        repos(30)
    for i in range(0,3):
        gainage(30)
        repos(30)
    for i in range(0,3):
        squats(10)
        repos(30)
    for i in range(0,3):
        chaise(20)
        repos(30)
    time.sleep(0.5)
    setText("Bravo")
    time.sleep(2)
    return 1

# Fonction du programme pour sportif de niveau intermédiaire, de base dans la rasp
def intermediaire():
    for i in range(0,3):
        pompes(10)
        repos(45)
    for i in range(0,3):
        dips(10)
        repos(45)
    for i in range(0,3):
        gainage(45)
        repos(45)
    for i in range(0,3):
        squats(20)
        repos(45)
    for i in range(0,3):
        chaise(35)
        repos(45)
    time.sleep(0.5)
    setText("Bravo")
    time.sleep(2)
    return 1

# Fonction du programme pour sportif de niveau avancé, de base dans la rasp
def avance():
    for i in range(0,3):
        pompes(15)
        repos(45)
    for i in range(0,3):
        dips(15)
        repos(45)
    for i in range(0,3):
        gainage(60)
        repos(45)
    for i in range(0,3):
        squats(30)
        repos(45)
    for i in range(0,3):
        chaise(45)
        repos(45)
    time.sleep(0.5)
    setText("Bravo")
    time.sleep(2)
    return 1