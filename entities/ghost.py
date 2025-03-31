import pygame
import random
from config import TILE_SIZE


class Ghost:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.direction = (1, 0)
        self.frame_counter = 0
        self.speed = 10

    def move(self, level):
        self.frame_counter += 1
        if self.frame_counter < self.speed:
            return

        self.frame_counter = 0  # reseta o contador

        new_x = self.x + self.direction[0]
        new_y = self.y + self.direction[1]

        if level[new_y][new_x] != 1:
            self.x = new_x
            self.y = new_y
        else:
            import random
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            random.shuffle(directions)
            for dir in directions:
                dx, dy = dir
                nx, ny = self.x + dx, self.y + dy
                if level[ny][nx] != 1:
                    self.direction = dir
                    break

    def draw(self, screen):
        rect = pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        screen.blit(self.image, rect)

    def check_collision(self, player):
        return self.x == player.x and self.y == player.y
