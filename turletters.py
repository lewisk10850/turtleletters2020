import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
        tur.pu()
        tur.fd(12)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        tur.fd(40)
        tur.left(90)
        tur.circle(10,180)
        tur.left(180)
        tur.circle(10,180)
        tur.pu()
        tur.left(180)
        tur.fd(28)
        tur.left(90)
        tur.fd(10)
        tur.right(90)
    elif letter == "C":
        tur.pu()
        tur.fd(25)
        tur.right(90)
        tur.fd(10)
        tur.right(90)
        tur.pd()
        tur.circle(21,200)
        tur.pu()
        tur.fd(9)
        tur.left(70)
        tur.fd(48)
        tur.right(90)

    elif letter == "D":
        tur.pu()
        tur.fd(15)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        tur.fd(40)
        tur.left(90)
        tur.circle(18,235)
        tur.pu()
        tur.right(150)
        tur.fd(25)
        tur.right(90)
        tur.fd(39)

    elif letter == "E":
        tur.pu()
        tur.fd(15)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        tur.fd(40)
        tur.left(90)
        tur.fd(20)
        tur.backward(20)
        tur.right(270)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.backward(20)
        tur.right(270)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.pu()
        tur.fd(5)
        tur.left(90)
        tur.fd(10)
        tur.right(90)
    elif letter == "F":
        tur.pu()
        tur.fd(15)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        tur.fd(40)
        tur.left(180)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.backward(20)
        tur.left(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.pu()
        tur.fd(5)
        tur.left(90)
        tur.fd(10)
        tur.right(90)
    elif letter == "G":
        tur.setheading(0)
        tur.fd(40)
        tur.bk(40)
        tur.right(90)
        tur.fd(60)
        tur.left(90)
        tur.fd(40)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(25)
        tur.pu()
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(25)
        tur.fd(20)		
    elif letter == "H":
        tur.pd()
        tur.setheading(0)
        tur.right(90)
        tur.fd(60)
        tur.bk(30)
        tur.left(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(30)
        tur.bk(60)
        tur.pu()
        tur.left(90)
        tur.fd(20)
    elif letter == "I":
        tur.pd()
        tur.setheading(0)
        tur.fd(40)
        tur.bk(20)
        tur.right(90)
        tur.fd(60)
        tur.right(90)
        tur.fd(20)
        tur.bk(40)
        tur.pu()
        tur.right(90)
        tur.fd(60)
        tur.right(90)
        tur.fd(20)
    elif letter == "J":
        tur.pd()
        tur.setheading(0)
        tur.pu()
        tur.fd(40)
        tur.pd()
        tur.right(90)
        tur.fd(40)
        tur.right(45)
        tur.fd(10)
        tur.right(45)
        tur.fd(20)
        tur.right(45)
        tur.fd(10)
        tur.pu()
        tur.right(45)
        tur.fd(40)
        tur.right(90)
        tur.fd(35)
        tur.fd(20)
    elif letter == "K":
        tur.setheading(0)
        tur.right(90)
        tur.fd(60)
        tur.bk(30)
        tur.left(45)
        tur.fd(45)
        tur.bk(45)
        tur.left(90)
        tur.fd(45)
        tur.pu()
        tur.right(45)
        tur.fd(20)
        tur.pu()
    elif letter == "L":
        tur.penup()
        tur.forward(5)
        tur.pendown()
        tur.right(90)
        tur.forward(60)
        tur.left(90)
        tur.forward(40)
        tur.penup()
        tur.left(90)
        tur.forward(60)
        tur.right(90)
        tur.penup()
    elif letter == "M":
        tur.penup()
        tur.forward(5)
        tur.pendown()
        tur.right(90)
        tur.forward(60)
        tur.right(180)
        tur.forward(60)
        tur.right(90)
        tur.forward(20)
        tur.right(90)
        tur.forward(20)
        tur.right(180)
        tur.forward(20)
        tur.right(90)
        tur.forward(20)
        tur.right(90)
        tur.forward(60)
        tur.right(180)
        tur.forward(60)
        tur.right(90)
    elif letter == "N":
        tur.penup()
        tur.forward(5)
        tur.pendown()
        tur.right(90)
        tur.forward(60)
        tur.right(180)
        tur.forward(60)
        tur.right(145)
        tur.forward(72)
        tur.left(145)
        tur.forward(60)
        tur.right(90)
    elif letter == "O":
        tur.penup()
        tur.forward(5)
        tur.pendown()
        tur.right(90)
        tur.forward(60)
        tur.left(90)
        tur.forward(40)
        tur.left(90)
        tur.forward(60)
        tur.left(90)
        tur.forward(40)
        tur.right(180)
        tur.forward(40)
    elif letter == "P":
        tur.penup()
        tur.forward(5)
        tur.pendown()
        tur.right(90)
        tur.forward(60)
        tur.right(180)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(30)
        tur.right(90)
        tur.forward(40)
        tur.right(180)
        tur.forward(40)
        tur.left(90)
        tur.forward(30)
        tur.right(90)	
    elif letter == "Q":
        tur.penup()
        tur.forward(10)
        tur.right(90)	
        tur.forward(25)
        tur.pendown()
        tur.circle(10, 490)
        tur.right(70)
        tur.forward(5)
        tur.right(180)
        tur.forward(15)
        #letter completed and returned to position
        tur.penup()
        tur.right(60)
        tur.forward(28)
        tur.right(90)
        tur.forward(22)
    elif letter == "R":
        tur.penup()
        tur.forward(13)
        tur.right(90)
        tur.forward(10)
        tur.pendown()
        tur.forward(40)
        tur.right(180)
        tur.forward(20)
        tur.right(90)
        tur.circle(10,180)
        tur.left(90)
        tur.forward(20)
        tur.left(45)
        tur.forward(30)
        #letter completed and returned to position
        tur.penup()
        tur.left(45)
        tur.forward(6)
        tur.left(90)
        tur.forward(51)
        tur.right(90)
    elif letter == "S":
        tur.pu()
        tur.fd(28)
        tur.right(90)
        tur.fd(5)
        tur.right(90)
        tur.pd()
        tur.fd(20)
        tur.left(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(25)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.pu()
        tur.right(90)
        tur.fd(45)
        tur.right(90)
        tur.fd(37)
    elif letter == "T":
        tur.penup()
        tur.forward(13)
        tur.right(90)
        tur.forward(15)
        tur.left(90)
        tur.pendown()
        tur.forward(14)
        tur.right(180)
        tur.forward(7)
        tur.left(90)
        tur.forward(30)
        #letter completed and returned to position
        tur.penup()
        tur.left(90)
        tur.forward(20)
        tur.left(90)
        tur.forward(45)
        tur.right(90)
    elif letter == "U":
        tur.penup()
        tur.forward(10)
        tur.right(90)
        tur.forward(10)
        tur.pendown()
        tur.forward(20)
        tur.circle(10,180)
        tur.forward(21)
        #letter completed and returned to position
        tur.penup()
        tur.forward(9)
        tur.right(90)
        tur.forward(10)
    elif letter == "V":
       turtle.penup()
        turtle.forward(9)
        turtle.right(90)
        turtle.forward(10)
        turtle.pendown()
        turtle.right(60)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()
    elif letter == "W":
       turtle.forward(50)
        turtle.left(120)
        turtle.forward(25)
        turtle.right(120)
        turtle.forward(25)
        turtle.left(120)
        turtle.forward(50)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()
    elif letter == "X":
        turtle.right(60)
        turtle.forward(50)
        turtle.penup()
        turtle.left(150)
        turtle.forward(45)
        turtle.left(150)
        turtle.pendown()
        turtle.forward(55)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()
    elif letter == "Y":
        turtle.right(60)
        turtle.forward(50)
        turtle.right(30)
        turtle.forward(50)
        turtle.penup()
        turtle.backward(50)
        turtle.left(30)
        turtle.pendown()
        turtle.left(120)
        turtle.forward(50)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()
    elif letter == "Z":
        turtle.forward(50)
        turtle.right(130)
        turtle.forward(77)
        turtle.left(130)
        turtle.forward(53)		
		
        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)


    window.exitonclick()
