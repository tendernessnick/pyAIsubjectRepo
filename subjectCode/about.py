import pygame
import pygame_menu
from constants import *


def show_about_screen():
    pygame.init()
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('About Pac-Man 2D')
    about_menu = pygame_menu.Menu('About Pac-Man 2D', dis_width, dis_height, theme=pygame_menu.themes.THEME_DARK)

    about_text = (
        "Pac-Man 2D Game\n"
        "Author: Your Name\n"
        "This game is a simple implementation of the classic Pac-Man game.\n"
        "Use the arrow keys to move Pac-Man and collect the food.\n"
        "Avoid the monsters or the game will be over.\n"
        "Green boosts increase your speed temporarily.\n"
        "Enjoy the game!"
    )

    about_menu.add.label(about_text, max_char=40, font_size=20)

    def go_back():
        import menu
        menu.main_menu()

    about_menu.add.button('Back', go_back)

    while True:
        dis.fill(black)  # Fill screen with black color
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        about_menu.update(events)
        about_menu.draw(dis)
        pygame.display.flip()
