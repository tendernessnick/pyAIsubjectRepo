import pygame
import pygame_menu
from constants import dis_width, dis_height  # 导入屏幕宽度和高度常量
from about import show_about_screen  # 导入显示关于界面的函数
from main import gameLoop  # 导入游戏主循环

def start_game():
    gameLoop()

def show_about():
    show_about_screen()

def exit_game():
    pygame.quit()  # 退出pygame
    quit()  # 退出程序

def main_menu():
    pygame.init()  # 初始化pygame
    dis = pygame.display.set_mode((dis_width, dis_height))  # 初始化显示模式
    pygame.display.set_caption('Pac-man')  # 设置窗口标题

    # 创建菜单对象，设置菜单标题和尺寸，使用黑暗主题
    menu = pygame_menu.Menu('Pac-man', dis_width, dis_height, theme=pygame_menu.themes.THEME_DARK)

    # 向菜单添加按钮
    menu.add.button('Play', start_game)  # "Play"按钮调用start_game函数
    menu.add.button('About', show_about)  # "About"按钮调用show_about函数
    menu.add.button('Quit', exit_game)  # "Quit"按钮调用exit_game函数
    menu.mainloop(dis)  # 显示菜单，传入显示对象

# 如果直接运行该文件，则显示主菜单
if __name__ == "__main__":
    main_menu()

