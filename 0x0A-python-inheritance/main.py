import turtle

# Create a turtle instance
pen = turtle.Turtle()

# Set the speed of drawing
pen.speed(3)

# Draw Tom
pen.color("gray")
pen.pensize(3)

# Draw Tom's body
pen.penup()
pen.goto(-50, -50)
pen.pendown()
pen.circle(50)

# Draw Tom's face
pen.penup()
pen.goto(-20, 20)
pen.pendown()
pen.circle(20)

# Draw Tom's ears
pen.penup()
pen.goto(-50, 70)
pen.pendown()
pen.setheading(60)
pen.circle(-30, 120)
pen.setheading(-60)
pen.circle(30, 120)

# Draw Tom's eyes
pen.penup()
pen.goto(-10, 40)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
pen.circle(5)
pen.end_fill()

pen.penup()
pen.goto(-30, 40)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
pen.circle(5)
pen.end_fill()

# Draw Jerry
pen.color("brown")

# Draw Jerry's body
pen.penup()
pen.goto(70, -50)
pen.pendown()
pen.circle(40)

# Draw Jerry's face
pen.penup()
pen.goto(90, 20)
pen.pendown()
pen.circle(20)

# Draw Jerry's ears
pen.penup()
pen.goto(70, 60)
pen.pendown()
pen.setheading(60)
pen.circle(-20, 120)
pen.setheading(-60)
pen.circle(20, 120)

# Draw Jerry's eyes
pen.penup()
pen.goto(90, 40)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
pen.circle(5)
pen.end_fill()

pen.penup()
pen.goto(110, 40)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
pen.circle(5)
pen.end_fill()

# Hide the turtle
pen.hideturtle()

# Keep the turtle window open
turtle.done()
