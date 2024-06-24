import pygame
import random
import time
from constants import *
from pathfinding import a_star
from walls import walls

# 食物类
class Food:
    def __init__(self, x, y):
        self.x = x  # 食物的x坐标
        self.y = y  # 食物的y坐标

    def draw(self, dis):
        pygame.draw.rect(dis, red, [self.x, self.y, food_size, food_size])

# 加速豆类
class SpeedBoost:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, dis):
        # 在指定显示对象上绘制食物
        pygame.draw.rect(dis, green, [self.x, self.y, food_size, food_size])

# 怪物类
class Monster:
    def __init__(self, x, y, speed):
        self.x = x  # 怪物的x坐标
        self.y = y  # 怪物的y坐标
        self.speed = speed  # 怪物的速度
        self.path = []  # 怪物的路径
        self.path_update_interval = 0.2  # 路径更新间隔（秒），会影响怪物追踪吃豆人的效率
        self.last_path_update = time.time()  # 上次路径更新的时间，用于计时，到时即刷新路径
        self.target_index = 0  # 当前路径目标索引

    def move_towards_player(self, player_x, player_y, walls):
        """
        怪物向玩家移动
        :param player_x: 玩家x坐标
        :param player_y: 玩家y坐标
        :param walls: 墙体列表
        """

        current_time = time.time()

        # 如果距离上次更新路径的时间超过设定间隔，或者路径为空，则更新路径
        if current_time - self.last_path_update > self.path_update_interval or not self.path:
            start = (self.x // wall_thickness * wall_thickness, self.y // wall_thickness * wall_thickness)
            end = (player_x // wall_thickness * wall_thickness, player_y // wall_thickness * wall_thickness)
            self.path = a_star(start, end, walls, wall_thickness)
            self.last_path_update = current_time
            self.target_index = 0

        # 如果路径存在并且路径目标索引未超出路径长度
        if self.path and self.target_index < len(self.path):
            next_step = self.path[self.target_index]
            dx, dy = next_step[0] - self.x, next_step[1] - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance < self.speed:
                # 如果距离小于速度，则直接移动到下一个位置
                self.x, self.y = next_step
                self.target_index += 1
            else:
                # 否则按比例移动
                self.x += self.speed * dx / distance
                self.y += self.speed * dy / distance

            # 确保位置为整数
            self.x, self.y = int(self.x), int(self.y)

    # 在指定显示对象上绘制怪物
    def draw(self, dis):
        pygame.draw.rect(dis, blue, [self.x, self.y, monster_size, monster_size])


# 生成有效随机位置的函数
def generate_valid_position(size):
    """
    生成有效的随机位置
    :param size: 物体大小
    :return: 随机生成的位置
    """

    while True:
        # random.randint(a, b) 函数生成一个在 a 和 b 之间的随机整数（包括 a 和 b）
        # 这里的 x 和 y 是物体左上角的坐标，范围是从 0 到 dis_width - size 和 0 到 dis_height - size，确保物体完全在屏幕内
        x = random.randint(0, dis_width - size)
        y = random.randint(0, dis_height - size)

        # pygame.Rect(x, y, width, height) 创建一个矩形对象，表示物体在屏幕上的位置和大小
        rect = pygame.Rect(x, y, size, size)
        collision = False

        # 遍历所有墙体 walls 列表
        # rect.colliderect(wall) 检查当前生成的矩形 rect 是否与墙体 wall 发生碰撞
        # 如果发生碰撞，将 collision 标志设置为 True 并退出循环
        for wall in walls:
            if rect.colliderect(wall):
                collision = True
                break

        # 如果没有检测到碰撞 (collision 仍为 False)，则返回当前随机生成的 x 和 y 坐标。
        # 否则，循环继续，重新生成新的随机位置并进行碰撞检测，直到找到一个不与任何墙体碰撞的位置为止
        if not collision:
            return x, y
