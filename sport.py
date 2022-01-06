from driverI2C import *
from time import *
from grove_ultrasonic import *
from grove_rotary_angle_sensor import *
from button import *
from LED import *
from buzzer import *
from database import *

# Définition du pin de la LED et du Buzzer
initLED(2)
initbuzzer(8)

# Fonction pour d'emettre un `bip`
def buzzer():
    onbuzzer(8)
    time.sleep(0.2)
    offbuzzer(8)

# Fonction pour choisir un nombre de répétition pour un type d'exercice donné 
# Exercice a répétition ou exercice de gainage en temps
def chosirNombre(nom):
    nombreRep = 0
    taille = 0
    if (nom == "repetition"):
        taille = 50 # nombre maximum de répétition possible
    else:
        taille = 120 # temps maximum de gainage
    while True:
        repEnCours = (getIndice(taille))
        if (repEnCours != nombreRep):
            nombreRep = repEnCours
            if (nombreRep > 1):
                setText(str(nombreRep) + " " + nom + "s")
            else:
                setText(str(nombreRep) + " " + nom)
        value = readButton(3)
        if (value == 1):
            break # si on appuie sur le bouton alors on a choisi un nombre de répétition/secondes
        time.sleep(.05)
    return nombreRep

# Fonction pour un exercice de type répétition
# Entrée :
#   - nom de l'exercice : str
#   - nombre de repetition : int
#   - distance de validation de la répétition : int
def exerciceSerie(nom,repet,distanceCapteur):
    repetAFaire = repet 
    setText(str(repetAFaire) + " " + nom + "s")
    while True:
        distance = readValueUltraSonic()
        if (distance < distanceCapteur): # On réduit le nombre de répétition restante a chaque fois que l'on descends sous le seuil
            repetAFaire -= 1
            # On affiche le nombre de repition restante avec ou sans "s"
            if (repetAFaire > 1):
                setText(str(repetAFaire) + " " + nom + "s")
            else:
                setText(str(repetAFaire) + " " + nom)
            buzzer()
            time.sleep(0.9)
        if (repetAFaire == 0): # Un double `bip` est emis quand on a fini
            buzzer()
            time.sleep(0.2)
            buzzer()
            break
        time.sleep(0.1)
    return 1

# Fonction pour un exercice de type répétition
# Entrée :
#   - nom de l'exercice : str
#   - nombre de secondes : int
#   - distance de maintient maximum : int
#   - distance de maintient minimum : int
def exerciceGainage(nom,temps,distanceCapteurMax,distanceCapteurMin):
    secondeRestante = temps
    etat = "ok"
    setText(str(secondeRestante) + " secondes de " + nom)
    while True:
        distance = readValueUltraSonic()
        print(distance)
        if (distance <= distanceCapteurMax and distanceCapteurMin <= distance): # si on se situe dans la bonne tranche de distance alors le temps est décompté
            etat = "ok"
            offLED(2)
            secondeRestante -= 1
            if (secondeRestante > 1):
                setText(str(secondeRestante) + " secondes de " + nom)
            else:
                setText(str(secondeRestante) + " seconde de " + nom)
            time.sleep(1)
        elif (distance < distanceCapteurMin): # si on est en dessous la tranche de distance alors on doit monter
            if (etat != "Montez !"):
                etat = "Montez !"
                # On affiche le message et on allume la led pour attirer l'attention
                setText(etat)
                onLED(2)
        elif (distance > distanceCapteurMax): # si on est au dessus la tranche de distance alors on doit descendre
            if (etat != "Descendez !"):
                etat = "Descendez !"
                # On affiche le message et on allume la led pour attirer l'attention
                setText(etat)
                onLED(2)
        if (secondeRestante == 0): # Un double `bip` est emis quand on a fini
            buzzer()
            time.sleep(0.2)
            buzzer()
            break
        
# Fonction de temporisation entre deux séries
def repos(temps):
    tempsRestant = temps
    while tempsRestant > 0:
        # On affiche le nombre de seconde restante avec ou sans "s"
        if (tempsRestant > 1):
            setText("Repos restant " + str(tempsRestant) + " secondes")
        else:
            setText("Repos restant " + str(tempsRestant) + " seconde")
        tempsRestant -= 1
        time.sleep(1)
    return 1

# Fonction pour faire des pompes
def pompes(repet=0):
    time.sleep(0.1)
    if (repet == 0):
        repet = chosirNombre("repetition")
    exerciceSerie("pompe",repet,20) # On fait un exercice de type répétition nommé "pompe", de `repet` répétition et il faut descendre a 20cm pour valider une répétition
    updateStat("pompes", repet) # On met a jour les stats sur les pompes
    return 1

def squats(repet=0):
    time.sleep(0.1)
    if (repet == 0):
        repet = chosirNombre("repetition")
    exerciceSerie("squat",repet,50) # On fait un exercice de type répétition nommé "squat", de `repet` répétition et il faut descendre a 50cm pour valider une répétition
    updateStat("squats", repet) # On met a jour les stats sur les squats
    return 1

def dips(repet=0):
    time.sleep(0.1)
    if (repet == 0):
        repet = chosirNombre("repetition")
    exerciceSerie("dip",repet,10) # On fait un exercice de type répétition nommé "dip", de `repet` répétition et il faut descendre a 10cm pour valider une répétition
    updateStat("dips", repet) # On met a jour les stats sur les dips
    return 1

def gainage(temps=0):
    time.sleep(0.1)
    if (temps == 0):
        temps = chosirNombre("seconde")
    exerciceGainage("gainage",temps,20,5) # On fait un exercice de type gainage nommé "gainage", de `temps` secondes et il entre 5 et 20cm pour valider une seconde
    updateStat("gainage", temps) # On met a jour les stats sur le gainage
    return 1

def chaise(temps=0):
    time.sleep(0.1)
    if (temps == 0):
        temps = chosirNombre("seconde")
    exerciceGainage("chaise",temps,70,50) # On fait un exercice de type gainage nommé "chaise", de `temps` secondes et il entre 50 et 70cm pour valider une seconde
    updateStat("chaise", temps) # On met a jour les stats sur la chaise
    return 1