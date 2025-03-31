# scenes/menu.py

import pygame
from config import WIDTH, HEIGHT, WHITE, YELLOW, BLACK
from core.score import get_top_scores


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
        title_rect = title.get_rect(center=(WIDTH // 2, 100))
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

    def draw_scores(self):
        self.screen.blit(pygame.transform.scale(self.bg, (WIDTH, HEIGHT)), (0, 0))

        title_font = pygame.font.SysFont("Arial", 42, bold=True)
        title = title_font.render("PONTUAÇÕES", True, WHITE)
        self.screen.blit(title, title.get_rect(center=(WIDTH // 2, 80)))

        scores = get_top_scores(5)

        if not scores:
            msg = self.font.render("Nenhuma pontuação registrada.", True, WHITE)
            self.screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        else:
            for i, score in enumerate(scores):
                score_text = self.font.render(f"{i + 1}. {score} pontos", True, WHITE)
                self.screen.blit(score_text, (WIDTH // 2 - 80, 150 + i * 40))

        hint = pygame.font.SysFont("Arial", 20).render("Pressione qualquer tecla para voltar", True, WHITE)
        self.screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT - 40)))
