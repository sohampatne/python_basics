# Precondition - Installing Pygame
# pip install pygame

# Step 1 - Imports
import pygame

# Variables
width, height = 700, 600
square_width = 15
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (225, 225, 0)
game_over = False

# Step 2 - Create the Screen
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.update()
pygame.display.set_caption('Snake Game by SohVin')

while not game_over:
    for event in pygame.event.get():
        # print(event)   # prints out ALL the actions that take place on the screen
        if event.type == pygame.QUIT:
            game_over = True
    pygame.draw.rect(screen, yellow, ((width / 2), (height / 2), square_width, square_width))
    pygame.display.update()
pygame.quit()
quit()
# Step 3 - Create the Snake
# Step 4 - Moving the Snake
# Step 5 - Game Over when Snake hits the boundaries
# Step 6 - Adding the Food
# Step 7 - Increasing the Length of the Snake
# Step 8 - Displaying the Score
