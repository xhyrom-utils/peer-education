import tkinter, random

canvas = tkinter.Canvas(width=1000, height=500)
canvas.pack()


x, y = 1000 / 2, 500 / 2
canvas.create_text(
    x,
    y,
    text="ahoj",
    font=("Arial", 24),
    fill=random.choice(["red", "green", "blue"]),
)

canvas.create_text(
    x,
    y + 60,
    text="python",
    font=("Arial", 24),
    fill=random.choice(["red", "green", "blue"]),
    angle=90,
)

canvas.mainloop()
