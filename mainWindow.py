import tkinter as tk

def button1_clicked():
    print("Button 1 clicked!")

def button2_clicked():
    print("Button 2 clicked!")

root = tk.Tk()
root.title("Resizable Window with Buttons")

# Set the initial window size
root.geometry("800x400")

# Configure the root window to be resizable in both directions
root.resizable(True, True)

# Set the background color to white
root.configure(bg="white")

# Create the red button
button1 = tk.Button(root, text="Button 1", bg="red", fg="white", relief=tk.RAISED, bd=2, command=button1_clicked)
button1.place(relx=0.5, rely=0.9, anchor=tk.CENTER, relwidth=0.8, relheight=0.1)

# Create the green button above the red button
button2 = tk.Button(root, text="Button 2", bg="green", fg="white", relief=tk.RAISED, bd=2, command=button2_clicked)
button2.place(relx=0.5, rely=0.8, anchor=tk.CENTER, relwidth=0.8, relheight=0.1)

root.mainloop()
