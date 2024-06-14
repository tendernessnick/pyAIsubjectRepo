import pygame
from constants import dis_width, dis_height, wall_thickness

walls = [
    # 外围墙体
    pygame.Rect(0, 0, dis_width, wall_thickness),
    pygame.Rect(0, 0, wall_thickness, dis_height),
    pygame.Rect(0, dis_height - wall_thickness, dis_width, wall_thickness),
    pygame.Rect(dis_width - wall_thickness, 0, wall_thickness, dis_height),

    # 内部墙体

    # 中心方框
    pygame.Rect(320, 350, 60, wall_thickness),
    pygame.Rect(430, 350, 60, wall_thickness),
    pygame.Rect(320, 250, 60, wall_thickness),
    pygame.Rect(430, 250, 60, wall_thickness),
    pygame.Rect(320, 260, wall_thickness, 100),
    pygame.Rect(480, 260, wall_thickness, 100),

    # 内圈上T形
    pygame.Rect(320, 110, 170, wall_thickness),
    pygame.Rect(400, 110, wall_thickness, 90),

    # 内圈左右T形
    pygame.Rect(270, 180, 70, wall_thickness),
    pygame.Rect(470, 180, 70, wall_thickness),
    pygame.Rect(260, 110, wall_thickness, 180),
    pygame.Rect(540, 110, wall_thickness, 180),

    # 内圈左右竖杠
    pygame.Rect(260, 350, wall_thickness, 70),
    pygame.Rect(540, 350, wall_thickness, 70),

    # 内圈下T形
    pygame.Rect(320, 410, 170, wall_thickness),
    pygame.Rect(400, 410, wall_thickness, 70),

    # 内圈下横杠
    pygame.Rect(260, 470, 90, wall_thickness),
    pygame.Rect(460, 470, 90, wall_thickness),

    # 外圈上竖杠
    pygame.Rect(400, 0, wall_thickness, 50),

    # 外圈上左右横杠
    # 内
    pygame.Rect(260, 50, 90, wall_thickness),
    pygame.Rect(460, 50, 90, wall_thickness),
    # 外
    pygame.Rect(120, 50, 90, wall_thickness),
    pygame.Rect(600, 50, 90, wall_thickness),

    pygame.Rect(120, 100, 90, wall_thickness),
    pygame.Rect(600, 100, 90, wall_thickness),

    pygame.Rect(120, 140, 90, wall_thickness),
    pygame.Rect(600, 140, 90, wall_thickness),

    pygame.Rect(120, 100, wall_thickness, 50),
    pygame.Rect(600, 100, wall_thickness, 50),
    pygame.Rect(200, 100, wall_thickness, 50),
    pygame.Rect(680, 100, wall_thickness, 50),

    # 外圈下横杠
    pygame.Rect(320, 530, 170, wall_thickness),

    # 外圈左右竖杠
    pygame.Rect(200, 200, wall_thickness, 220),
    pygame.Rect(600, 200, wall_thickness, 220),

    # 外圈左右横杠
    pygame.Rect(70, 310, 80, wall_thickness),
    pygame.Rect(660, 310, 80, wall_thickness),

    # 外外圈左右竖杠
    pygame.Rect(60, 100, wall_thickness, 220),
    pygame.Rect(740, 100, wall_thickness, 220),

    # 外外圈左右下角L形
    pygame.Rect(120, 470, 80, wall_thickness),
    pygame.Rect(600, 470, 80, wall_thickness),

    pygame.Rect(200, 470, wall_thickness, 70),
    pygame.Rect(600, 470, wall_thickness, 70),
]
