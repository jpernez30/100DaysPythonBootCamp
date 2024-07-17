
from tkinter import *


random_words = [
    "apple", "banana", "cat", "dog", "elephant", "frog", "giraffe", "house", "island", "jacket",
    "kite", "lemon", "mountain", "notebook", "orange", "pencil", "queen", "rabbit", "sandwich", "table",
    "umbrella", "violin", "window", "xylophone", "yellow", "zebra", "airplane", "balloon", "chocolate", "dolphin",
    "eagle", "flower", "guitar", "horse", "ice", "jellyfish", "kangaroo", "lion", "moon", "nest",
    "octopus", "penguin", "quail", "rainbow", "star", "tree", "unicorn", "volcano", "whale", "yogurt",
    "ant", "bear", "car", "drum", "egg", "fish", "goat", "hat", "igloo", "jam",
    "key", "lamp", "mouse", "nurse", "owl", "piano", "quilt", "rose", "snake", "tiger",
    "umbrella", "vase", "wolf", "x-ray", "yacht", "zoo", "anchor", "bicycle", "cake", "dragon",
    "envelope", "fan", "ghost", "hammer", "iguana", "jelly", "kite", "leaf", "moon", "necklace",
    "ostrich", "pumpkin", "quilt", "rocket", "sheep", "turtle", "unicorn", "violin", "water", "xylophone"
]
current_index = 0
letter_index = 0


def count_down(count):
    canvas.itemconfig(timer_text, text=f"{count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        my_label.config(text=f'Your speed is {round(current_index+1/60,2)} per minute')

def start_timer():
    #hide start button
    start_button.grid_forget()
    #Show first word
    my_label.config(text=random_words[current_index])
    # Start the game
    count_down(60);

def check_letter(letter):
    global current_index, letter_index
    # Letter of current word is typed, check word and index
    print(len(random_words[current_index]))
    if(letter == random_words[current_index][letter_index]):
        letter_index = letter_index +1
        # if end of letter is reached, change word
        if(letter_index == len(random_words[current_index])):
            # reset word_index
            letter_index = 0;
            # increase current_index, get a new word
            current_index = current_index + 1;
            #update the on screen
            my_label.config(text=random_words[current_index])

def key_handler(event):
    check_letter(event.char)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

my_label = Label(text="", font=("Arial", 24, "bold"))
my_label.config(text="Speed typer")
my_label.grid(column=0, row=1)
moving = Label(text="^", font=("Arial", 24, "bold"))
moving.config(padx=0)
moving.grid(column=0, row=2)

my_label.config(padx=0, pady=25)
canvas = Canvas(width=100, height=100, bg="#e7305b", highlightthickness=0)
canvas.grid(column=0, row=0)
timer_text = canvas.create_text(50, 50, text="00", fill="white", font=("Courier", 35, "bold"))

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

window.bind("<Key>", key_handler)

window.mainloop()
