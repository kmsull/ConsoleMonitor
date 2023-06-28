import tkinter as tk

def start_button_clicked():
    print("Start button clicked!")
    start_button.config(state=tk.DISABLED, bg="gray")
    stop_button.config(state=tk.NORMAL, bg="red")

def stop_button_clicked():
    print("Stop button clicked!")
    stop_button.config(state=tk.DISABLED, bg="gray")
    start_button.config(state=tk.NORMAL, bg="green")

root = tk.Tk()
root.title("Resizable Window with Buttons")

# Set the initial window size
root.geometry("1600x800")

# Configure the root window to be resizable in both directions
root.resizable(True, True)

# Set the background color to white
root.configure(bg="white")

# Create the Start button
start_button = tk.Button(root, text="Start", bg="green", fg="white", relief=tk.RAISED, bd=2, command=start_button_clicked)
start_button.place(relx=0.5, rely=1.0, anchor=tk.S, relwidth=0.8, height=40, y=-70)

# Create the Stop button
stop_button = tk.Button(root, text="Stop", bg="gray", fg="white", relief=tk.RAISED, bd=2, state=tk.DISABLED, command=stop_button_clicked)
stop_button.place(relx=0.5, rely=1.0, anchor=tk.S, relwidth=0.8, height=40, y=-20)

root.mainloop()
