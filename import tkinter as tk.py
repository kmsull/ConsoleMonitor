import tkinter as tk

def button_clicked():
    print("Button clicked!")

root = tk.Tk()
root.title("Resizable Window with Button")
root.geometry("400x300")  # Initial size of the window

# Configure the root window to be resizable in both directions
root.resizable(True, True)

# Set the background color to white
root.configure(bg="white")

# Create a frame to hold the button
frame = tk.Frame(root)
frame.pack()

# Create the green, square button with rounded edges
button = tk.Button(frame, text="Click me!", bg="green", fg="white", relief=tk.RAISED, bd=2, command=button_clicked)
button.pack(padx=10, pady=10)

# Place the button 150 pixels from the bottom and right edges
button.place(relx=1.0, rely=1.0, x=-150, y=-150, anchor=tk.SE)

root.mainloop()
