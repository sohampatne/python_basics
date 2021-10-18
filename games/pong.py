# Step 0 - Imports
import turtle
import winsound

# Step 0.1 - Variables

exitFlag = False
screenWidth = 800
screenHeight = 600
paddleWidth = 20  # 1*20
paddleHeight = 100  # 5*20
halfScreen = screenWidth / 2 - paddleWidth / 2
screenMaxHeight = screenHeight / 2 - 10
ballCircum = 20
ballXSpeed = 0.275
ballYSpeed = 0.275
paddleSpeed = 50
leftPlayerScore = 0
rightPlayerScore = 0

# Step 1 - Object Creation

# Step 1.1 - Screen creation
window = turtle.Screen()
window.setup(width=screenWidth, height=screenHeight)
window.bgcolor('black')
window.tracer(0)
window.title('Pong Game')

# Step 1.2 - Paddle Creation

# Step 1.2.1 - Left Paddle Creation
leftPaddle = turtle.Turtle()
leftPaddle.penup()
leftPaddle.shape('square')
leftPaddle.color('#ADFFF9')
leftPaddle.speed(0)
leftPaddle.shapesize(stretch_len=paddleWidth / 20, stretch_wid=paddleHeight / 20)
leftPaddle.goto(-halfScreen, 0)

# Step 1.2.2 - Right Paddle Creation
rightPaddle = turtle.Turtle()
rightPaddle.penup()
rightPaddle.shape('square')
rightPaddle.color('#FFADAD')
rightPaddle.speed(0)
rightPaddle.shapesize(stretch_len=paddleWidth / 20, stretch_wid=paddleHeight / 20)
rightPaddle.goto(halfScreen - 10, 0)

# Step 1.3 - Ball Creation
ball = turtle.Turtle()
ball.penup()
ball.shape('circle')
ball.color('#FEFF90')
ball.home()
ball.shapesize(stretch_len=ballCircum / 20, stretch_wid=ballCircum / 20)
ball.speed(0)


# Step 3 - Functions

def left_paddle_up():
    leftPaddle.sety(leftPaddle.ycor() + paddleSpeed)


def left_paddle_down():
    leftPaddle.sety(leftPaddle.ycor() - paddleSpeed)


def right_paddle_up():
    rightPaddle.sety(rightPaddle.ycor() + paddleSpeed)


def right_paddle_down():
    rightPaddle.sety(rightPaddle.ycor() - paddleSpeed)


def exit_program():
    global exitFlag
    exitFlag = True
    print('Exiting Program... \n Exited Program \n Thanks for Playing!')


def play_sound():
    winsound.PlaySound('bounce_ball.wav', winsound.SND_ASYNC)


def play_oops_sound():
    winsound.PlaySound('oops.wav', winsound.SND_ASYNC)


# Step 3.1 - Listen

window.listen()
window.onkeypress(left_paddle_up, 'w')
window.onkeypress(left_paddle_down, 's')
window.onkeypress(right_paddle_up, 'Up')
window.onkeypress(right_paddle_down, 'Down')
window.onkeypress(exit_program, 'x')

# Last and Main step - Main loop

ballYCor = ball.ycor()
ballXcor = ball.xcor()

while not exitFlag:
    # Step 4 - Collisions
    # Step 4.1 - Ball Y cor collisions
    if ballYCor >= screenMaxHeight or ballYCor <= -screenMaxHeight + 8:
        ballYSpeed *= -1
        print('Y axis wall touched')
        # play_sound()

    if ballXcor >= halfScreen - 18:
        ballXSpeed *= -1
        leftPlayerScore += 1
        print('Right Player\'s wall touched!')
        print('Left Player Scored!')
        print('| Right Player | Left Player |' +
              f'\n|       {rightPlayerScore}      |      {leftPlayerScore}      |')
        play_oops_sound()

    if ballXcor <= -halfScreen:
        ballXSpeed *= -1
        rightPlayerScore += 1
        print('Left Player\'s wall touched!')
        print('Right Player Scored!')
        print('| Right Player | Left Player |' +
              f'\n|       {rightPlayerScore}      |      {leftPlayerScore}      |')
        play_oops_sound()

    if leftPlayerScore == 5 or rightPlayerScore == 5:
        if leftPlayerScore > rightPlayerScore:
            print(f'The Left Player Wins by {leftPlayerScore - rightPlayerScore} point(s)')
        else:
            print(f'The Right Player Wins by {rightPlayerScore - leftPlayerScore} point(s)')
        break

    # Step 4.2 - Paddle and Ball Collisions
    elif ballXcor >= rightPaddle.xcor() - 20 and \
            (rightPaddle.ycor() + paddleHeight / 2 >= ballYCor >= rightPaddle.ycor() - paddleHeight / 2):
        ballXSpeed *= -1
        play_sound()
    elif ballXcor <= leftPaddle.xcor() + 20 and \
            (leftPaddle.ycor() + paddleHeight / 2 >= ballYCor >= leftPaddle.ycor() - paddleHeight / 2):
        ballXSpeed *= -1
        play_sound()

    ballYCor = ball.ycor() + ballYSpeed
    ballXcor = ball.xcor() + ballXSpeed
    ball.sety(ballYCor)
    ball.setx(ballXcor)
    # IMPORTANT UPDATE FUNCTION
    window.update()
    # print(ball.ycor())
