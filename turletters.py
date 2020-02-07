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
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
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
	    pass
    elif letter == "R":
	    pass
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
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
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
