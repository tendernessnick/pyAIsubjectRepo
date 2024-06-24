import pygame
import pygame_menu
from constants import *  # 导入所有常量

def show_about_screen():
    pygame.init()
    dis = pygame.display.set_mode((dis_width, dis_height))  # 设置显示模式（屏幕尺寸）
    pygame.display.set_caption('About Pac-Man')  # 设置窗口标题

    # 创建关于界面的菜单对象，设置菜单标题和尺寸，使用黑暗主题
    about_menu = pygame_menu.Menu('About', dis_width, dis_height, theme=pygame_menu.themes.THEME_DARK)

    # 描述游戏玩法的文本
    about_text = (
        "Pac-Man\n"
        "Author: Tenderness\n"
        "This game is a simple implementation of the classic Pac-Man game.\n"
        "Use the arrow keys to move Pac-Man and eat the food.\n"
        "Avoid the monsters or the game will be over.\n"
        "Green boosts increase your speed temporarily.\n"
        "Enjoy the game!"
    )

    # 向关于菜单添加标签，显示关于信息
    about_menu.add.label(about_text, max_char=40, font_size=20)

    def go_back():
        import menu  # 延迟导入menu模块，避免循环依赖
        menu.main_menu()  # 返回主菜单

    # 向关于菜单添加返回按钮，调用go_back函数
    about_menu.add.button('Back', go_back)

    # ----------无限循环，保持关于界面显示，当用户用鼠标点击back和enter就可以退出界面----------
    while True:
        dis.fill(black)  # 用黑色填充屏幕背景
        events = pygame.event.get()  # 获取所有事件
        for event in events:
            if event.type == pygame.QUIT:  # 如果接收到退出事件
                pygame.quit()  # 退出pygame
                exit()  # 退出程序

        about_menu.update(events)  # 更新关于菜单
        about_menu.draw(dis)  # 绘制关于菜单
        pygame.display.flip()   # 刷新显示
