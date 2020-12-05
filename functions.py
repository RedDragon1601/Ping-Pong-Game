import turtle
from player import*

# Functions

# Player 1 Move
def player_1_up():
	y = player_1.ycor()
	y += 20
	player_1.sety(y)

def player_1_down():
	y = player_1.ycor()
	y -= 20
	player_1.sety(y)

#Player 2 Move
def player_2_up():
	y = player_2.ycor()
	y += 20
	player_2.sety(y)

def player_2_down():
	y = player_2.ycor()
	y -= 20
	player_2.sety(y)