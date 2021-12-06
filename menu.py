from driverI2C import *
from button import *
from grove_rotary_angle_sensor import *
import time

    
def demarrer():
    return 1


def pause():
    return 1



option = {"Démarrer" : demarrer, "Pause" : pause}
keyOption = list(option.keys())
valueOption = list(option.values())
indexChoix = 0


def changerIndexChoix(inc):
    global indexChoix
    if (indexChoix + inc == len(option)):
        indexChoix = 0
        return True
    elif (indexChoix + inc == -1):
        indexChoix = len(option) -1
        return True
    else :
        indexChoix = indexChoix + inc
        return True


def choixMenu():
    setText(keyOption[indexChoix])
    while True:
        value = readButton(3)
        time.sleep(.5)
        print(value)
        if (value == 1):
            print("bouton ok")
            changerIndexChoix(1) 
            print(keyOption[indexChoix])
            setText(keyOption[indexChoix])
            valueOption[indexChoix]()
            break

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