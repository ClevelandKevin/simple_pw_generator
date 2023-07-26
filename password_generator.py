import random
import tkinter as tk
from tkinter import messagebox

### Used characters ###
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    try:
        number_of_letters = int(entry_letters.get())
        number_of_numbers = int(entry_numbers.get())
        number_of_symbols = int(entry_symbols.get())
        
        if number_of_letters < 0 or number_of_numbers < 0 or number_of_symbols < 0:
            messagebox.showerror("Error", "Please enter non-negative values.")
            return
        
        if number_of_letters + number_of_numbers + number_of_symbols == 0:
            messagebox.showerror("Error", "Please enter at least one character for the password.")
            return

        ### Here the list is filled with different characters ###
        password_list = []

        for char in range(number_of_letters):
            password_list.append(random.choice(letters))

        for char in range(number_of_numbers):
            password_list.append(random.choice(numbers))

        for char in range(number_of_symbols):
            password_list.append(random.choice(symbols))

        ### The list is scrambled and then output individually ###
        random.shuffle(password_list)

        password = "".join(password_list)

        entry_result.delete(0, tk.END)
        entry_result.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and arrange the GUI elements
lbl_letters = tk.Label(root, text="How many letters should be used?")
lbl_letters.pack()

entry_letters = tk.Entry(root)
entry_letters.pack()

lbl_numbers = tk.Label(root, text="How many numbers should be used?")
lbl_numbers.pack()

entry_numbers = tk.Entry(root)
entry_numbers.pack()

lbl_symbols = tk.Label(root, text="How many symbols should be used?")
lbl_symbols.pack()

entry_symbols = tk.Entry(root)
entry_symbols.pack()

btn_generate = tk.Button(root, text="Generate Password", command=generate_password)
btn_generate.pack()

entry_result = tk.Entry(root, readonlybackground="white")
entry_result.pack()

# Start the main event loop
root.mainloop()
