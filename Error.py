# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 00:00:53 2022

@author: seong
"""

str = input()

try:
    
    if '.' in str:
        raise ValueError
except ValueError:
    print('asdasda')    