from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title('Flash card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

data=pandas.read_csv('data/french_words.csv')
to_learn=data.to_dict(orient="records")

def next_card():
    cur_card=choice(to_learn)
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=cur_card["French"])

# ---------------------------- UI SETUP ------------------------------- #

canvas = Canvas(width=800, height=526)
card_img = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_img)
card_title=canvas.create_text(400, 150, text='', fill='black',font=('Ariel', 40, 'italic'))
card_word=canvas.create_text(400, 263, text='', fill='black',font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0, row=0,columnspan=2)
ri=PhotoImage(file='images/right.png')
right_button = Button(image=ri, highlightthickness=0,borderwidth=0, command=next_card)
right_button.grid(column=1, row=1)
wi=PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wi, highlightthickness=0,borderwidth=0, command=next_card)
wrong_button.grid(column=0, row=1)
next_card()

window.mainloop()