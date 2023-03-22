import tkinter as tk
import random

class CricketGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Cricket Game")

        # Labels
        self.runs_label = tk.Label(master, text="Runs: 0")
        self.runs_label.pack()

        self.wickets_label = tk.Label(master, text="Wickets: 0")
        self.wickets_label.pack()

        # Buttons
        self.hit_button = tk.Button(master, text="Hit", command=self.hit)
        self.hit_button.pack()

        # Initialize the game variables
        self.runs = 0
        self.wickets = 0

    def hit(self):
        # Generate a random number between 0 and 6
        run = random.randint(0, 6)

        # Update the runs and wickets
        if run == 0:
            self.wickets += 1
            self.wickets_label.config(text="Wickets: " + str(self.wickets))
        else:
            self.runs += run
            self.runs_label.config(text="Runs: " + str(self.runs))

        # Check if the game is over
        if self.wickets == 10:
            self.hit_button.config(state="disabled")
            self.runs_label.config(text="Game Over - Runs: " + str(self.runs))

# Create the main window and start the game
root = tk.Tk()
game = CricketGame(root)
root.mainloop()
