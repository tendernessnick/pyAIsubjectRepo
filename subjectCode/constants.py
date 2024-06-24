import pygame

# 这个文件定义了游戏中用到的各种常量，包括颜色、屏幕尺寸、玩家和怪物的大小和速度、食物和道具的大小和数量、墙的颜色和厚度、加速道具的持续时间和增加的速度量，以及字体样式

# 初始化pygame
pygame.init()

# 定义一些常量
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)

# 定义屏幕宽度和高度
dis_width = 800
dis_height = 600

# 定义玩家大小和速度
player_size = 20
initial_player_speed = 5  # 初始吃豆人的速度

# 定义食物大小和速度
food_size = 20
food_count = 10

# 定义怪物大小和速度
monster_size = 20
max_monster_speed = initial_player_speed + 1

# 定义墙体颜色和厚度
wall_color = white
wall_thickness = 10

# 定义加速道具的持续时间和速度增加量
speed_boost_duration = 10
speed_boost_amount = 2

# 定义字体样式
font_style = pygame.font.SysFont(None, 50)
