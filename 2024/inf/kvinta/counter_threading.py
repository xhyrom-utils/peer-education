import tkinter
import threading
import time


def update_counter(canvas, count_element):
    for x in range(1, 100):
        canvas.itemconfig(count_element, text=str(x))
        canvas.update()
        time.sleep(1)


canvas = tkinter.Canvas(width=1000, height=500)
canvas.pack()

count_element = canvas.create_text(
    1000 / 2,
    500 / 2,
    text="0",
    font=("Arial", 24),
    fill="black",
)

threading.Thread(target=update_counter, args=(canvas, count_element)).start()

canvas.mainloop()
