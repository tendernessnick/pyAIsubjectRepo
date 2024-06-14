import pygame

# 初始化pygame
pygame.init()

# 定义一些常量
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)

dis_width = 800
dis_height = 600

player_size = 20
initial_player_speed = 5  # 初始吃豆人的速度

food_size = 20
food_count = 10

monster_size = 20
max_monster_speed = initial_player_speed + 1

wall_color = white
wall_thickness = 10

speed_boost_duration = 10
speed_boost_amount = 2

font_style = pygame.font.SysFont(None, 50)
