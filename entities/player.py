import pygame
from config import TILE_SIZE


class Player:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.score = 0
        self.direction = None  # ← armazenar a última direção

    def move(self, dx, dy, level):
        new_x = self.x + dx
        new_y = self.y + dy

        if level[new_y][new_x] != 1:  # se não for parede
            # Comer ponto se houver
            if level[new_y][new_x] == 2:
                self.score += 10
                level[new_y][new_x] = 0
            self.x = new_x
            self.y = new_y

    def draw(self, screen):
        rect = pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        screen.blit(self.image, rect)

