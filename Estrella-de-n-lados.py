import turtle
a=int(input("Ingrese el número de puntas de la estrella(impar):  "))

t=turtle.Pen()
t.speed(1)
for x in range(0,a):
	t.forward(120)
	t.left(360/a*2)
turtle.getscreen()._root.mainloop()

