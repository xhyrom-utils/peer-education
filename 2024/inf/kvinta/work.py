import tkinter

canvas = tkinter.Canvas(width=1000, height=500)
canvas.pack()

x, y = 1000 / 2, 500 / 2
canvas.create_text(
    x, y, text="ahoj", font=("Times New Roman", 24), fill="red", activefill="blue"
)
canvas.create_text(
    x + 13.5, y + 29, text="python", font=("Times New Roman", 24), angle=90
)

canvas.mainloop()
