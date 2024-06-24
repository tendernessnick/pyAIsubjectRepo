import pygame
import time
import random

from constants import *  # 导入常量
from walls import walls  # 导入墙体信息
from entities import Food, SpeedBoost, Monster, generate_valid_position  # 导入实体对象和生成位置的函数

# 设置显示窗口的尺寸
dis = pygame.display.set_mode((dis_width, dis_height))

def message(msg, color, dis):
    """
    在屏幕上显示信息
    :param msg: 信息内容
    :param color: 信息颜色
    :param dis: 显示对象
    """
    mesg = font_style.render(msg, True, color)  # 渲染消息
    dis.blit(mesg, [dis_width / 6, dis_height / 3])  # 将消息显示在屏幕上

def go_to_main_menu():
    """
    返回主菜单
    """
    from menu import main_menu  # 延迟导入，避免循环依赖
    main_menu()

def gameLoop():
    """
    游戏主循环
    """
    game_over = False  # 游戏结束标志
    score = 0  # 初始分数
    player_x, player_y = 390, 280  # 玩家初始位置
    player_speed = initial_player_speed  # 玩家初始速度
    player_speed_boosted = False  # 玩家是否加速标志
    player_speed_timer = 0  # 加速计时器

    foods = [Food(*generate_valid_position(food_size)) for _ in range(food_count)]  # 初始化食物
    speed_boosts = []  # 初始化加速道具
    # teleports = []  # 瞬移道具列表，预留位置
    monsters = [Monster(*generate_valid_position(monster_size), random.randint(3, max_monster_speed))]  # 初始怪物

    last_monster_time = time.time()  # 记录上次生成怪物的时间
    last_speed_boost_time = time.time()  # 记录上次生成加速道具的时间
    monster_interval = 10  # 每10秒生成一个怪物
    speed_boost_interval = 15  # 每15秒生成一个加速道具
    # teleport_interval = 20  # 每20秒生成一个瞬移道具

    clock = pygame.time.Clock()  # 设置游戏时钟

    # 没有碰到怪物时，游戏循环不结束
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 如果接收到退出事件，则结束游戏
                game_over = True

        keys = pygame.key.get_pressed()  # 获取键盘按键状态
        old_x, old_y = player_x, player_y  # 记录玩家旧位置

        # 根据按键移动玩家
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # 检查玩家与墙的碰撞
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        for wall in walls:
            if player_rect.colliderect(wall):
                player_x, player_y = old_x, old_y  # 碰撞后恢复到旧位置

        # 限制玩家在屏幕范围内
        if player_x < 0:
            player_x = 0
        if player_x > dis_width - player_size:
            player_x = dis_width - player_size
        if player_y < 0:
            player_y = 0
        if player_y > dis_height - player_size:
            player_y = dis_height - player_size

        # 填充屏幕背景为黑色
        dis.fill(black)
        pygame.draw.rect(dis, yellow, [player_x, player_y, player_size, player_size])  # 绘制玩家

        # 绘制墙体
        for wall in walls:
            pygame.draw.rect(dis, wall_color, wall)

        # 处理食物的逻辑
        for food in foods[:]:
            food.draw(dis)
            if player_x < food.x + food_size and player_x + player_size > food.x:
                if player_y < food.y + food_size and player_y + player_size > food.y:
                    foods.remove(food)
                    score += 1
                    foods.append(Food(*generate_valid_position(food_size)))  # 重新生成一个食物

        # 处理加速道具的逻辑
        for speed_boost in speed_boosts[:]:
            speed_boost.draw(dis)
            if player_x < speed_boost.x + food_size and player_x + player_size > speed_boost.x:
                if player_y < speed_boost.y + food_size and player_y + player_size > speed_boost.y:
                    speed_boosts.remove(speed_boost)
                    player_speed += speed_boost_amount  # 增加玩家速度
                    player_speed_boosted = True
                    player_speed_timer = time.time()  # 记录加速开始时间

        # 处理瞬移道具的逻辑（预留位置）
        # for teleport in teleports[:]:
        #     teleport.draw(dis)
        #     if player_x < teleport.x + food_size and player_x + player_size > teleport.x:
        #         if player_y < teleport.y + food_size and player_y + player_size > teleport.y:
        #             teleports.remove(teleport)
        #             player_x, player_y = generate_valid_position(player_size)  # 随机生成新位置

        # 检查加速效果是否结束
        if player_speed_boosted and time.time() - player_speed_timer > speed_boost_duration:
            player_speed -= speed_boost_amount
            player_speed_boosted = False

        # 处理怪物的逻辑
        for monster in monsters:
            monster.move_towards_player(player_x, player_y, walls)
            monster.draw(dis)
            if player_x < monster.x + monster_size and player_x + player_size > monster.x:
                if player_y < monster.y + monster_size and player_y + player_size > monster.y:
                    game_over = True  # 玩家被怪物碰到，游戏结束

        # 检查是否需要生成新的怪物
        if time.time() - last_monster_time > monster_interval:
            last_monster_time = time.time()
            monsters.append(Monster(*generate_valid_position(monster_size), random.randint(3, max_monster_speed)))

        # 检查是否需要生成新的加速道具
        if time.time() - last_speed_boost_time > speed_boost_interval:
            last_speed_boost_time = time.time()
            speed_boosts.append(SpeedBoost(*generate_valid_position(food_size)))

        # 检查是否需要生成新的瞬移道具（预留位置）
        # if time.time() - last_teleport_time > teleport_interval:
        #     last_teleport_time = time.time()
        #     teleports.append(Teleport(*generate_valid_position(food_size)))

        pygame.display.update()  # 更新显示，刷新界面，保证游戏正常进行
        clock.tick(30)  # 控制游戏帧率，怪物移动速度

    # 游戏结束后的处理
    dis.fill(black)
    message(f"Game Over! Score: {score}", white, dis)
    pygame.display.update()
    pygame.time.wait(2000)
    go_to_main_menu()

