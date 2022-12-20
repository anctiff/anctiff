import time
import pyautogui
import keyboard
import threading
from tkinter import *

# Create window
window = Tk()
window.title("Auto Clicker")

# Functions
def start_bot():
    # Get interval from user input
    interval = txt.get()
    try:
        interval = int(interval)
    except ValueError:
        interval = 1  # Use default value if invalid input
    if interval <= 0:
        interval = 1  # Use default value if invalid input
        
    # Start bot in separate thread
    bot_thread = threading.Thread(target=run_bot, args=(interval,))
    bot_thread.start()
    
def run_bot(interval):
    # Initialize flag to control loop
    run = True
    
    # Initialize start time
    start = time.time()
    
    # Run loop until flag is set to False
    while run:
        # Check if 'n' key is pressed
        if keyboard.is_pressed('n'):
            run = False  # Set flag to False to stop loop
            break
            
        # Check if interval has passed
        if time.time() >= (start + interval):
            pyautogui.tripleClick()  # Triple click
            start = time.time()  # Reset start time
        else:
            pyautogui.click()  # Single click

# Create widgets
lbl = Label(window, text="Click Delay")
lbl.grid(column=1, row=0, padx=(75, 10))

txt = Entry(window, width=10)
txt.grid(column=1, row=1, padx=(75, 10))

btn = Button(window, text="Start Bot", command=start_bot, bg="Blue", fg="White")
btn.grid(column=1, row=2, padx=(75, 10), pady=(15, 10))
window.geometry('220x100')

# Run mainloop
window.mainloop()
