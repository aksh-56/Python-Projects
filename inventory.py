# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 01:41:11 2021

@author: aksh
"""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
 print("Inventory:")
 item_total = 0
 for k, v in stuff.items():
 # FILL THIS PART IN
  print("Total number of items: " + str(item_total))
  displayInventory(stuff) 