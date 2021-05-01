"""
import turtle as t

def pyLOL():
    
    t.setheading(0)
    t.forward(100)

t.listen()
t.onkeypress(pyLOL,"Right")
"""
"""
import turtle as t
def pynojammineshake():
    t.fillcolor("black")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
t.listen()
t.onkeypress(pynojammineshake,"c")
"""
"""
import turtle as t
def j():
    t.setheading(90)
    t.forward(10)
def d():
    t.setheading(180)
    t.forward(10)
def b():
    t.setheading(270)
    t.forward(10)
def c():
    t.setheading(0)
    t.forward(10)

t.listen()
t.onkeypress(j,"Up")
t.onkeypress(d,"Left")
t.onkeypress(b,"Down")
t.onkeypress(c,"Right")
"""
"""
import turtle as t
def mouse():
    t.forward(10)

t.listen
t.onscreenclick(t.goto)
"""
"""
import turtle as t
def lol():
    for a in range(1,37,1):
        t.forward(300)
        t.left(160)
        t.forward(300)
        t.left(150)
        
        
t.speed(10)
t.listen()
t.onkeypress(lol,"s")
"""
import turtle as t


def sideLine():
    t.speed(100)
    for i in range(1,5,1):
        t.forward(400)
        t.right(90)
        
def horizon():
    for i in range(1,21,1):
        t.speed(100)    
        
        t.forward(400)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(400)
        t.left(90)
        t.forward(10)
        t.left(90)

def vertical():
    for i in range(1,21,1):
        t.speed(100)
        t.forward(10)
        t.left(90)
        t.forward(400)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(400)
        t.left(90)
def r():
    t.color("red")
    t.pendown()
    t.stamp()
    t.penup()
def b():
    t.color("blue")
    t.pendown()
    t.stamp()
    t.penup()
    
t.speed(100)
sideLine()
horizon()
vertical()
t.onscreenclick(t.goto)
t.onkeypress(r,"r")
t.onkeypress(b,"b")
t.penup()
