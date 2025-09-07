import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry.get() + button_text)

# Create the main window
root = tk.Tk()
root.title("Deez_Puff Calculator")
root.geometry("600x700")
root.resizable(False, False)
root.configure(bg="#000000")

# Entry widget to show expression
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Create and place buttons
for row_index, row in enumerate(buttons):
    frame = tk.Frame(root, bg="#000000")
    frame.pack(expand=True, fill="both")
    for col_index, button_text in enumerate(row):
        btn = tk.Button(frame, text=button_text, font=("Arial", 20), fg="white", bg="#FF0000",
                        activebackground="#050606", activeforeground="white",
                        borderwidth=0, command=lambda x=button_text: on_click(x))
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)

# Run the application
root.mainloop()
