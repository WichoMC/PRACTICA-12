import turtle
import argparse

def recorrido_recursivo(tortuga, espacio, huellas):
    if huellas > 0:
        tortuga.stamp()
        espacio = espacio + 3
        tortuga.forward(espacio)
        tortuga.right(24)
        recorrido_recursivo(tortuga, espacio, huellas-1)



'''
ap = argparse.ArgumentParser()
ap.add_argument("--huella", required = True, help="numero de huellas")
args = vars(ap.parse_args())
huellas = int(args["huella"])
'''

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tortuga")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()
recorrido_recursivo(tess, 20,30)
wn.mainloop()
