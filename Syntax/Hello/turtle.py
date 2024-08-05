# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:52:50 2024

@author: soyoung
"""

# turtle
import turtle

t=turtle.Pen()

for x in range(100):    
    t.forward(x)        #전진 0~99
    t.left(90)          #회전(왼쪽으로 90도)

turtle.done()

#%%
t=turtle.Pen()
for x in range(100):
    t.circle(100)
    t.left(5)
    
turtle.done()