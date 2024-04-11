import tkinter, random

canvas = tkinter.Canvas(width=1000, height=500)
canvas.pack()


x, y = 1000 / 2, 500 / 2
canvas.create_text(
    x,
    y,
    text="ahoj\nsvete",
    font=("Arial", 24, "bold", "underline", "italic"),
    fill=random.choice(["red", "green", "blue"]),
    activefill="purple",
    justify="center",
    # width="3m",
)

canvas.mainloop()
