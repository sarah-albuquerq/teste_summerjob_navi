# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 12:40:19 2020

@author: sarah
"""

S = 0
for x in range(1, 5000000):
    if (x % 2 == 0) and (x % 49 == 0) and (x % 37 == 0):
        S = S + 1
print(S)

