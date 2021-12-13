from driverI2C import *
from time import *
from grove_ultrasonic import *
from grove_rotary_angle_sensor import *
from button import *
from LED import *
from buzzer import *


initLED(2)
initbuzzer(8)


def chosirNombre(nom):
    nombreRep = 0
    degreesActuel = 0
    taille = 0
    if (nom == "repetition"):
        taille = 50
    else:
        taille = 120
    while True:
        degrees = getDegrees()
        repEnCours = (getIndice(taille))
        if (repEnCours != nombreRep):
            nombreRep = repEnCours
            if (nombreRep > 1):
                setText(str(nombreRep) + " " + nom + "s")
            else:
                setText(str(nombreRep) + " " + nom)
        value = readButton(3)
        if (value == 1):
            print("bouton ok")
            print("nombre de repet = " + str(nombreRep))
            break
        time.sleep(.05)
    return nombreRep

def exerciceSerie(nom,repet,distanceCapteur):
    repetAFaire = repet 
    setText(str(repetAFaire) + " " + nom + "s")
    while True:
        distance = readValueUltraSonic()
        if (distance < distanceCapteur):
            repetAFaire -= 1
            if (repetAFaire > 1):
                setText(str(repetAFaire) + " " + nom + "s")
            else:
                setText(str(repetAFaire) + " " + nom)
            onbuzzer(8)
            time.sleep(0.2)
            offbuzzer(8)
            time.sleep(0.9)
        if (repetAFaire == 0):
            onbuzzer(8)
            time.sleep(0.2)
            offbuzzer(8)
            time.sleep(0.2)
            onbuzzer(8)
            time.sleep(0.2)
            offbuzzer(8)
            break
        time.sleep(0.1)
    return 1

def exerciceGainage(nom,temps,distanceCapteurMax,distanceCapteurMin):
    secondeRestante = temps
    etat = "ok"
    setText(str(secondeRestante) + " secondes")
    while True:
        distance = readValueUltraSonic()
        print(distance)
        if (distance < distanceCapteurMax and distanceCapteurMin < distance):
            etat = "ok"
            offLED(2)
            secondeRestante -= 1
            if (secondeRestante > 1):
                setText(str(secondeRestante) + " secondes")
            else:
                setText(str(secondeRestante) + " seconde")
            time.sleep(1)
        elif (distance < distanceCapteurMin):
            if (etat != "Montez !"):
                etat = "Montez !"
                setText(etat)
                onLED(2)
        else:
            if (etat != "Descendez !"):
                etat = "Descendez !"
                setText(etat)
                onLED(2)
        if (secondeRestante == 0):
            onbuzzer(8)
            time.sleep(0.2)
            offbuzzer(8)
            time.sleep(0.2)
            onbuzzer(8)
            time.sleep(0.2)
            offbuzzer(8)
            break
        

def repos(temps):
    tempsRestant = temps
    while tempsRestant > 0:
        if (tempsRestant > 1):
            setText("Repos restant " + str(tempsRestant) + " secondes")
        else:
            setText("Repos restant " + str(tempsRestant) + " seconde")
        tempsRestant -= 1
        time.sleep(1)
    return 1


def pompes(repet=0):
    if (repet == 0):
        repet = chosirNombre("repetition")
    exerciceSerie("pompe",repet,20)
    return 1

def squats(repet=0):
    if (repet == 0):
        repet = chosirNombre("repetition")
    exerciceSerie("squat",repet,50)
    return 1

def dips(repet=0):
    if (repet == 0):
        repet = chosirNombre("repetition")
    exerciceSerie("dip",repet,10)
    return 1

def gaignage(temps=0):
    if (temps == 0):
        temps = chosirNombre("seconde")
    exerciceGainage("gainage",temps,20,5)
    return 1

def chaise(temps=0):
    if (temps == 0):
        temps = chosirNombre("seconde")
    exerciceGainage("chaise",temps,70,50)
    return 1