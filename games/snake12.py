# Precondition - Installing Pygame
# pip install pygame

# Step 1 - Imports
import pygame

# Variables
width, height = 700, 600
square_width = 15

# colors
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (225, 225, 0)
black = (0, 0, 0)

# game status
game_over = False

# snake coordinates
x1 = height/2
x1_change = 0
y1 = height/2
y1_change = 0

# clock
clock = pygame.time.Clock()

# Step 2 - Create the Screen
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.update()
pygame.display.set_caption('Snake Game by SohVin')

while not game_over:
    for event in pygame.event.get():
        # print(event) - prints out ALL the actions that take place on the screen

        # exitable program code
        if event.type == pygame.QUIT:
            game_over = True

        # key press input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
            elif event.key == pygame.K_UP:
                y1_change == -10
            elif event.key == pygame.K_DOWN:
                y1_change == 10

    # snake position change
    x1 += x1_change
    y1 += y1_change
    screen.fill(black)

    # snake creation
    pygame.draw.rect(screen, yellow, ((width / 2),
                     (height / 2), square_width, square_width))
    # screen updating
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()
# Step 3 - Create the Snake
# Step 4 - Moving the Snake
# Step 5 - Game Over when Snake hits the boundaries
# Step 6 - Adding the Food
# Step 7 - Increasing the Length of the Snake
# Step 8 - Displaying the Score
