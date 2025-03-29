# scenes/menu.py

import pygame
from config import WIDTH, HEIGHT, WHITE, YELLOW

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 28, bold=True)
        self.options = ["INICIAR JOGO", "PONTUAÇÃO", "SAIR"]
        self.selected = 0
        self.bg = pygame.image.load("assets/menu_bg.png").convert()

    def draw(self):
        self.screen.blit(pygame.transform.scale(self.bg, (WIDTH, HEIGHT)), (0, 0))

        title_font = pygame.font.SysFont("Arial", 48, bold=True)
        title = title_font.render("PAC-MAN RETRÔ", True, (255, 150, 0))
        title_rect = title.get_rect(center=(WIDTH//2, 100))
        self.screen.blit(title, title_rect)

        for i, option in enumerate(self.options):
            color = YELLOW if i == self.selected else WHITE
            text = self.font.render(option, True, color)
            rect = text.get_rect(center=(WIDTH // 2, 200 + i * 50))
            self.screen.blit(text, rect)

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected]
        return None
