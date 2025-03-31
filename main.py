import pygame
from config import *
from scenes.menu import Menu
from entities.player import Player
from entities.ghost import Ghost
from core.game import Game
from core.score import save_score


def run_game(level_number=1):
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pac-Man Retrô")
    clock = pygame.time.Clock()

    pygame.mixer.music.load("assets/game_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    pacman_img = pygame.image.load("assets/pacman.png").convert_alpha()
    ghost_img = pygame.image.load("assets/ghost.png").convert_alpha()
    wall_img = pygame.image.load("assets/wall.png").convert_alpha()
    dot_img = pygame.image.load("assets/dot.png").convert_alpha()

    images = {
        "pacman": pacman_img,
        "ghost": ghost_img,
        "wall": wall_img,
        "dot": dot_img
    }

    eat_sound = pygame.mixer.Sound("assets/eat.wav")
    death_sound = pygame.mixer.Sound("assets/death.wav")

    if level_number == 2:
        player = Player(1, 1, pacman_img)
        ghosts = [Ghost(5, 5, ghost_img), Ghost(7, 3, ghost_img)]
    else:
        player = Player(1, 1, pacman_img)
        ghosts = [Ghost(9, 3, ghost_img), Ghost(9, 5, ghost_img)]

    game = Game(screen, player, ghosts, images, level_number)

    start_ticks = pygame.time.get_ticks()
    LEVEL_TIME_LIMIT = 60

    while True:
        clock.tick(FPS)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit", player.score
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move(-1, 0, game.level)
                elif event.key == pygame.K_RIGHT:
                    player.move(1, 0, game.level)
                elif event.key == pygame.K_UP:
                    player.move(0, -1, game.level)
                elif event.key == pygame.K_DOWN:
                    player.move(0, 1, game.level)

        game.update()
        game.draw_level()
        player.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)
        game.draw_ui()

        pygame.display.flip()

        if game.is_game_over():
            pygame.time.wait(2000)
            pygame.mixer.music.stop()
            return "game_over", player.score

        if game.is_level_completed():
            pygame.time.wait(2000)
            pygame.mixer.music.stop()
            return "next_level", player.score

        elapsed = (pygame.time.get_ticks() - start_ticks) // 1000
        if elapsed >= LEVEL_TIME_LIMIT:
            pygame.time.wait(2000)
            pygame.mixer.music.stop()
            return "game_over", player.score


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Projeto Pac-Man")
    pygame.mixer.music.load("assets/menu_music.mp3")
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    running = True

    while running:
        menu = Menu(screen)
        in_menu = True
        while in_menu:
            screen.fill(BLACK)
            menu.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_menu = False
                    running = False
                else:
                    result = menu.update(event)
                    if result == "INICIAR JOGO":
                        in_menu = False
                    elif result == "PONTUAÇÃO":
                        viewing_scores = True
                        while viewing_scores:
                            screen.fill(BLACK)
                            menu.draw_scores()
                            for e in pygame.event.get():
                                if e.type == pygame.QUIT:
                                    viewing_scores = False
                                    running = False
                                elif e.type == pygame.KEYDOWN or e.type == pygame.MOUSEBUTTONDOWN:
                                    viewing_scores = False
                            pygame.display.flip()
                    elif result == "SAIR":
                        in_menu = False
                        running = False
            pygame.display.flip()
            clock.tick(FPS)

        if running:
            total_score = 0
            current_level = 1

            while True:
                # 🎯 Tela de transição de fase
                font = pygame.font.SysFont("Arial", 40, bold=True)
                text = font.render(f"Fase {current_level}", True, WHITE)
                screen.fill(BLACK)
                screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
                pygame.display.flip()
                pygame.time.wait(2000)

                result, score = run_game(level_number=current_level)
                total_score += score

                if result == "next_level":
                    current_level += 1
                elif result in ["game_over", "menu", "quit"]:
                    save_score(total_score)
                    pygame.mixer.music.load("assets/menu_music.mp3")
                    pygame.mixer.music.play(-1)
                    if result == "quit":
                        running = False
                    break

    pygame.quit()
    pygame.mixer.music.stop()


if __name__ == "__main__":
    main()


