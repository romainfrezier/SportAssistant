from driverI2C import *
from button import *
from grove_rotary_angle_sensor import *
from grove_ultrasonic import *
from sport import *
from programme import *
from LED import *
import time



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
        print("indiceEnCours =  " + str(indiceEnCours))
        if (indiceEnCours != indexChoix):
            indexChoix = indiceEnCours       
            setText(keys[indexChoix])
        value = readButton(3)
        time.sleep(.05)
        #print(value)
        if (value == 1):
            print("bouton ok")
            print(keys[indexChoix])
            setText(keys[indexChoix])
            values[indexChoix]()
            break
'''
                while True:
        degrees = getDegrees()
        if ( 0.1 <= degrees % 20 <= 2):
            changerIndexChoix(1,menu)
            setText(keys[indexChoix])
        value = readButton(3)
        time.sleep(.05)
        print(value)
        if (value == 1):
            print("bouton ok")
            print(keys[indexChoix])
            setText(keys[indexChoix])
            values[indexChoix]()
            break
            '''




option = {"Demarrer" : demarrer, "Pause" : pause}
keyOption = list(option.keys())
valueOption = list(option.values())
option2 = {"Programmes" : programme, "Serie" : serie}
keyOption2 = list(option2.keys())
valueOption2 = list(option2.values())
optionSport = {"Pompes" : pompes, "Squat" : squats, "Dips" : dips, "Gainage" : gaignage, "Chaise" : chaise}
keyOptionSport = list(optionSport.keys())
valueOptionSport = list(optionSport.values())
programme = {"Debutant" : debutant, "Intermediaire" : intermediaire, "Avance" : avance}
keyProgramme = list(programme.keys())
valueProgramme = list(programme.values())
indexChoix = 0

'''
def changerIndexChoix(inc,menu):
    global indexChoix
    if (indexChoix >= len(menu)):
        indexChoix = 0
    if (indexChoix + inc == len(menu)):
        indexChoix = 0
        return True
    elif (indexChoix + inc == -1):
        indexChoix = len(menu) -1
        return True
    else :
        indexChoix = indexChoix + inc
        return True
        '''


def choixMenu():
    setText(keyOption[indexChoix])
    time.sleep(3)
    potentiometre(option,keyOption,valueOption)
    '''
    while True:
        degrees = getDegrees()
        if ( 0.1 <= degrees % 20 <= 2):
            changerIndexChoix(1,option)
            setText(keyOption[indexChoix])
        value = readButton(3)
        time.sleep(.05)
        print(value)
        if (value == 1):
            print("bouton ok")
            print(keyOption[indexChoix])
            setText(keyOption[indexChoix])
            valueOption[indexChoix]()
            break
            '''

'''
def choixMenu():
    setText(keyOption[indexChoix])
    value = read5way()
    while read5way() != 4:
        if (value != read5way()):
            value = read5way()
            print(value)
            if (value == 1):
                changerIndexChoix(1) 
            elif (value == 3):   
                changerIndexChoix(-1)  
            print(keyOption[indexChoix])
            setText(keyOption[indexChoix])
        time.sleep(.5)
    valueOption[indexChoix]()    
    '''