'''
This file holds all the constants that are required for programming the LIS3DH
including register addresses and their values
'''

'''
The LIS3DH I2C address
'''
LIS3DH_I2C_ADDR     =       0x18

'''
The LIS3DH Register Map
'''
#0x00 - 0x06 - reserved
STATUS_REG_AUX      =       0x07
OUT_ADC1_L          =       0x08
OUT_ADC1_H          =       0x09
OUT_ADC2_L          =       0x0A
OUT_ADC2_H          =       0x0B
OUT_ADC3_L          =       0x0C
OUT_ADC3_H          =       0x0D
INT_COUNTER_REG     =       0x0E
WHO_AM_I            =       0x0F
# 0x10 0x1E - reserved
TEMP_CFG_REG        =       0x1F
CTRL_REG1           =       0x20
CTRL_REG2           =       0x21
CTRL_REG3           =       0x22
CTRL_REG4           =       0x23
CTRL_REG5           =       0x24
CTRL_REG6           =       0x25
REFERENCE           =       0x26
STATUS_REG2         =       0x27
OUT_X_L             =       0x28
OUT_X_H             =       0x29
OUT_Y_L             =       0x2A
OUT_Y_H             =       0x2B
OUT_Z_L             =       0x2C
OUT_Z_H             =       0x2D
FIFO_CTRL_REG       =       0x2E
FIFO_SRC_REG        =       0x2F
INT1_CFG            =       0x30
INT1_SOURCE         =       0x31
INT1_THS            =       0x32
INT1_DURATION       =       0x33
#0x34 - 0x37 - reserved
CLICK_CFG           =       0x38
CLICK_SRC           =       0x39
CLICK_THS           =       0x3A
TIME_LIMIT          =       0x3B
TIME_LATENCY        =       0x3C
TIME_WINDOW         =       0x3D

'''
Values to select range of the accelerometer
'''
RANGE_2G            =       0b00
RANGE_4G            =       0b01
RANGE_8G            =       0b10
RANGE_16G           =       0b11

'''
Values to select data refresh rate of the accelerometer
'''
RATE_400HZ          =       0b0111
RATE_200HZ          =       0b0110
RATE_100HZ          =       0b0101
RATE_50HZ           =       0b0100
RATE_25HZ           =       0b0011
RATE_10HZ           =       0b0010
RATE_1HZ            =       0b0001
RATE_POWERDOWN      =       0
RATE_LOWPOWER_1K6HZ =       0b1000
RATE_LOWPOWER_5KHZ  =       0b1001

'''
The WHO_AM_I reply
'''
WHO_AM_I_ID         =       0x33














