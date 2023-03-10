import random
import tkinter as tk
from tkinter import messagebox

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        
        self.secret_number = random.randint(1, 100)
        self.guesses_left = 10
        
        # Create the widgets
        self.instructions_label = tk.Label(self.master, text="Guess a number between 1 and 100")
        self.guess_label = tk.Label(self.master, text="Guesses left: {}".format(self.guesses_left))
        self.guess_entry = tk.Entry(self.master)
        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_guess)
        
        # Place the widgets on the screen
        self.instructions_label.pack()
        self.guess_label.pack()
        self.guess_entry.pack()
        self.guess_button.pack()
        
    def check_guess(self):
        # Get the user's guess
        guess = int(self.guess_entry.get())
        
        # Check if the guess is correct
        if guess == self.secret_number:
            messagebox.showinfo("Congratulations", "You guessed the number!")
            self.master.destroy()
        else:
            self.guesses_left -= 1
            
            if self.guesses_left == 0:
                messagebox.showwarning("Game Over", "You ran out of guesses. The number was {}.".format(self.secret_number))
                self.master.destroy()
            else:
                message = "Incorrect. Guesses left: {}".format(self.guesses_left)
                if guess < self.secret_number:
                    message += "\nTry a higher number."
                else:
                    message += "\nTry a lower number."
                self.guess_label.config(text=message)
                self.guess_entry.delete(0, tk.END)
                
# Create the main window
root = tk.Tk()

# Create the game instance
game = GuessNumberGame(root)

# Start the game loop
root.mainloop()
