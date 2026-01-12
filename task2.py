"""
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the game

This will be silimar to something you have already done, but in this task you 
are breaking the code up into different sections to make each a function.
"""
import random
from rich import print
def Title():
    print("Guess a number from 1 to 100")
    print("If it's right you win if not guess again")
    print("----------------------------------------")
def Game():
    num = random.randint(1,100)
    win = False
    while win == False:
     guess= int(input("Guess a number:"))
     if guess == num:
         print("[bold blue]Yay you win!![/bold blue]")
         win = True
     else:
         print("[bold red]Wrong try again[/bold red]")
         continue


Title()   
Game()



