# Step 0 - Imports
import turtle

# Variables

exFlag = True
windowWidth = 800  # y
windowHeight = 600  # x
paddleWidth = 20  # 20*1
paddleHeight = 100  # 20*5
ballCirCum = 20

halfScreen = windowWidth / 2 - paddleWidth / 2  # 10

# Section 1 - Objects Creation
# Step 1 - Screen
window = turtle.Screen()
window.setup(width=windowWidth, height=windowHeight)
window.title('Pong Game')
window.bgcolor('black')
window.tracer(0)

# Step 2 - Left & Right Paddles
# Step 2.1 Left Paddle
leftPaddle = turtle.Turtle()
leftPaddle.speed(0)
leftPaddle.shape('square')
leftPaddle.color('light blue')
leftPaddle.shapesize(stretch_wid=paddleHeight / 20, stretch_len=paddleWidth / 20)
leftPaddle.penup()
leftPaddle.goto(-halfScreen, 0)

# Step 2.2 Right Paddle
rightPaddle = turtle.Turtle()
rightPaddle.speed(0)
rightPaddle.shape('square')
rightPaddle.color('light blue')
rightPaddle.shapesize(stretch_wid=paddleHeight / 20, stretch_len=paddleWidth / 20)
rightPaddle.penup()
rightPaddle.goto(halfScreen - 10, 0)

# Step 3 - Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.shapesize(stretch_len=ballCirCum / 20, stretch_wid=ballCirCum / 20)
ball.color('yellow')
ball.penup()
ball.home()

# Section 2 - Functions

# Step 4 - Paddle Movement Functions

# Step 5 - Ball Movement Functions

# Step 5.1 - Collision with window screen

# Step 5.2 - Collision with Paddles

# Step 6 - Main Function (Infinite Loop)
window.update()
ball.goto(100, 50)
window.update()

gameTime = 5000 #input('Please enter game time: ')

