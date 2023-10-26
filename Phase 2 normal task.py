# Import modules
import tkinter as tk
import random
import time

# Create a list of words to choose from
words = ["apple", "banana", "cherry", "dragon", "elephant", "flower", "giraffe", "honey", "icecream", "jacket"]

# Define global variables
start_time = 0 # To store the start time of typing
end_time = 0 # To store the end time of typing
word_count = 0 # To count the number of words typed
correct_count = 0 # To count the number of correct words typed

# Define functions
def start():
    """This function starts the timer and displays a random word"""
    global start_time, word_count
    start_time = time.time() # Record the current time
    word_count = 0 # Reset the word count
    display_word() # Call the display_word function

def display_word():
    """This function displays a random word from the list"""
    global word_label, entry_box, word_count
    word_label.config(text=random.choice(words)) # Set the text of the word label to a random word
    entry_box.delete(0, tk.END) # Clear the entry box
    entry_box.focus() # Set the focus to the entry box
    word_count += 1 # Increment the word count

def check_word(event):
    """This function checks if the entered word matches the displayed word and updates the score"""
    global word_label, entry_box, correct_count, score_label
    if entry_box.get().lower() == word_label.cget("text").lower(): # If the entered word matches the displayed word (case-insensitive)
        correct_count += 1 # Increment the correct count
        score_label.config(text=f"Score: {correct_count}/{word_count}") # Update the score label
    display_word() # Call the display_word function

def stop():
    """This function stops the timer and calculates the typing speed"""
    global start_time, end_time, word_count, correct_count, speed_label
    end_time = time.time() # Record the current time
    elapsed_time = end_time - start_time # Calculate the elapsed time in seconds
    speed = (word_count / elapsed_time) * 60 # Calculate the typing speed in words per minute
    speed_label.config(text=f"Speed: {speed:.2f} WPM") # Update the speed label
    word_count = 0 # Reset the word count
    correct_count = 0 # Reset the correct count

# Create a window
window = tk.Tk()
window.title("Typing Speed Tester")
window.geometry("300x200")

# Create widgets
word_label = tk.Label(window, text="", font=("Arial", 20)) # A label to display a random word
entry_box = tk.Entry(window) # An entry box to type the word
start_button = tk.Button(window, text="Start", command=start) # A button to start the timer and display a word
stop_button = tk.Button(window, text="Stop", command=stop) # A button to stop the timer and calculate the speed
score_label = tk.Label(window, text="Score: 0/0") # A label to show the score (correct/total)
speed_label = tk.Label(window, text="Speed: 0.00 WPM") # A label to show the speed (words per minute)

# Arrange widgets on a grid
word_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
entry_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
start_button.grid(row=2, column=0, padx=10, pady=10)
stop_button.grid(row=2, column=1, padx=10, pady=10)
score_label.grid(row=3, column=0, padx=10, pady=10)
speed_label.grid(row=3, column=1, padx=10, pady=10)

# Bind the return key to the check_word function
window.bind("<Return>", check_word)

# Start the main loop
window.mainloop()
