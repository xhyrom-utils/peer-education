import tkinter

canvas = tkinter.Canvas(width=1000, height=500)
canvas.pack()

x, y = 100, 100
x1, y1 = 202, 102

canvas.create_rectangle(x, y, x1, y1, fill="blue")
canvas.mainloop()