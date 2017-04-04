# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 10:06:30 2017

@author: kkesi
"""

def word_count(string):
    new_string = string.lower().split()
    new_dict ={}
    for word in new_string:
        if word not in new_dict:
            new_dict[word] = 1

        else:
            new_dict[word] += 1
    return new_dict

string = {"I am that I am"}

print(word_count(string))