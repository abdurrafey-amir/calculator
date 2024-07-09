from tkinter import Tk, Canvas, Text, Button, PhotoImage

window = Tk()

window.geometry("600x650")
window.configure(bg = "#142F44")

canvas = Canvas(
    window,
    bg = "#142F44",
    height = 650,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    20.0,
    54.0,
    580,
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
    x=262.0,
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
    x=394.0,
    y=261,
    width=110,
    height=110
)

window.mainloop()
