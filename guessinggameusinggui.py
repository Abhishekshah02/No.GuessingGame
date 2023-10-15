import random
from tkinter import *

a = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    x = int(guess_entry.get())
    attempts += 1

    if x <a :
        result_label.config(text=f"Try higher! (Attempts: {attempts})")
    elif x >a:
        result_label.config(text=f"Try lower! (Attempts: {attempts})")
    else:
        result_label.config(text=f"Congratulations! You guessed it in {attempts} attempts.")
        guess_button.config(state=DISABLED)
    guess_entry.delete(0, END)    

root = Tk()
root.title("Number Guessing Game")

root.geometry("300x200")

instruction_label = Label(root, text="Guess a number between 1 and 100:")
instruction_label.pack()

guess_entry = Entry(root)
guess_entry.pack()

guess_button = Button(root, text="Submit Guess", command=check_guess)
guess_button.pack()

result_label = Label(root)
result_label.pack()

root.mainloop()