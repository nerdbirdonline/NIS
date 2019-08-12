import time
import random
import math
import turtle
import os
turtle.setundobuffer(1)
turtle.tracer(1)

print("What colour would you like to be?")
playerchoice = input()

# set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("NerdBird In Space")
wn.bgpic("spacebg.gif")


# border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# set the score to 0
score = 0

# draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" % score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# create player turtle
player = turtle.Turtle()
player.color(playerchoice)
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 20

# choose a nnumber of enimies
number_of_enemies = 5
# create an empty list of enimies
enemies = []

# add enimies to the list
for i in range(number_of_enemies):
    # create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 4

# create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 50

# define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"

# Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    # declare bulletstate as a global if its needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # move bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) +
                         math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 23:
        return True
    else:
        return False


# create keyword binding
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.listen()
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(fire_bullet, "space")

# main game loop
while True:

    for enemy in enemies:
        # move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # move the enemy back and down
        if enemy.xcor() > 280:
            # move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                # move all enemies down
                y = e.ycor()
                y -= 40
                e.sety(y)
            # change enemy direction
            enemyspeed *= -1

        # check for a collision between bullet and the enemy
        if isCollision(bullet, enemy):
            # reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # update score
            score += 10
            scorestring = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left",
                            font=("Arial", 14, "normal"))

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # check to see if bullet has reached the top
    if bullet.ycor() > 275:
        bulletstate = "ready"
        bullet.hideturtle()


delay = input("Press Enter to finish")
