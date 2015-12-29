# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 22:11:00 2015

@author: steven
"""

import sys
sys.path.append('../')
import bms

R=1.
L=0.03
J=10
k=1
Tr=0.1# Torque requested on motor output

#e=bmsp.Step(1.,'e')
Ui=bms.Step(1.,'Input Voltage')
e=bms.Variable('Counter electromotive force')
Uind=bms.Variable('Voltage Inductor')
Iind=bms.Variable('Intensity Inductor')
Tm=bms.Variable('Motor torque')
Text=bms.Step(-Tr,'Outside Torque')
T=bms.Variable('Torque')
W=bms.Variable('Rotational speed')

s=bms.Variable('s')

block1=bms.SubstractBlock(Ui,e,Uind)
block2=bms.ODEBlock(Uind,Iind,[1],[R,L])
block3=bms.GainBlock(Iind,Tm,k)
block4=bms.SumBlock(Tm,Text,T)
block5=bms.ODEBlock(T,W,[1],[0,J])
block6=bms.GainBlock(W,e,1/k)
ds=bms.DynamicSystem(100,1000,[block1,block2,block3,block4,block5,block6])
#res=ds.ResolutionOrder()
#print(res)
ds.Simulate()
#ds.PlotVariables()
ds.PlotVariables([[Ui,W],[Tm,Text]])