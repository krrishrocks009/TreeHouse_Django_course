# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 16:12:11 2017

@author: kkesi
"""
import random

from combat import Combat


COLORS = ["red", "green", "blue", "orange"]


class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = "sword"
    sound = "roar"
    
    
    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)
        
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def __str__(self):
        return "{} {}, HP: {}, XP: {} ".format(self.color.title(),
                                                self.__class__.__name__,
                                                self.hit_points,
                                                self.experience)
            
    def battlecry(self):
        return self.sound.upper()
    
class Goblin(Monster):
    max_hit_points = 3
    max_experience = 2
    dound = "squeak"
    
class Dragon(Monster):
    min_hit_points = 3
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = "raaaaaaar"
    
    
    
    