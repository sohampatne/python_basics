import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class Cube(object):
    rows = 20
    w = 500

    def __init__(this, dirnx, dirny, start_position, color=(255, 255, 0)):
        print('inside cube init')
        this.pos = start_position
        this.dirnx = dirnx
        this.dirny = dirny
        this.color = color

    def move(self, x_change, y_change):
        print('inside cube move')
        self.dirnx = x_change
        self.dirny = y_change
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        print('inside cube draw')
        dis = self.w // self.rows  # 25
        x = self.pos[0]  # X Position
        y = self.pos[1]  # Y Position

        pygame.draw.rect(surface, self.color, pygame.Rect(
            x * dis + 1, y * dis + 1, dis-2, dis-2))  # 26, 1, 23, 23 # x, y, width, height

        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (x * dis + centre - radius, y * dis + 8)
            circleMiddle2 = (x * dis + dis - radius * 2, y * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)
#


def main():
    # Step 1 - Initializing Pygame
    pygame.init()

    global width, rows, s, snack, canvas
    width, height = 500, 500
    rows = 20

    # Initializing surface
    canvas = pygame.display.set_mode((width, height))

    # Initialing Color
    snack_color = (255, 0, 0)

    snack = Cube(1, 0, (1, 0), snack_color)

    counter = 0
    while counter <= 5000:
        snack.draw(canvas, True)
        snack.move(1, 0)
        snack.draw(canvas)
        pygame.display.flip()
        counter += 1


main()
