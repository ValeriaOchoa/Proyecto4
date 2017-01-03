##movimiento de imagen
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
my_image = PhotoImage(file="15824564_1115709555208363_840438098_o.gif")
canvas.create_image(0,0,anchor=NW, image=my_image)

def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -2)
        canvas.move(2, 0, -4)
        canvas.move(3, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 2)
        canvas.move(2, 0, 3)
        canvas.move(3, 0, 5)
    elif event.keysym == 'Left':
        canvas.move(1, -2, 0)
        canvas.move(2, -4, 0)
        canvas.move(3, -5, 0)
    else:
        canvas.move(1, 2, 0)
        canvas.move(2, 4, 0)
        canvas.move(3, 5, 0)

canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
tk.mainloop()
