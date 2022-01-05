from driverI2C import *
from button import *
from grove_rotary_angle_sensor import *
from grove_ultrasonic import *
from sport import *
from programme import *
from LED import *
from database import *
import time


programmes = getProgrammes()
stats = getStats()
optionProgrammesPersos = {}
keyOptionProgrammesPersos = list(optionProgrammesPersos.keys())
valueOptionProgrammePersos = list(optionProgrammesPersos.values())
optionStats = {}
keyOptionStats = list(optionStats.keys())
valueOptionStats = list(optionStats.values())

def getProgrammePerso(nom):
    programmeChoisi = {}
    for programme in programmes:
        if programme["Nom"] == nom:
            programmeChoisi = programme["Exercices"]
            break
    return programmeChoisi

def programmePerso(nom):
    programme = getProgrammePerso(nom)
    personnalise(programme)
    demarrer()

def updateProgrammesPersos():
    global programmes
    global optionProgrammesPersos
    global keyOptionProgrammesPersos
    global valueOptionProgrammePersos
    programmes = getProgrammes()
    listeProgrammes = {}
    for programme in programmes:
        values = list(programme.values())
        listeProgrammes[values[1]] = programmePerso
        print(programme)
    optionProgrammesPersos = listeProgrammes
    keyOptionProgrammesPersos = list(optionProgrammesPersos.keys())
    valueOptionProgrammePersos = list(optionProgrammesPersos.values())

def updateStats():
    global stats
    global optionStats
    global keyOptionStats
    global valueOptionStats
    stats = getStats()
    listeStats = {}
    for stat in stats:
        values = list(stat.values())
        chaine = ""
        if (values[2] == 'repet'):
            chaine = str(values[1]) + " " + str(values[0])
        else:
            chaine = str(values[1]) + " secondes de " + str(values[0])
        listeStats[chaine] = demarrer
        print(stats)
    optionStats = listeStats
    keyOptionStats = list(optionStats.keys())
    valueOptionStats = list(optionStats.values())

updateProgrammesPersos()

def programmesPersomenu():
    updateProgrammesPersos()
    time.sleep(0.1)
    potentiometre(optionProgrammesPersos,keyOptionProgrammesPersos,valueOptionProgrammePersos)
    return 1

def statsMenu():
    updateStats()
    time.sleep(0.1)
    potentiometre(optionStats,keyOptionStats,valueOptionStats)
    return 1

def demarrer():
    time.sleep(0.1)
    potentiometre(option2,keyOption2,valueOption2)
    return 1

def serie():
    time.sleep(0.1)
    potentiometre(optionSport,keyOptionSport,valueOptionSport)
    demarrer()
    return 1

def programme():
    time.sleep(0.1)
    potentiometre(programme,keyProgramme,valueProgramme)
    demarrer()
    return 1

def pause():
    return 1


def potentiometre(menu,keys,values):
    global indexChoix
    indexChoix = 0
    setText(keys[0])
    indiceEnCours = 0
    while True:
        indiceEnCours = getIndice(len(menu))
        #print("indiceEnCours =  " + str(indiceEnCours))
        if (indiceEnCours != indexChoix):
            indexChoix = indiceEnCours       
            setText(keys[indexChoix])
        value = readButton(3)
        time.sleep(.05)
        #print(value)
        if (value == 1):
            #print("bouton ok")
            if (values[indexChoix] == programmePerso):
                print(keys[indexChoix])
                setText(keys[indexChoix])
                values[indexChoix](keys[indexChoix])
            else:
                print(keys[indexChoix])
                setText(keys[indexChoix])
                values[indexChoix]()
            break




option2 = {"Programmes" : programme, "Programmes perso" : programmesPersomenu, "Serie" : serie , "Statistiques" : statsMenu}
keyOption2 = list(option2.keys())
valueOption2 = list(option2.values())
optionSport = {"Pompes" : pompes, "Squat" : squats, "Dips" : dips, "Gainage" : gainage, "Chaise" : chaise}
keyOptionSport = list(optionSport.keys())
valueOptionSport = list(optionSport.values())
programme = {"Debutant" : debutant, "Intermediaire" : intermediaire, "Avance" : avance}
keyProgramme = list(programme.keys())
valueProgramme = list(programme.values())
indexChoix = 0



def choixMenu():
    time.sleep(0.5)
    demarrer()