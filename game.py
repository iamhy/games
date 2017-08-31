# 1 - 导入pygame库，这一步能让你使用库里提供的功能
import pygame
from pygame.locals import *
import math
import random

# 2 - 初始化pygame，设置展示窗口
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [100, 100]

acc = [0, 0]
arrows = []

badtimer = 100
badtimer1 = 0
badguys = [[640, 100]]
healthvalue = 194

#3 - 加载作为兔子的图片
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg = badguyimg1

#4 -不停地循环执行接下来的部分

while True:
    badtimer -= 1
    #5 - 在给屏幕画任何东西之前用黑色进行填充
    screen.fill(0)
    # 6 - 在屏幕的（100，100）坐标出添加你加载的兔子图片
    for x in range(int(width / grass.get_width() + 1)):
        for y in range(int(height / grass.get_height() + 1)):
            screen.blit(grass, (x * 100, y * 100))
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))
    # 6.1 - 设置玩家的位置和鼠标位置
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (playerpos[1] + 32),
                       position[0] - (playerpos[0] + 26))
    playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)
    playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2,
                  playerpos[1] - playerrot.get_rect().height / 2)
    screen.blit(playerrot, playerpos1)

    #6.2 - 绘制箭头
    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
            print(index)
            arrows.pop(index)
        index += 1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(
                arrow, 360 - projectile[0] * 57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    # 6.3 绘制坏蛋
    if badtimer == 0:
        badguys.append([640, random.randint(50, 430)])
        badtimer = 100 - (badtimer1 * 2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5
    index = 0
    for badguy in badguys:
        if badguy[0] < -64:
            badguys.pop(index)
        badguy[0] -= 7
        #6.3.1 - 
        badrect = pygame.Rect(badguyimg.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        index += 1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)

    #7 - 更新屏幕
    pygame.display.flip()
    # 8 - 检查一些新的事件，如果有退出命令，则终止程序的执行。
    for event in pygame.event.get():
        # 检查是否有点关闭按钮
        if event.type == QUIT:
            pygame.quit()
            exit(0)

        if event.type == KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True

        if event.type == KEYUP:
            if event.key == K_w:
                keys[0] = False
            elif event.key == K_a:
                keys[1] = False
            elif event.key == K_s:
                keys[2] = False
            elif event.key == K_d:
                keys[3] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append([math.atan2(position[1] - (playerpos1[1] + 32), position[0] -
                                      (playerpos1[0] + 26)), playerpos1[0] + 32, playerpos1[1] + 32])

    #9 - 移动玩家
    if keys[0]:
        playerpos[1] -= 5
    if keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    if keys[3]:
        playerpos[0] += 5
