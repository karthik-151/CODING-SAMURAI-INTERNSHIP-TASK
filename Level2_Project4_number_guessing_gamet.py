import tkinter as tk
import random
from tkinter import messagebox

# Game setup
secret_number = random.randint(1, 50)
attempts_left = 10

# Function to check guess
def check_guess():
    global attempts_left, secret_number
    
    try:
        guess = int(entry_guess.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number!")
        return
    
    if guess < 1 or guess > 50:
        messagebox.showwarning("Out of Range", "Enter a number between 1 and 50")
        return
    
    attempts_left -= 1
    
    if guess == secret_number:
        messagebox.showinfo("Congratulations!", f"You guessed it right! The number was {secret_number}")
        reset_game()
    elif attempts_left == 0:
        messagebox.showinfo("Game Over", f"You ran out of attempts! The number was {secret_number}")
        reset_game()
    elif guess < secret_number:
        label_result.config(text=f"Too Low! Attempts left: {attempts_left}")
    else:
        label_result.config(text=f"Too High! Attempts left: {attempts_left}")

# Reset function
def reset_game():
    global secret_number, attempts_left
    secret_number = random.randint(1, 50)
    attempts_left = 10
    label_result.config(text="New Game Started! Guess a number between 1 and 50")
    entry_guess.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.config(bg="#f2e6ff")

label_title = tk.Label(root, text="🎮 Guess the Number (1-50)", font=("Arial", 16, "bold"), bg="#f2e6ff")
label_title.pack(pady=10)

label_instruction = tk.Label(root, text="Enter your guess:", font=("Arial", 12), bg="#f2e6ff")
label_instruction.pack()

entry_guess = tk.Entry(root, font=("Arial", 12))
entry_guess.pack(pady=5)

btn_check = tk.Button(root, text="Check Guess", command=check_guess, font=("Arial", 12), bg="#d9b3ff")
btn_check.pack(pady=10)

label_result = tk.Label(root, text="You have 10 attempts. Start guessing!", font=("Arial", 12), bg="#f2e6ff")
label_result.pack(pady=20)

btn_reset = tk.Button(root, text="Reset Game", command=reset_game, font=("Arial", 12), bg="#c299ff")
btn_reset.pack(pady=5)

root.mainloop()
