import pygame
import time
import random

from constants import *
from walls import walls
from entities import Food, SpeedBoost, Monster, generate_valid_position

dis = pygame.display.set_mode((dis_width, dis_height))

def message(msg, color, dis):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def go_to_main_menu():
    from menu import main_menu
    main_menu()

def gameLoop():
    game_over = False
    score = 0
    player_x = 390
    player_y = 280
    player_speed = initial_player_speed
    player_speed_boosted = False
    player_speed_timer = 0

    foods = [Food(*generate_valid_position(food_size)) for _ in range(food_count)]
    speed_boosts = []
    monsters = [Monster(*generate_valid_position(monster_size), random.randint(3, max_monster_speed))]

    last_monster_time = time.time()
    last_speed_boost_time = time.time()
    monster_interval = 10  # 每10秒生成一个怪物
    speed_boost_interval = 15  # 每15秒生成一个加速豆

    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        old_x, old_y = player_x, player_y

        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # 检查与墙的碰撞
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        for wall in walls:
            if player_rect.colliderect(wall):
                player_x, player_y = old_x, old_y

        # 限制玩家在屏幕范围内
        if player_x < 0:
            player_x = 0
        if player_x > dis_width - player_size:
            player_x = dis_width - player_size
        if player_y < 0:
            player_y = 0
        if player_y > dis_height - player_size:
            player_y = dis_height - player_size

        dis.fill(black)
        pygame.draw.rect(dis, yellow, [player_x, player_y, player_size, player_size])

        for wall in walls:
            pygame.draw.rect(dis, wall_color, wall)

        for food in foods[:]:
            food.draw(dis)
            if player_x < food.x + food_size and player_x + player_size > food.x:
                if player_y < food.y + food_size and player_y + player_size > food.y:
                    foods.remove(food)
                    score += 1
                    foods.append(Food(*generate_valid_position(food_size)))

        for speed_boost in speed_boosts[:]:
            speed_boost.draw(dis)
            if player_x < speed_boost.x + food_size and player_x + player_size > speed_boost.x:
                if player_y < speed_boost.y + food_size and player_y + player_size > speed_boost.y:
                    speed_boosts.remove(speed_boost)
                    player_speed += speed_boost_amount
                    player_speed_boosted = True
                    player_speed_timer = time.time()

        if player_speed_boosted and time.time() - player_speed_timer > speed_boost_duration:
            player_speed -= speed_boost_amount
            player_speed_boosted = False

        for monster in monsters:
            monster.move_towards_player(player_x, player_y, walls)
            monster.draw(dis)
            if player_x < monster.x + monster_size and player_x + player_size > monster.x:
                if player_y < monster.y + monster_size and player_y + player_size > monster.y:
                    game_over = True

        # 检查是否需要生成新的怪物
        if time.time() - last_monster_time > monster_interval:
            last_monster_time = time.time()
            monsters.append(Monster(*generate_valid_position(monster_size), random.randint(3, max_monster_speed)))

        # 检查是否需要生成新的加速豆
        if time.time() - last_speed_boost_time > speed_boost_interval:
            last_speed_boost_time = time.time()
            speed_boosts.append(SpeedBoost(*generate_valid_position(food_size)))

        pygame.display.update()
        clock.tick(30)

    dis.fill(black)
    message(f"Game Over! Score: {score}", white, dis)
    pygame.display.update()
    pygame.time.wait(2000)
    go_to_main_menu()

    # 这里是对master 分支同步的测试


