import tkinter as tk
from tkinter import messagebox
def press(num):
    entry_var.set(entry_var.get() + str(num))
def equalpress():
    try:
        result = str(eval(entry_var.get()))
        history.append(entry_var.get() + " = " + result)  # save to history
        entry_var.set(result)
    except:
        entry_var.set("Error")
def clear():
    entry_var.set("")
def backspace():
    current = entry_var.get()
    entry_var.set(current[:-1])
def show_history():
    if history:
        messagebox.showinfo("Calculation History", "\n".join(history))
    else:
        messagebox.showinfo("Calculation History", "No calculations yet!")
root = tk.Tk()
root.title("Simple Calculator")
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))
root.configure(bg="#222831")
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 30), bg="#393E46", fg="white", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, padx=20, pady=20, sticky="nsew")
history = []
def make_button(text, row, col, bg="#00ADB5", fg="white", command=None):
    return tk.Button(root, text=text, fg=fg, bg=bg, font=("Arial", 22, "bold"),
                     relief="raised", bd=4, command=command).grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3)
]
for (text, row, col) in buttons:
    if text == "=":
        make_button(text, row, col, bg="#FF5722", command=equalpress)
    else:
        make_button(text, row, col, command=lambda t=text: press(t))
make_button("C", 5, 0, bg="#F44336", command=clear)        # Clear
make_button("⌫", 5, 1, bg="#9C27B0", command=backspace)    # Backspace
make_button("H", 5, 2, bg="#607D8B", command=show_history) # History
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)
root.mainloop()
