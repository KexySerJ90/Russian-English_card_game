from tkinter import Tk, Canvas, PhotoImage, Button
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
cur_card = {}
to_learn = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/russian_english_adjectives.csv')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global cur_card, flip_timer
    window.after_cancel(flip_timer)
    cur_card.update(choice(to_learn))
    canvas.itemconfig(card_title, text="English", fill='black')
    canvas.itemconfig(card_word, text=cur_card["English"], fill='black')
    canvas.itemconfig(canvas_image, image=card_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="Russian", fill='white')
    canvas.itemconfig(card_word, text=cur_card["Russian"], fill='white')
    canvas.itemconfig(canvas_image, image=card_back_img)


def is_known():
    to_learn.remove(cur_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Flash card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_img)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
ri = PhotoImage(file='images/right.png')
wright_button = Button(image=ri, highlightthickness=0, borderwidth=0, command=is_known)
wright_button.grid(column=1, row=1)
wi = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wi, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(column=0, row=1)
next_card()

window.mainloop()
