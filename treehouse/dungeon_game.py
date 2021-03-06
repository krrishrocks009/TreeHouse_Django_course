# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:14:27 2017

@author: kkesi
"""
import random
import os

#draw grid
#pick random location for player
#pick random location for door
#pick random location for monster
#draw player in the grid
#take input for movement
#move player, unless invalid move(past edges of grid)
#check for win/loss
#clear screen / redraw grid

CELLS =[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

        
def clear_system():
    os.system("cls" if os.name == "nt" else "clear")
        
def get_locations():
    return random.sample(CELLS, 3)
    
    
def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "up":
        y -= 1
    if move == "DOWN":
        y += 1
    return x, y
    
    
def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    return moves
    
def draw_map(player):
    print(" _"*5)
    tile = "|{}"
    
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)
        
    
def game_loop():
    monster, door, player = get_locations() 
    
    while True:
        clear_system()
        draw_map(player)
        valid_moves = get_moves(player)
        
        print("You're currently in room {}".format(player))
        print("You can move {}".format(", ".join(valid_moves)))
        print("Enter QUIT to quit")
        
        move = input("> ")
        move = move.upper()
        
        if move == 'QUIT':
            print("\n ** See you again!**\n")
            break
        if move in valid_moves:
            player = move_player(player, move)
            
            
            if player == monster:
                print("\n ** On no! The monster got you! Better Luck next time!**\n")
                
                break
            if player == door:
                print("\n ** You escaped! congragulations!!**\n")
                break
                
        else:
            input("\n **walls are hard! Don't run into them! **\n ")
        
    else:
        if input("Play again? [y/n]").lower() != "n":
            game_loop()

   


        
clear_system()
print("Welocome to the dungeon")
input("Press return to start!")
clear_system()
game_loop()
        
    


