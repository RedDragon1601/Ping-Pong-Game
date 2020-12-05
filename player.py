import turtle

# Player 1
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("red")
player_1.shapesize(3, 1)
player_1.penup()
player_1.goto(-350, 0)

# Player 2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("blue")
player_2.shapesize(3, 1)
player_2.penup()
player_2.goto(350, 0)