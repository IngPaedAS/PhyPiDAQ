#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''read data from digital sensor:
     this script illustrates the general usage of package phypidaq
     prints data read from a digital sensor  
     INA219 Current & Voltage sensor
    
'''
import time, numpy as np

# import module controlling readout device
#from phypidaq.AS7265xConfig import *
import AS7265xConfig

print('AS7265 Test')


# create an instance of the device
cdict={'Gain': 3}
device = AS7265xConfig.AS7265xConfig(cdict)

# initialize the device
device.init()

# reserve space for data (two channels here)
dat = np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]) 

print(' starting readout,     type <ctrl-C> to stop')

# read-out interval in s
dt = 1.
# start time
T0 = time.time()

# readout loop, stop with <crtl>-C
while True:
  device.acquireData(dat)
  dT = time.time() - T0
  print('%.2g: %.2g, %.2g, %.2g, %.2g, %.2g, %.2g, %.2g, %.2g, %.2g, %.2g, %.2g, %.2g, %.2g, %.2g, %.2g, %.2g, %.2g, %.2g' %(dT, dat[0], dat[1], dat[2], dat[3], dat[4], dat[5], dat[6], dat[7], dat[8], dat[9], dat[10], dat[11], dat[12], dat[13], dat[14], dat[15], dat[16], dat[17]) )
  time.sleep(dt)

