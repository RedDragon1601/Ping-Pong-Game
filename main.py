import turtle
from player import*
from functions import*
import time

sc = turtle.Screen()
sc.title('Ping Pong')
sc.bgcolor('black')

# Score
score_a = 0
score_b = 0

#create game border
border_a = turtle.Turtle()
border_a.speed(0)
border_a.setposition(-390, -250)
border_a.color('red')

for i in range(1):
    border_a.goto(-390, 250)
    border_a.goto(390, 250)
    border_a.goto(390, -250)
    border_a.goto(-390, -250)
    border_a.hideturtle()

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Keyboard bindings
turtle.listen()
turtle.onkey(player_1_up, "w")
turtle.onkey(player_1_down, "s")
turtle.onkey(player_2_up, "Up")
turtle.onkey(player_2_down, "Down")

# Main game loop
while True:
    sc.update()	

	# Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

	# Border checking
    if ball.ycor() > 245:
        ball.sety(245)
        ball.dy *= -1

    if ball.ycor() < -245:
        ball.sety(-245)
        ball.dy *= -1

    if ball.xcor() > 385:
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        time.sleep(1)
        ball.goto(0, 0)

    if ball.xcor() < -385:
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        time.sleep(1)
        ball.goto(0, 0)

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_2.ycor() + 40 and ball.ycor() > player_2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_1.ycor() + 40 and ball.ycor() > player_1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1