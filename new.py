from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

window = Tk()
window.geometry("485x750")
window.configure(bg="#142F44")

canvas = Canvas(window, bg="#142F44", height=750, width=485, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# canvas.create_rectangle(25.0, 40.0, 465, 200, fill="#205B7A", outline="")

inp = Entry(bg="#205B7A", fg="white", font=("Arial", 15), bd=0, highlightthickness=0, relief="flat")
inp.place(x=25, y=40, width=440, height=150)

button_width = 100
button_height = 90
button_spacing = 10
button_x = 25
button_y = 225



def add_1():
    inp.insert('end', 1)

def add_2():
    inp.insert('end', 2)

def add_3():
    inp.insert('end', 3)

def add_4():
    inp.insert('end', 4)

def add_5():
    inp.insert('end', 5)

def add_6():
    inp.insert('end', 6)

def add_7():
    inp.insert('end', 7)

def add_8():
    inp.insert('end', 8)

def add_9():
    inp.insert('end', 9)

def add_0():
    inp.insert('end', 0)

def add_perc():
    inp.insert('end', "%")

def add_divide():
    inp.insert('end', "÷")

def add_multiply():
    inp.insert('end', "×")

def add_sub():
    inp.insert('end', "-")

def add_plus():
    inp.insert('end', "+")

def add_dot():
    inp.insert('end', ".")

clear_image = PhotoImage(file=("build/assets/frame0/clear.png"))
clear = Button(image=clear_image, borderwidth=0, highlightthickness=0, command=lambda: print("clear clicked"), relief="flat")
clear.place(x=button_x, y=button_y, width=2*button_width, height=button_height)

perc_image = PhotoImage(file=("build/assets/frame0/perc.png"))
perc = Button(image=perc_image, borderwidth=0, highlightthickness=0, command=lambda: add_perc(), relief="flat")
perc.place(x=button_x + 2*(button_width + button_spacing), y=button_y, width=button_width, height=button_height)

divide_image = PhotoImage(file=("build/assets/frame0/divide.png"))
divide = Button(image=divide_image, borderwidth=0, highlightthickness=0, command=lambda: add_divide(), relief="flat")
divide.place(x=button_x + 3*(button_width + button_spacing), y=button_y, width=button_width, height=button_height)

seven_image = PhotoImage(file=("build/assets/frame0/seven.png"))
seven = Button(image=seven_image, borderwidth=0, highlightthickness=0, command=lambda: add_7(), relief="flat")
seven.place(x=button_x, y=button_y + button_height + button_spacing, width=button_width, height=button_height)

eight_image = PhotoImage(file=("build/assets/frame0/eight.png"))
eight = Button(image=eight_image, borderwidth=0, highlightthickness=0, command=lambda: add_8(), relief="flat")
eight.place(x=button_x + button_width + button_spacing, y=button_y + button_height + button_spacing, width=button_width, height=button_height)

nine_image = PhotoImage(file=("build/assets/frame0/nine.png"))
nine = Button(image=nine_image, borderwidth=0, highlightthickness=0, command=lambda: add_9(), relief="flat")
nine.place(x=button_x + 2*(button_width + button_spacing), y=button_y + button_height + button_spacing, width=button_width, height=button_height)

multiply_image = PhotoImage(file=("build/assets/frame0/multiply.png"))
multiply = Button(image=multiply_image, borderwidth=0, highlightthickness=0, command=lambda: add_multiply(), relief="flat")
multiply.place(x=button_x + 3*(button_width + button_spacing), y=button_y + (button_height + button_spacing), width=button_width, height=button_height)

four_image = PhotoImage(file=("build/assets/frame0/four.png"))
four = Button(image=four_image, borderwidth=0, highlightthickness=0, command=lambda: add_4(), relief="flat")
four.place(x=button_x, y=button_y + 2*(button_height + button_spacing), width=button_width, height=button_height)

five_image = PhotoImage(file=("build/assets/frame0/five.png"))
five = Button(image=five_image, borderwidth=0, highlightthickness=0, command=lambda: add_5(), relief="flat")
five.place(x=button_x + button_width + button_spacing, y=button_y + 2*(button_height + button_spacing), width=button_width, height=button_height)

six_image = PhotoImage(file=("build/assets/frame0/six.png"))
six = Button(image=six_image, borderwidth=0, highlightthickness=0, command=lambda: add_6(), relief="flat")
six.place(x=button_x + 2*(button_width + button_spacing), y=button_y + 2*(button_height + button_spacing), width=button_width, height=button_height)

sub_image = PhotoImage(file=("build/assets/frame0/sub.png"))
sub = Button(image=sub_image, borderwidth=0, highlightthickness=0, command=lambda: add_sub(), relief="flat")
sub.place(x=button_x + 3*(button_width + button_spacing), y=button_y + 2*(button_height + button_spacing), width=button_width, height=button_height)

one_image = PhotoImage(file=("build/assets/frame0/one.png"))
one = Button(image=one_image, borderwidth=0, highlightthickness=0, command=lambda: add_1(), relief="flat")
one.place(x=button_x, y=button_y + 3*(button_height + button_spacing), width=button_width, height=button_height)

two_image = PhotoImage(file=("build/assets/frame0/two.png"))
two = Button(image=two_image, borderwidth=0, highlightthickness=0, command=lambda: add_2(), relief="flat")
two.place(x=button_x + button_width + button_spacing, y=button_y + 3*(button_height + button_spacing), width=button_width, height=button_height)

three_image = PhotoImage(file=("build/assets/frame0/three.png"))
three = Button(image=three_image, borderwidth=0, highlightthickness=0, command=lambda: add_3(), relief="flat")
three.place(x=button_x + 2*(button_width + button_spacing), y=button_y + 3*(button_height + button_spacing), width=button_width, height=button_height)

plus_image = PhotoImage(file=("build/assets/frame0/plus.png"))
plus = Button(image=plus_image, borderwidth=0, highlightthickness=0, command=lambda: add_plus(), relief="flat")
plus.place(x=button_x + 3*(button_width + button_spacing), y=button_y + 3*(button_height + button_spacing), width=button_width, height=button_height)

signs_image = PhotoImage(file=("build/assets/frame0/signs.png"))
signs = Button(image=signs_image, borderwidth=0, highlightthickness=0, command=lambda: print("signs clicked"), relief="flat")
signs.place(x=button_x, y=button_y + 4*(button_height + button_spacing), width=button_width, height=button_height)

zero_image = PhotoImage(file=("build/assets/frame0/zero.png"))
zero = Button(image=zero_image, borderwidth=0, highlightthickness=0, command=lambda: add_0(), relief="flat")
zero.place(x=button_x + button_width + button_spacing, y=button_y + 4*(button_height + button_spacing), width=button_width, height=button_height)

dot_image = PhotoImage(file=("build/assets/frame0/dot.png"))
dot = Button(image=dot_image, borderwidth=0, highlightthickness=0, command=lambda: add_dot(), relief="flat")
dot.place(x=button_x + 2*(button_width + button_spacing), y=button_y + 4*(button_height + button_spacing), width=button_width, height=button_height)

equal_image = PhotoImage(file=("build/assets/frame0/equal.png"))
equal = Button(image=equal_image, borderwidth=0, highlightthickness=0, command=lambda: print("equal clicked"), relief="flat")
equal.place(x=button_x + 3*(button_width + button_spacing), y=button_y + 4*(button_height + button_spacing), width=button_width, height=button_height)

window.mainloop()