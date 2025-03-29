import pygame
from config import TILE_SIZE


class Player:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.score = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))

    def move(self, dx, dy, level):
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < len(level[0]) and 0 <= new_y < len(level):
            if level[new_y][new_x] != 1:
                self.x = new_x
                self.y = new_y

            if level[self.y][self.x] == 2:
                level[self.y][self.x] = 0
                self.score += 10
                pygame.mixer.Sound("assets/eat.wav").play()
