from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage




window = Tk()


window.geometry("550x650")
window.configure(bg= "#142F44")


canvas = Canvas(
    window,
    bg="#142F44",
    height=600,
    width=650,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
# inp = Entry(
#     bg="#205B7a",
# )
# inp.place(
#     x=44,
#     y=479
# )
canvas.create_rectangle(
    44.0,
    54.0,
    480,
    217,
    fill="#205B7A",
    outline=""
)

clear_image = PhotoImage(file=("build/assets/frame0/clear.png"))
clear = Button(
    image=clear_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("clear clicked"),
    relief="flat"
)

clear.place(
    x=25.0,
    y=275,
    width=237,
    height=96
)

perc_image = PhotoImage(file=("build/assets/frame0/perc.png"))
perc = Button(
    image=perc_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("perc clicked"),
    relief="flat"
)

perc.place(
    x=262,
    y=271,
    width=127,
    height=100
)

divide_image = PhotoImage(file=("build/assets/frame0/divide.png"))
divide = Button(
    image=divide_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("divide clicked"),
    relief="flat"
)

divide.place(
    x=389,
    y=261,
    width=110,
    height=110
)

seven_image = PhotoImage(file=("build/assets/frame0/seven.png"))
seven = Button(
    image=seven_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("seven clicked"),
    relief="flat"
)

seven.place(
    x=381,
    y=383,
    width=116,
    height=98
)

eight_image = PhotoImage(file=("build/assets/frame0/eight.png"))
eight = Button(
    image=eight_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("eight clicked"),
    relief="flat"
)

eight.place(
    x=381,
    y=497,
    width=120,
    height=96
)

nine_image = PhotoImage(file=("build/assets/frame0/nine.png"))
nine = Button(
    image=nine_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("nine clicked"),
    relief="flat"
)

nine.place(
    x=389,
    y=607,
    width=109,
    height=105
)

multiply_image = PhotoImage(file=("build/assets/frame0/multiply.png"))
multiply = Button(
    image=multiply_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("multiply clicked"),
    relief="flat"
)

multiply.place(
    x=381,
    y=724,
    width=114,
    height=95
)

four_image = PhotoImage(file=("build/assets/frame0/four.png"))
four = Button(
    image=four_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("four clicked"),
    relief="flat"
)

four.place(
    x=23,
    y=383,
    width=121,
    height=102
)

five_image = PhotoImage(file=("build/assets/frame0/five.png"))
five = Button(
    image=five_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("five clicked"),
    relief="flat"
)

five.place(
    x=139,
    y=367,
    width=123,
    height=118
)

six_image = PhotoImage(file=("build/assets/frame0/six.png"))
six = Button(
    image=six_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("six clicked"),
    relief="flat"
)

six.place(
    x=262,
    y=383,
    width=119,
    height=102
)

sub_image = PhotoImage(file=("build/assets/frame0/sub.png"))
sub = Button(
    image=sub_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("sub clicked"),
    relief="flat"
)

sub.place(
    x=262,
    y=495,
    width=119,
    height=108
)


window.mainloop()