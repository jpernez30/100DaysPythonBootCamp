import turtle

# Set up the screen
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # Turns off the screen updates

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(400)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -230)
ball.dx = 0.15
ball.dy = 0.15

# Bricks
bricks = []

colors = ["red", "blue", "green", "yellow"]
for i in range(-350, 400, 100):
    for j in range(200, 300, 40):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(colors[(i // 100 + j // 40) % len(colors)])
        brick.penup()
        brick.goto(i, j)
        bricks.append(brick)

# Score
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(260, -300)
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Paddle movement
def paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 350:
        x = 350
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -350:
        x = -350
    paddle.setx(x)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_right, "Right")
win.onkeypress(paddle_left, "Left")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, -230)
        ball.dy *= -1

    # Paddle and ball collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1

    # Ball and brick collision
    for brick in bricks:
        if (ball.ycor() > brick.ycor() - 20 and ball.ycor() < brick.ycor() + 20) and (ball.xcor() > brick.xcor() - 50 and ball.xcor() < brick.xcor() + 50):
            ball.dy *= -1
            brick.hideturtle()
            bricks.remove(brick)
            score += 10
            score_display.clear()
            score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    # Check for win condition
    if not bricks:
        score_display.clear()
        score_display.write("You Win!", align="center", font=("Courier", 36, "normal"))
        break

win.mainloop()
