import pygame
import sys

# 初始化Pygame
pygame.init()

# 游戏窗口大小
window_width = 800
window_height = 600

# 设置窗口大小
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("移动小球游戏")

# 小球初始位置和速度
ball_x = window_width // 2
ball_y = window_height // 2
ball_speed_x = 5
ball_speed_y = 5

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 移动小球
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 检查边界碰撞
    if ball_x < 0 or ball_x > window_width:
        ball_speed_x = -ball_speed_x
    if ball_y < 0 or ball_y > window_height:
        ball_speed_y = -ball_speed_y

    # 填充窗口颜色
    screen.fill((0, 0, 0))

    # 画小球
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), 20)

    # 更新窗口显示
    pygame.display.update()

    # 控制帧速率
    pygame.time.delay(60)
