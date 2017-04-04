# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 14:22:22 2017

@author: kkesi
"""



def disemvowel(word):
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    new_word = []

    for letter in word:
        if letter not in vowels:
            new_word.append(letter)
            
    new_word = "".join(new_word)
    return new_word
    
print(disemvowel("ahgfeabbaeiouAEIHFODHU"))



    
