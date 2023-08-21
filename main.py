from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title('Flash card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)




# ---------------------------- UI SETUP ------------------------------- #

canvas = Canvas(width=800, height=526)
card_img = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_img)
canvas.create_text(400, 150, text='Title', fill='black',font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text='word', fill='black',font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0, row=0,columnspan=2)
ri=PhotoImage(file='images/right.png')
right_button = Button(image=ri, highlightthickness=0,borderwidth=0)
right_button.grid(column=1, row=1)
wi=PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wi, highlightthickness=0,borderwidth=0)
wrong_button.grid(column=0, row=1)

window.mainloop()