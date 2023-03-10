import tkinter as tk
from tkinter import messagebox
import random

# List of suspects
suspects = ["Aiden", "Becky", "Charlie", "David", "Ella"]

# List of locations
locations = ["Office", "Kitchen", "Bedroom", "Bathroom", "Living Room"]

# List of possible murder weapons
weapons = ["Knife", "Gun", "Poison", "Rope", "Hammer"]

# Randomly select the killer, location and weapon
killer = random.choice(suspects)
location = random.choice(locations)
weapon = random.choice(weapons)

# Function to start the game
def start_game():
    # Show the game instructions
    messagebox.showinfo("Detective Game", "Welcome to the detective game! Your goal is to solve the murder mystery. You have to figure out who the killer is, in which room the murder took place and what weapon was used. Good luck!")
    
    # Create the main window
    window = tk.Tk()
    window.title("Detective Game")

    # Create the labels and entry boxes for the game
    tk.Label(window, text="Enter the name of the suspect:").grid(row=0, column=0)
    suspect_entry = tk.Entry(window)
    suspect_entry.grid(row=0, column=1)

    tk.Label(window, text="Enter the location of the murder:").grid(row=1, column=0)
    location_entry = tk.Entry(window)
    location_entry.grid(row=1, column=1)

    tk.Label(window, text="Enter the murder weapon:").grid(row=2, column=0)
    weapon_entry = tk.Entry(window)
    weapon_entry.grid(row=2, column=1)

    # Function to check the user's answers
    def check_answers():
        # Get the user's answers
        user_suspect = suspect_entry.get().strip()
        user_location = location_entry.get().strip()
        user_weapon = weapon_entry.get().strip()

        # Check the user's answers against the correct answers
        if user_suspect == killer and user_location == location and user_weapon == weapon:
            messagebox.showinfo("Detective Game", "Congratulations! You solved the murder mystery. The killer was " + killer + ", the murder took place in the " + location + " and the weapon used was " + weapon + ".")
        else:
            messagebox.showinfo("Detective Game", "Sorry, your answer is incorrect. Keep trying!")

    # Create the button to check the user's answers
    check_button = tk.Button(window, text="Check Answers", command=check_answers)
    check_button.grid(row=3, column=1)

    # Run the main loop
    window.mainloop()

# Call the start_game function to start the game
start_game()
