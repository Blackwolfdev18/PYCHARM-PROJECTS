import turtle
yuvi=turtle.Turtle()
yuvi.pensize(5)

#body
yuvi.penup()
yuvi.goto(-70,-70)
yuvi.pendown()
yuvi.fillcolor("yellow")
yuvi.begin_fill()
yuvi.forward(200)
yuvi.left(90)
yuvi.forward(200)
yuvi.left(90)
yuvi.forward(200)
yuvi.left(90)
yuvi.forward(200)

yuvi.end_fill()


#brownpants
yuvi.fillcolor("#8B4513")
yuvi.begin_fill()
yuvi.forward(40)
yuvi.left(90)
yuvi.forward(200)
yuvi.left(90)
yuvi.forward(40)
yuvi.left(90)
yuvi.forward(200)
yuvi.left(90)
yuvi.end_fill()


#shirts
yuvi.fillcolor("white")
yuvi.begin_fill()
yuvi.forward(20)
yuvi.left(90)
yuvi.forward(200)
yuvi.left(90)
yuvi.forward(20)
yuvi.left(90)
yuvi.forward(200)
yuvi.end_fill()

yuvi.penup()



#tie
yuvi.left(90)

yuvi.forward(18)
yuvi.left(90)
yuvi.forward(100)
yuvi.fillcolor("red")
yuvi.begin_fill()
yuvi.pencolor("red")
yuvi.pendown()
yuvi.circle(7)
yuvi.end_fill()


yuvi.penup()

#eye
yuvi.pencolor("black")
yuvi.goto(75,50)
yuvi.pendown()
yuvi.fillcolor("white")
yuvi.begin_fill()
yuvi.circle(25)
yuvi.end_fill()

yuvi.fillcolor("black")
yuvi.penup()
yuvi.goto(80,60)
yuvi.begin_fill()
yuvi.circle(10)
yuvi.end_fill()

#eye2
yuvi.penup()
yuvi.pencolor("black")
yuvi.goto(-15,50)
yuvi.pendown()
yuvi.fillcolor("white")
yuvi.begin_fill()
yuvi.circle(25)
yuvi.end_fill()

yuvi.penup()
yuvi.goto(-10,60)
yuvi.fillcolor("black")
yuvi.begin_fill()
yuvi.circle(10)
yuvi.end_fill()


#smile
yuvi.penup()
yuvi.goto(-10,0)
yuvi.pendown()
yuvi.pensize(5)
yuvi.right(90)
yuvi.fillcolor("red")
yuvi.begin_fill()
yuvi.circle(40,180)
yuvi.left(90)
yuvi.forward(80)
yuvi.end_fill()


#teeths
yuvi.fillcolor("white")
yuvi.begin_fill()
yuvi.left(180)
yuvi.forward(25)
yuvi.right(90)
yuvi.forward(15)
yuvi.left(90)
yuvi.forward(10)
yuvi.left(90)
yuvi.forward(15)
yuvi.end_fill()


yuvi.fillcolor("white")
yuvi.begin_fill()
yuvi.right(90)
yuvi.forward(10)
yuvi.right(90)
yuvi.forward(15)
yuvi.left(90)
yuvi.forward(10)
yuvi.left(90)
yuvi.forward(15)
yuvi.end_fill()




style = ('Courier', 50, 'italic')
yuvi.penup()
yuvi.pensize(5)
yuvi.goto(-300,-300)
yuvi.write("SpongeBob ",font=style)



turtle.done()


