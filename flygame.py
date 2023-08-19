import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 游戏窗口大小
window_width = 800
window_height = 600

# 设置窗口大小
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("飞机射击游戏")

# 颜色定义
white = (255, 255, 255)
red = (255, 0, 0)

# 飞机属性
player_speed = 5
player_width = 50
player_height = 50
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height - 10

# 子弹属性
bullet_speed = 10
bullet_width = 5
bullet_height = 15
bullet_color = red
bullets = []

# 敌人属性
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemies = []

# 得分
score = 0

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_width - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        bullet_x = player_x + player_width // 2 - bullet_width // 2
        bullet_y = player_y
        bullets.append([bullet_x, bullet_y])

    # 移动子弹
    for bullet in bullets:
        bullet[1] -= bullet_speed

    # 移除超出屏幕的子弹
    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    # 生成敌人
    if len(enemies) < 5 and random.randint(1, 100) < 10:
        enemy_x = random.randint(0, window_width - enemy_width)
        enemy_y = 0
        enemies.append([enemy_x, enemy_y])

    # 移动敌人
    for enemy in enemies:
        enemy[1] += enemy_speed

    # 移除超出屏幕的敌人
    enemies = [enemy for enemy in enemies if enemy[1] < window_height]

    # 检测子弹与敌人的碰撞
    for bullet in bullets:
        for enemy in enemies:
            if (
                    bullet[0] < enemy[0] + enemy_width
                    and bullet[0] + bullet_width > enemy[0]
                    and bullet[1] < enemy[1] + enemy_height
                    and bullet[1] + bullet_height > enemy[1]
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    # 渲染屏幕
    screen.fill(white)

    # 画飞机
    pygame.draw.rect(screen, red, (player_x, player_y, player_width, player_height))

    # 画子弹
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, (bullet[0], bullet[1], bullet_width, bullet_height))

    # 画敌人
    for enemy in enemies:
        pygame.draw.rect(screen, red, (enemy[0], enemy[1], enemy_width, enemy_height))

    # 显示得分
    font = pygame.font.Font(None, 36)
    text = font.render(f"得分: {score}", True, red)
    screen.blit(text, (10, 10))

    pygame.display.update()

    # 控制帧速率
    pygame.time.delay(30)
