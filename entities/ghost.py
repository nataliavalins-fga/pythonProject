import pygame
import random
from config import TILE_SIZE


class Ghost:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

    def draw(self, screen):
        screen.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))

    def move(self, level):
        dx, dy = self.direction
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < len(level[0]) and 0 <= new_y < len(level) and level[new_y][new_x] != 1:
            self.x = new_x
            self.y = new_y
        else:
            self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

    def check_collision(self, player):
        return self.x == player.x and self.y == player.y
