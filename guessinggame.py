# TASK 2 Guessing game

import random
from tkinter import *

x = random.randint(1, 100)

attempts = 0
while(True):
    a=int(input("Enter the number between 1 to 100  "))
    attempts= attempts+1

    if a==x:
        print("Congratulation Your guessed it in", attempts  ,"attempt")

    elif a<x:
        print("Try higher \n",attempts ,"attempt")

    elif a>x:
         print("Try lower \n",attempts ,"attempt")
