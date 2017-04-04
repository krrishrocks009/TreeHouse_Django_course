# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 10:44:21 2017

@author: kkesi
"""
a_dict = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
def num_courses(a_dict):
    values = list(a_dict.values())
    i = 0
    total = 0
    for values in a_dict:
        if len(values[i]) > 1:
            total += len(values[i])
            i += 1
        else:
            total += 1
    return total
print(num_courses(a_dict))   


def courses(teachers):
    total_courses = []
    end_result = []
    for key in teachers.items():
        total_courses.append(teachers.values())
    for courses_of_one_teacher in teachers.values():
        for course in courses_of_one_teacher:
            end_result.append(course)
    return len(end_result)
teachers = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
'Kenneth Love': ['Python Basics', 'Python Collections']}        
            
print(courses(teachers))

def most_courses(teachers):
    new_list = []
    
    for key in teachers.items():
        new_list.append(teachers.values())
        
    for course in new_list:
        
    
        print(new_list)    
    
print(most_courses(teachers))

TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)
for tile in TILES:
    if tile != "||":
        print(tile, end="")
    else:
        print()
    
            
            