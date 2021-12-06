import smbus
import time

bus = smbus.SMBus(1)
adresse= 0x50

def lirePouls():
    return bus.read_byte_data(adresse, 0x00)



