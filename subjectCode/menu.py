import pygame
import pygame_menu
from constants import dis_width, dis_height
from about import show_about_screen
from main import gameLoop

def start_game():
    gameLoop()

def show_about():
    show_about_screen()

def exit_game():
    pygame.quit()
    quit()

def main_menu():
    pygame.init()
    dis = pygame.display.set_mode((dis_width, dis_height))  # 初始化显示模式
    pygame.display.set_caption('Pac-Man 2D')
    menu = pygame_menu.Menu('Pac-Man 2D', dis_width, dis_height, theme=pygame_menu.themes.THEME_DARK)

    menu.add.button('Play', start_game)
    menu.add.button('About', show_about)
    menu.add.button('Quit', exit_game)
    menu.mainloop(dis)

# hot-fix 添加了一个注释
# hot-fix 又添加了一个注释
if __name__ == "__main__":
    main_menu()

