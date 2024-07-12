from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

window = Tk()
window.geometry("550x750")
window.configure(bg="#142F44")

canvas = Canvas(window, bg="#142F44", height=750, width=550, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

canvas.create_rectangle(25.0, 40.0, 525, 200, fill="#205B7A", outline="")

button_width = 100
button_height = 90
button_spacing = 10
button_x = 25
button_y = 225

clear_image = PhotoImage(file=("build/assets/frame0/clear.png"))
clear = Button(image=clear_image, borderwidth=0, highlightthickness=0, command=lambda: print("clear clicked"), relief="flat")
clear.place(x=button_x, y=button_y, width=button_width, height=button_height)

perc_image = PhotoImage(file=("build/assets/frame0/perc.png"))
perc = Button(image=perc_image, borderwidth=0, highlightthickness=0, command=lambda: print("perc clicked"), relief="flat")
perc.place(x=button_x + button_width + button_spacing, y=button_y, width=button_width, height=button_height)

divide_image = PhotoImage(file=("build/assets/frame0/divide.png"))
divide = Button(image=divide_image, borderwidth=0, highlightthickness=0, command=lambda: print("divide clicked"), relief="flat")
divide.place(x=button_x + 2*(button_width + button_spacing), y=button_y, width=button_width, height=button_height)

seven_image = PhotoImage(file=("build/assets/frame0/seven.png"))
seven = Button(image=seven_image, borderwidth=0, highlightthickness=0, command=lambda: print("seven clicked"), relief="flat")
seven.place(x=button_x, y=button_y + button_height + button_spacing, width=button_width, height=button_height)

eight_image = PhotoImage(file=("build/assets/frame0/eight.png"))
eight = Button(image=eight_image, borderwidth=0, highlightthickness=0, command=lambda: print("eight clicked"), relief="flat")
eight.place(x=button_x + button_width + button_spacing, y=button_y + button_height + button_spacing, width=button_width, height=button_height)

nine_image = PhotoImage(file=("build/assets/frame0/nine.png"))
nine = Button(image=nine_image, borderwidth=0, highlightthickness=0, command=lambda: print("nine clicked"), relief="flat")
nine.place(x=button_x + 2*(button_width + button_spacing), y=button_y + button_height + button_spacing, width=button_width, height=button_height)

multiply_image = PhotoImage(file=("build/assets/frame0/multiply.png"))
multiply = Button(image=multiply_image, borderwidth=0, highlightthickness=0, command=lambda: print("multiply clicked"), relief="flat")
multiply.place(x=button_x + 3*(button_width + button_spacing), y=button_y, width=button_width, height=button_height)

four_image = PhotoImage(file=("build/assets/frame0/four.png"))
four = Button(image=four_image, borderwidth=0, highlightthickness=0, command=lambda: print("four clicked"), relief="flat")
four.place(x=button_x, y=button_y + 2*(button_height + button_spacing), width=button_width, height=button_height)

five_image = PhotoImage(file=("build/assets/frame0/five.png"))
five = Button(image=five_image, borderwidth=0, highlightthickness=0, command=lambda: print("five clicked"), relief="flat")
five.place(x=button_x + button_width + button_spacing, y=button_y + 2*(button_height + button_spacing), width=button_width, height=button_height)

six_image = PhotoImage(file=("build/assets/frame0/six.png"))
six = Button(image=six_image, borderwidth=0, highlightthickness=0, command=lambda: print("six clicked"), relief="flat")
six.place(x=button_x + 2*(button_width + button_spacing), y=button_y + 2*(button_height + button_spacing), width=button_width, height=button_height)

sub_image = PhotoImage(file=("build/assets/frame0/sub.png"))
sub = Button(image=sub_image, borderwidth=0, highlightthickness=0, command=lambda: print("sub clicked"), relief="flat")
sub.place(x=button_x + 3*(button_width + button_spacing), y=button_y + button_height + button_spacing, width=button_width, height=button_height)

one_image = PhotoImage(file=("build/assets/frame0/one.png"))
one = Button(image=one_image, borderwidth=0, highlightthickness=0, command=lambda: print("one clicked"), relief="flat")
one.place(x=button_x, y=button_y + 3*(button_height + button_spacing), width=button_width, height=button_height)

two_image = PhotoImage(file=("build/assets/frame0/two.png"))
two = Button(image=two_image, borderwidth=0, highlightthickness=0, command=lambda: print("two clicked"), relief="flat")
two.place(x=button_x + button_width + button_spacing, y=button_y + 3*(button_height + button_spacing), width=button_width, height=button_height)

three_image = PhotoImage(file=("build/assets/frame0/three.png"))
three = Button(image=three_image, borderwidth=0, highlightthickness=0, command=lambda: print("three clicked"), relief="flat")
three.place(x=button_x + 2*(button_width + button_spacing), y=button_y + 3*(button_height + button_spacing), width=button_width, height=button_height)

plus_image = PhotoImage(file=("build/assets/frame0/plus.png"))
plus = Button(image=plus_image, borderwidth=0, highlightthickness=0, command=lambda: print("plus clicked"), relief="flat")
plus.place(x=button_x + 3*(button_width + button_spacing), y=button_y + 2*(button_height + button_spacing), width=button_width, height=button_height)

zero_image = PhotoImage(file=("build/assets/frame0/zero.png"))
zero = Button(image=zero_image, borderwidth=0, highlightthickness=0, command=lambda: print("zero clicked"), relief="flat")
zero.place(x=button_x, y=button_y + 4*(button_height + button_spacing), width=button_width, height=button_height)

dot_image = PhotoImage(file=("build/assets/frame0/dot.png"))
dot = Button(image=dot_image, borderwidth=0, highlightthickness=0, command=lambda: print("dot clicked"), relief="flat")
dot.place(x=button_x + button_width + button_spacing, y=button_y + 4*(button_height + button_spacing), width=button_width, height=button_height)

equal_image = PhotoImage(file=("build/assets/frame0/equal.png"))
equal = Button(image=equal_image, borderwidth=0, highlightthickness=0, command=lambda: print("equal clicked"), relief="flat")
equal.place(x=button_x + 2*(button_width + button_spacing), y=button_y + 4*(button_height + button_spacing), width=button_width, height=button_height)

window.mainloop()