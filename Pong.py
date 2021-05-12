import turtle
from playsound import playsound

# Draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen_x_limit = 390
screen_y_limit = 290

# Draw paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=1, stretch_len=5)
paddle_1.left(90)
paddle_1.penup()
paddle_1.goto(-350, 0)

# Draw paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Draw ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# Score
score_1 = 0
score_2 = 0

# Head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


# Paddle 1 movement set
def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        paddle_1.fd(30)
    else:
        paddle_1.sety(250)
    if (paddle_1.ycor() + 50 == ball.ycor()) and (paddle_1.xcor() == ball.xcor()):
        ball.dx *= -1


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        paddle_1.back(30)
    else:
        paddle_1.sety(-250)
    if paddle_1.ycor() - 50 == ball.ycor() and (paddle_1.xcor() == ball.xcor()):
        ball.dx *= -1


# Paddle movement set
def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_2.sety(y)


# Keyboard
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")


while True:
    screen.update()
    flag = 0

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Collision with the upper wall
    if ball.ycor() > 290:
        playsound("C:\\Users\\amosf\\Downloads\\pong_bounce.wav")
        ball.sety(290)
        ball.dy *= -1

    # Collision with lower wall
    elif ball.ycor() < -290:
        playsound("C:\\Users\\amosf\\Downloads\\pong_bounce.wav")
        ball.sety(-290)
        ball.dy *= -1

    # Collision with left and right wall
    if ball.xcor() < -390:
        flag = 1
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
    elif ball.xcor() > 390:
        flag = 1
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))

    # Point sound and restart ball
    if flag:
        playsound("C:\\Users\\amosf\\Downloads\\pong_258020__kodack__arcade-bleep-sound.wav")
        ball.goto(0, 0)
        ball.dx *= -1

    # Collision with the paddle 1
    if(ball.xcor() == -330) and (paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50):
        ball.dx *= -1
        playsound("C:\\Users\\amosf\\Downloads\\pong_bounce.wav")

    # collision with the paddle 2
    elif (ball.xcor() == 330) and (paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50):
        ball.dx *= -1
        playsound("C:\\Users\\amosf\\Downloads\\pong_bounce.wav")
