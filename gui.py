import tkinter as tk
import sys

# Create a new tkinter window
root = tk.Tk()

# Create a tkinter text widget to display output
output = tk.Text(root, height=20, width=50)
output.pack()

# Create a tkinter entry widget to accept user input
entry = tk.Entry(root)
entry.pack()

# Define a function to redirect standard output to the tkinter text widget
def write(text):
    output.insert(tk.END, text)

# Redirect standard output to the tkinter text widget
sys.stdout.write = write

# Define a function to handle user input
def handle_input():
    user_input = entry.get()
    print(f"User entered: {user_input}")
    entry.delete(0, tk.END)

# Create a tkinter button to submit user input
button = tk.Button(root, text="Submit", command=handle_input)
button.pack()

# Run the tkinter main loop
root.mainloop()
