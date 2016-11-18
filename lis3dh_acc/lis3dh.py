#! /usr/bin/env python
import time
import sys
import smbus
import constants

from smbus import SMBus

#Will only work for the raspberry Pi 2, for other version might need to be
#changed
LIS3DH = SMBus(1)

def twosComp(x):
    if(0x8000 & x):
        x=-(0x010000 - x)
    return x
    
def setDataRate(dataRate):
    temp = LIS3DH.read_byte_data(LIS3DH_I2C_ADDR,CTRL_REG1)
    temp &= 0b1111
    temp |= (dataRate << 4)
    LIS3DH.write_byte_data(LIS3DH_I2C_ADDR,CTRL_REG1)
    
def setup():
    #Check the WHO_AM_I address
    whoami = LIS3DH.read_byte_data(LIS3DH_I2C_ADDR,WHO_AM_I)
    if whoami != 0x33:
        print "LIS3DH with I2C address 0x18 not connected"
        sys.exit()
    
    #Set the data rate to 100HZ 
    setDataRate(RATE_100HZ)
    
    #Its connected so let us enable the XYZ axis
    LIS3DH.write_byte_data(LIS3DH_I2C_ADDR,CTRL_REG1,0x57)
    
def getValueX():
    low_byte  = LIS3DH.read_byte_data(LIS3DH_I2C_ADDR,OUT_X_L)
    high_byte = LIS3DH.read_byte_data(LIS3DH_I2C_ADDR,OUT_X_H)
    result    = (high<<8) | low
    result    = twosComp(result)
    result    = float(result)/16380
    return result
    
def getValueY():
    low_byte  = LIS3DH.read_byte_data(LIS3DH_I2C_ADDR,OUT_Y_L)
    high_byte = LIS3DH.read_byte_data(LIS3DH_I2C_ADDR,OUT_Y_H)
    result    = (high<<8) | low
    result    = twosComp(result)
    result    = float(result)/16380
    return result

def getValueZ():
    low_byte  = LIS3DH.read_byte_data(LIS3DH_I2C_ADDR,OUT_Z_L)
    high_byte = LIS3DH.read_byte_data(LIS3DH_I2C_ADDR,OUT_Z_H)
    result    = (high<<8) | low
    result    = twosComp(result)
    result    = float(result)/16380
    return result

def main():
    setup()
    while(True):
        print getValueX()
        print getValueY()
        print getValueZ()
        time.sleep(1)
        
if __name__=="__main__":
    main()