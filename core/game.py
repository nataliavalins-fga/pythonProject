import pygame
from config import *
from copy import deepcopy
from core.level import get_level_data, check_victory


class Game:
    def __init__(self, screen, player, ghosts, images, level_number=1):
        self.screen = screen
        self.player = player
        self.ghosts = ghosts
        self.images = images
        self.font = pygame.font.SysFont("Arial", 24)
        self.level = deepcopy(get_level_data(level_number))  # ✅ cópia segura
        self.level_number = level_number
        self.game_over = False
        self.victory = False

    def draw_level(self):
        for y, row in enumerate(self.level):
            for x, tile in enumerate(row):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if tile == 1:
                    self.screen.blit(self.images['wall'], rect)
                elif tile == 2:
                    self.screen.blit(self.images['dot'], rect)

    def update(self):
        if not self.game_over and not self.victory:
            for ghost in self.ghosts:
                ghost.move(self.level)
                if ghost.check_collision(self.player):
                    self.game_over = True
                    pygame.mixer.Sound("assets/death.wav").play()

            if check_victory(self.level):
                self.victory = True

    def draw_ui(self):
        if self.game_over:
            self._draw_text("GAME OVER", RED)
        elif self.victory:
            self._draw_text("VOCÊ VENCEU!", YELLOW)
        else:
            score_text = self.font.render(f"Pontos: {self.player.score}", True, WHITE)
            self.screen.blit(score_text, (10, HEIGHT - 30))

        # Exibe número da fase
        level_text = self.font.render(f"Fase {self.level_number}", True, WHITE)
        self.screen.blit(level_text, (WIDTH - 120, 10))

    def _draw_text(self, text, color):
        text_surface = self.font.render(text, True, color)
        rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text_surface, rect)

    def is_game_over(self):
        return self.game_over

    def is_level_completed(self):
        return self.victory
