#! /usr/bin/env python
import time
import sys
import smbus
import constants

from smbus import SMBus

#Will only work for the raspberry Pi 2, for other version might need to be
#changed
LIS3DH = SMBus(1)

def setup():
    #Check the WHO_AM_I address
    whoami = LIS3DH.read_byte_data(LIS3DH_I2C_ADDR,WHO_AM_I)
    if whoami != 0x33:
        print "LIS3DH with I2C address 0x18 not connected"
        sys.exit()
    #Its connected so let us enable the XYZ axis
    LIS3DH.write_byte_data(LIS3DH_I2C_ADDR,CTRL_REG1,0x77)
    
    #Set the data rate to 100HZ 
    
def disconnect():
    