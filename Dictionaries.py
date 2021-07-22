# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 13:14:43 2021

@author: aksh
"""

def printPicnic(itemsDict, leftWidth, rightWidth):
 print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
 for k, v in itemsDict.items():
  print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 80}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
