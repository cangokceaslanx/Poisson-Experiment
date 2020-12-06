#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:01:45 2019

@author: user
"""

import matplotlib.pyplot as mt
datax = [300,320,340,360,380,400,420,440,460,480,500]
datay = [0,0,0,993,998,1022,1078,1016,1031,1087,1107]
index = []
mt.plot(datax,datay, color="red")
mt.xlabel("Voltages")
mt.ylabel("Number of decays in 100s")
mt.title("Operating Voltage Determination")
mt.show()