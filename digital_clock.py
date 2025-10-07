# Digital Clock using Tkinter

import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Configure window size
root.geometry("400x150")
root.resizable(False, False)

# Clock label
label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="cyan")
label.pack(anchor="center", pady=20)

def time():
    # Get current time
    current_time = strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    current_time_24 = strftime("%H:%M:%S")   # 24-hour format
    label.config(text=f"{current_time}\n{current_time_24}")
    label.after(1000, time)  # Update every 1 second

time()  # Initialize clock

root.mainloop()
