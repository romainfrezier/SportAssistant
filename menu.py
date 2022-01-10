from driverI2C import *
from button import *
from grove_rotary_angle_sensor import *
from grove_ultrasonic import *
from sport import *
from programme import *
from LED import *
from database import *
import time

# Fonction pour naviguer dans le menu principal
def choixMenu():
    time.sleep(0.1)
    print("Menu Général")
    potentiometre(optionGeneral,keyOptionGeneral,valueOptionGeneral)
    return 1

# Fonction pour récupérer les programmes personnalisés sur la base de données
def getProgrammePerso(nom):
    programmeChoisi = {}
    for programme in programmes.values():
        if programme["Nom"] == nom:
            programmeChoisi = programme["Exercices"]
            break
    return programmeChoisi

# Fonction pour lancer un programme personalisé
def programmePerso(nom):
    programme = getProgrammePerso(nom)
    personnalise(programme)
    choixMenu()

# Charge les programmes personalisés dans la rasp
def updateProgrammesPersos():
    global programmes
    global optionProgrammesPersos
    global keyOptionProgrammesPersos
    global valueOptionProgrammePersos
    programmes = getProgrammes()
    listeProgrammes = {"Menu General" : choixMenu}
    print(programmes, "\n")
    for programme in programmes.values():
        print('le programme en cours', list(programme))
        values = list(programme.values())
        listeProgrammes[values[1]] = programmePerso
    optionProgrammesPersos = listeProgrammes # Copie du dictionnnaire des programmes personalisés
    keyOptionProgrammesPersos = list(optionProgrammesPersos.keys()) # Liste des clés du dictionnaire de programmes personalisés
    valueOptionProgrammePersos = list(optionProgrammesPersos.values()) # Liste des valeurs du dictionnaire de programmes personalisés

# Charge les stats dans la rasp
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
            chaine = str(values[1]) + " " + str(values[0]) # 1 -> nombre de répétitions ; 0 -> nom
        else:
            chaine = str(values[1]) + " secondes de " + str(values[0]) # 1 -> nombre de secondes ; 0 -> nom
        listeStats[chaine] = choixMenu # Retour a menu principal
    optionStats = listeStats # Copie du dictionnnaire des statistiques
    keyOptionStats = list(optionStats.keys()) # Liste des clés du dictionnaire de statistiques
    valueOptionStats = list(optionStats.values()) # Liste des valeurs du dictionnaire de statistiques

updateProgrammesPersos()

# Fonction pour naviguer dans le menu des programmes personalisés
def programmesPersomenu():
    updateProgrammesPersos()
    time.sleep(0.1)
    potentiometre(optionProgrammesPersos,keyOptionProgrammesPersos,valueOptionProgrammePersos)
    return 1

# Fonction pour naviguer dans le menu des statistiques
def statsMenu():
    updateStats()
    time.sleep(0.1)
    potentiometre(optionStats,keyOptionStats,valueOptionStats)
    return 1

# Fonction pour naviguer dans le menu des séries
def serie():
    time.sleep(0.1)
    potentiometre(optionSport,keyOptionSport,valueOptionSport)
    choixMenu()
    return 1

# Fonction pour naviguer dans le menu des programmes
def programme():
    time.sleep(0.1)
    potentiometre(programme,keyProgramme,valueProgramme)
    choixMenu()
    return 1

# Fonction pour utiliser le potentiomètre dans la navigation des menus
def potentiometre(menu,keys,values):
    global indexChoix
    indexChoix = 0
    setText(keys[0])
    indiceEnCours = 0
    while True:
        indiceEnCours = getIndice(len(menu)) 
        if (indiceEnCours != indexChoix):
            indexChoix = indiceEnCours       
            setText(keys[indexChoix])
        value = readButton(3)
        time.sleep(.05)
        if (value == 1): # si le bouton a été utilisé, c'est qu'on a choisi une option
            if (values[indexChoix] == programmePerso):
                setText(keys[indexChoix])
                values[indexChoix](keys[indexChoix])
            else:
                setText(keys[indexChoix])
                values[indexChoix]()
            break

programmes = getProgrammes()
stats = getStats()

# Partie menu général
optionGeneral = {"Programmes" : programme, "Programmes perso" : programmesPersomenu, "Serie" : serie , "Statistiques" : statsMenu}
keyOptionGeneral = list(optionGeneral.keys())
valueOptionGeneral = list(optionGeneral.values())

# Partie exercice
optionSport = {"Menu General" : choixMenu, "Pompes" : pompes, "Squat" : squats, "Dips" : dips, "Gainage" : gainage, "Chaise" : chaise}
keyOptionSport = list(optionSport.keys())
valueOptionSport = list(optionSport.values())

# Partie programme
programme = {"Menu General" : choixMenu, "Debutant" : debutant, "Intermediaire" : intermediaire, "Avance" : avance}
keyProgramme = list(programme.keys())
valueProgramme = list(programme.values())

# Partie programme personalisé
optionProgrammesPersos = {}
keyOptionProgrammesPersos = list(optionProgrammesPersos.keys())
valueOptionProgrammePersos = list(optionProgrammesPersos.values())

# Partie stats
optionStats = {}
keyOptionStats = list(optionStats.keys())
valueOptionStats = list(optionStats.values())

# Le premier élément est afficher a l'arriver sur un menu
indexChoix = 0
