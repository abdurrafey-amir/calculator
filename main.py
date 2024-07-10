from tkinter import Tk, Canvas, Text, Button, PhotoImage

window = Tk()

window.geometry("500x650")
window.configure(bg = "#142F44")

canvas = Canvas(
    window,
    bg = "#142F44",
    height = 650,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    20.0,
    54.0,
    480,
    217,
    fill="#205B7A",
    outline=""
)

clear_image = PhotoImage(file=("build/assets/frame0/button_1.png"))
clear = Button(
    image=clear_image,
    background="#FA2367",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)

clear.place(
    x=20.0,
    y=275.0,
    width=237.0,
    height=96.0
)

perc_image = PhotoImage(file=("build/assets/frame0/button_2.png"))
perc = Button(
    image=perc_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)

perc.place(
    x=277.0,
    y=271.0,
    width=127,
    height=100
)

divide_image = PhotoImage(file=("build/assets/frame0/button_3.png"))
divide = Button(
    image=divide_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)

divide.place(
    x=424.0,
    y=261,
    width=110,
    height=110
)

seven_image = PhotoImage(file=("build/assets/frame0/button_4.png"))
seven = Button(
    image=seven_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)

seven.place(
    x=381,
    y=383,
    width=116,
    height=98
)

eight_image = PhotoImage(file=("build/assets/frame0/button_5.png"))
eight = Button(
    image=eight_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)

eight.place(
    x=381,
    y=497,
    width=120,
    height=96
)

nine_image = PhotoImage(file=("build/assets/frame0/button_6.png"))
nine = Button(
    image=nine_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)

nine.place(
    x=389,
    y=607,
    width=109,
    height=105
)

four_image = PhotoImage(file=("build/assets/frame0/button_7.png"))
four = Button(
    image=four_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)

four.place(
    x=381,
    y=724,
    width=114,
    height=95
)

five_image = PhotoImage(file=("build/assets/frame0/button_8.png"))
five = Button(
    image=five_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)

five.place(
    x=23,
    y=383,
    width=121,
    height=102
)

six_image = PhotoImage(file=("build/assets/frame0/button_9.png"))
six = Button(
    image=six_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)

six.place(
    x=139,
    y=367,
    width=123,
    height=118
)

window.mainloop()
