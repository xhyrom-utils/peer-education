import tkinter, random
import tkinter.font

canvas = tkinter.Canvas(width=1000, height=500)
canvas.pack()

fonts = tkinter.font.families()

for x, y, anchor in [
    (0, 0, "nw"),
    (1000, 0, "ne"),
    (0, 500, "sw"),
    (1000, 500, "se"),
    (1000 / 2, 500 / 2, "center"),
]:
    font = random.choice(fonts)
    canvas.create_text(
        x,
        y,
        text=f"({x}, {y}) {font}",
        font=(font, 24),
        anchor=anchor,
        fill="black",
    )


canvas.mainloop()
