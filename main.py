import pygame
from config import *
from scenes.menu import Menu
from entities.player import Player
from entities.ghost import Ghost
from core.game import Game

global WIDTH, HEIGHT


def run_game():
    # Inicializa
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pac-Man Retrô")
    clock = pygame.time.Clock()
    pygame.mixer.music.load("assets/game_music.mp3")
    pygame.mixer.music.play(-1)

    # Carrega imagens
    pacman_img = pygame.image.load("assets/pacman.png").convert_alpha()
    ghost_img = pygame.image.load("assets/ghost.png").convert_alpha()
    wall_img = pygame.image.load("assets/wall.png").convert_alpha()
    dot_img = pygame.image.load("assets/dot.png").convert_alpha()

    # Sons
    pygame.mixer.music.set_volume(0.1)
    eat_sound = pygame.mixer.Sound("assets/eat.wav")
    death_sound = pygame.mixer.Sound("assets/death.wav")

    images = {
        "pacman": pacman_img,
        "ghost": ghost_img,
        "wall": wall_img,
        "dot": dot_img
    }

    # Entidades
    player = Player(1, 1, pacman_img)
    ghosts = [
        Ghost(9, 3, ghost_img),
        Ghost(9, 5, ghost_img)
    ]

    # Jogo
    game = Game(screen, player, ghosts, images)

    # Loop principal
    running = True
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-1, 0, game.level)
        elif keys[pygame.K_RIGHT]:
            player.move(1, 0, game.level)
        elif keys[pygame.K_UP]:
            player.move(0, -1, game.level)
        elif keys[pygame.K_DOWN]:
            player.move(0, 1, game.level)

        game.update()
        game.draw_level()
        player.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)
        game.draw_ui()

        pygame.display.flip()

    pygame.quit()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Projeto Pac-Man")
    pygame.mixer.music.load("assets/menu_music.mp3")
    pygame.mixer.music.play(-1)  # Loop infinito
    clock = pygame.time.Clock()

    # Tela de menu
    menu = Menu(screen)
    in_menu = True
    running = True

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
                    pass  # Você pode implementar tela de score aqui
                elif result == "SAIR":
                    in_menu = False
                    running = False

        pygame.display.flip()
        clock.tick(FPS)

    if running:
        run_game()

    pygame.quit()
    pygame.mixer.music.stop()


if __name__ == "__main__":
    main()
