# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 15:07:09 2017

@author: kkesi
"""

messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]
 
messy_list.insert(0, messy_list.pop(3))



# Your code goes below here

def list(messy_list):
    for obj in messy_list:
        if type(obj) is not int:
            messy_list.remove(obj)
    return print(messy_list)  
         
new_list = messy_list.pop()
    
messy_list.extend(new_list)
list(messy_list)


