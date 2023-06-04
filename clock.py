

import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

# Create a tkinter window
window = tk.Tk()
window.title('Digital Clock')

# Create a label for the clock
clock_label = tk.Label(window, font=('Arial', 80))
clock_label.pack(padx=50, pady=50)

# Update the clock initially
update_clock()

# Start the tkinter event loop
window.mainloop()
