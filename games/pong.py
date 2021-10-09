# Step 0 - Imports
import turtle

score = 0
execFlag = True
windowWidth = 800
windowHeight = 600
ballWidth = 20
ballHeight = ballWidth

paddleHeight = 100  # 5*20
paddleWidth = 20  # 1*20

turtleSize = 10
windowMaxX = windowWidth / 2 - turtleSize  # 390
windowMaxY = windowHeight / 2 - turtleSize  # 270
windowExcludingPaddleMaxX = windowMaxX - paddleWidth  # 390-20 = 370

paddleSpeed = 50
ballVerticalSpeed = 0.1  # X
ballHorizontalSpeed = 0.1  # Y

#  Step 1 - Turtle Screen/Window (Object Creation)
wn = turtle.Screen()
wn.title('Pong Game')
wn.bgcolor('black')
wn.setup(width=windowWidth, height=windowHeight)
wn.tracer(0)

# Step 2 - Left Paddle (Object Creation)
leftPaddle = turtle.Turtle()
leftPaddle.speed(0)
leftPaddle.shape('square')
leftPaddle.color('#ADFFFE')
leftPaddle.shapesize(stretch_wid=paddleHeight / 20, stretch_len=paddleWidth / 20)
leftPaddle.penup()
leftPaddle.goto(-windowMaxX, 0)

# Step 3 - Right Paddle (Object Creation)
rightPaddle = turtle.Turtle()
rightPaddle.speed(0)
rightPaddle.shape('square')
rightPaddle.color('#FFD2BA')
rightPaddle.shapesize(stretch_wid=paddleHeight / 20, stretch_len=paddleWidth / 20)
rightPaddle.penup()
rightPaddle.goto(windowMaxX - turtleSize, 0)

# Step 4 - Ball (Object Creation)
ball = turtle.Turtle()
ball.speed(40)
ball.shape('circle')
ball.shapesize(stretch_wid=ballWidth / 20, stretch_len=ballHeight / 20)
ball.color('#FFFC9E')
ball.penup()
# original position 0, 0
ball.home()

# ball.goto(0, 0)

# Making variables for the scores

left_player = 0
right_player = 0


# Functions
# Step 5 - Paddle movement - Change y coordinate position
def left_paddle_up():
    leftPaddle.sety(leftPaddle.ycor() + paddleSpeed)


def left_paddle_down():
    leftPaddle.sety(leftPaddle.ycor() - paddleSpeed)


def right_paddle_up():
    rightPaddle.sety(rightPaddle.ycor() + paddleSpeed)


def right_paddle_down():
    rightPaddle.sety(rightPaddle.ycor() - paddleSpeed)


def exit_program():
    global execFlag
    execFlag = False
    print("Received exit signal")


# Making the score board

# scoreBoard = turtle.Turtle()
# scoreBoard.speed(0)
# scoreBoard.color('#CCFFAD')
# scoreBoard.goto(0, 280)
# scoreBoard.penup()
# scoreBoard.hideturtle()
# scoreBoard.write('Left Player Points:    Nil'
#                 'Right Player Points:    Nil')

# Keyboard Binding
# Step 6 - Add key listener
wn.listen()
wn.onkeypress(exit_program, "x")

wn.onkeypress(left_paddle_up, "w")
wn.onkeypress(left_paddle_down, "s")
wn.onkeypress(right_paddle_up, "Up")
wn.onkeypress(right_paddle_down, "Down")

print("windowMaxX=" + str(windowMaxX) + ",windowMaxY=" + str(windowMaxY) + ",windowExcludingPaddleMaxX=" + str(
    windowExcludingPaddleMaxX))

# Step 7 - Main Game Loop (Infinite)
while True:
    if execFlag == False:
        print("Exit the program")
        break
    # Main Step 1 - Perform a TurtleScreen update
    wn.update()

    # Main Step 2 - Moving the Ball
    # current position + ballSpeed
    xPos = ball.xcor() + ballHorizontalSpeed
    yPos = ball.ycor() + ballVerticalSpeed
    ball.setx(xPos)
    ball.sety(yPos)
    print(str(xPos) + "+" + str(ballHorizontalSpeed) + "," + str(yPos) + "+" + str(ballVerticalSpeed))

    # Border Checking
    if -windowMaxY >= yPos or yPos >= windowMaxY:
        print("Y => Vertical boundary touched")
        # ball.sety(windowMaxY)
        ballVerticalSpeed *= -1
    if -windowMaxX >= xPos or xPos >= windowMaxX and xPos > 0:
        print("X => Horizontal boundary touched")
        # ball.setx(windowMaxX)
        # left_player += 1
        ballHorizontalSpeed *= -1
    #   scoreBoard.clear()
    #   scoreBoard.write('Left Player Points:    {}'
    #                    'Right Player Points:    {}'.format(left_player, right_player), align=)

    # Paddle Ball Collisions

# if (ball.xcor() > windowMaxX and ball.xcor() < windowExcludingPaddleMaxX) and (
#         ball.ycor() < rightPaddle.ycor() + 40 and ball.ycor() > rightPaddle.ycor() - 40):
#     ball.setx(360)
#     ballHorizontalSpeed *= -1
#
#     if (ball.xcor() < -windowMaxX and ball.xcor() > -windowExcludingPaddleMaxX) and (
#             ball.ycor() < leftPaddle.ycor() + 40 and ball.ycor() > leftPaddle.ycor() - 40):
#         ball.setx(-360)
#         ballHorizontalSpeed *= -1

# if -windowExcludingPaddleMaxX > yPos > windowExcludingPaddleMaxX:
#    if (rightPaddle.ycor() + paddleWidth >= ball.ycor() > rightPaddle.ycor() - paddleWidth):
#        ballXSpeed += -1
#        ballYSpeed += 0.2
# if -windowExcludingPaddleMaxX > xPos > windowExcludingPaddleMaxX:
#    if (leftPaddle.ycor() + paddleWidth > ball.ycor() > leftPaddle.ycor() - paddleWidth):
#        ballXSpeed += -1
#        ballYSpeed += 0.2
