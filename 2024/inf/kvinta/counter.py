import tkinter

canvas = tkinter.Canvas(width=1000, height=500)
canvas.pack()

count_element = canvas.create_text(
    1000 / 2,
    500 / 2,
    text="0",
    font=("Arial", 24),
    fill="black",
)

for x in range(1, 100):
    canvas.itemconfig(count_element, text=str(x))
    canvas.update()
    canvas.after(1000)

canvas.mainloop()
