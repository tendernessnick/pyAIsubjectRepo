import pygame
import random
import time
from constants import *
from pathfinding import a_star
from walls import walls

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, dis):
        pygame.draw.rect(dis, red, [self.x, self.y, food_size, food_size])

class SpeedBoost:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, dis):
        pygame.draw.rect(dis, green, [self.x, self.y, food_size, food_size])

class Monster:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.path = []
        self.path_update_interval = 0.2  # 路径更新间隔（秒）
        self.last_path_update = time.time()
        self.target_index = 0  # 当前路径目标索引

    def move_towards_player(self, player_x, player_y, walls):
        current_time = time.time()
        if current_time - self.last_path_update > self.path_update_interval or not self.path:
            start = (self.x // wall_thickness * wall_thickness, self.y // wall_thickness * wall_thickness)
            end = (player_x // wall_thickness * wall_thickness, player_y // wall_thickness * wall_thickness)
            self.path = a_star(start, end, walls, wall_thickness)
            self.last_path_update = current_time
            self.target_index = 0

        if self.path and self.target_index < len(self.path):
            next_step = self.path[self.target_index]
            dx, dy = next_step[0] - self.x, next_step[1] - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance < self.speed:
                self.x, self.y = next_step
                self.target_index += 1
            else:
                self.x += self.speed * dx / distance
                self.y += self.speed * dy / distance

            # 确保位置为整数
            self.x, self.y = int(self.x), int(self.y)

    def draw(self, dis):
        pygame.draw.rect(dis, blue, [self.x, self.y, monster_size, monster_size])

def generate_valid_position(size):
    while True:
        x = random.randint(0, dis_width - size)
        y = random.randint(0, dis_height - size)
        rect = pygame.Rect(x, y, size, size)
        collision = False
        for wall in walls:
            if rect.colliderect(wall):
                collision = True
                break
        if not collision:
            return x, y
