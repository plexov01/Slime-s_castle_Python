from pygame import *
import pyganim
import os

MONSTER_WIDTH = 64
MONSTER_HEIGHT = 72
MONSTER_COLOR = "#888888"
b = True #В какую сторону движется
ANIMATION_right = [('animation/monster/Right/imgonline-com-ua-Resize-wDrz74ZvER.png'),
                            ('animation/monster/Right/imgonline-com-ua-Resize-QV7YTX0pRNbu7b.png'),
                            ('animation/monster/Right/imgonline-com-ua-Resize-Fdgiu8NI8lRR.png'),
                            ('animation/monster/Right/imgonline-com-ua-Resize-G5HvLJaMo1UfufS7.png')]
ANIMATION_left = [('animation/monster/Left/imgonline-com-ua-Mirror-l5mW2ZOBnQx1tvS.png'),
                ('animation/monster/Left/imgonline-com-ua-Mirror-oGHxGXGV8p3506.png'),
                ('animation/monster/Left/imgonline-com-ua-Mirror-zSZqAMDJAx.png'),
                ('animation/monster/Left/imgonline-com-ua-Mirror-TEfJZrXdnRGuB6GZ.png')]
class Monster(sprite.Sprite):
    def __init__(self, x, y, left, up, maxLengthLeft,maxLengthUp):
        sprite.Sprite.__init__(self)
        self.image = Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image.fill(Color(MONSTER_COLOR))
        self.rect = Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)
        self.image.set_colorkey(Color(MONSTER_COLOR))
        self.startX = x # начальные координаты
        self.startY = y
        self.maxLengthLeft = maxLengthLeft # максимальное расстояние, которое может пройти в одну сторону
        self.maxLengthUp= maxLengthUp # максимальное расстояние, которое может пройти в одну сторону, вертикаль
        self.xvel = left # cкорость передвижения по горизонтали, 0 - стоит на месте
        self.yvel = up # скорость движения по вертикали, 0 - не двигается
        boltAnimRight = []
        boltAnimleft = []
        for anim in ANIMATION_right:
            boltAnimRight.append((anim, 0.2))
        self.boltAnimRight = pyganim.PygAnimation(boltAnimRight)
        self.boltAnimRight.play()
        for anim in ANIMATION_left:
            boltAnimleft.append((anim, 0.2))
        self.boltAnimleft = pyganim.PygAnimation(boltAnimleft)
        self.boltAnimleft.play()
         
    def update(self): # по принципу героя
        self.image.fill(Color(MONSTER_COLOR))
        global b
        if b:
            self.boltAnimRight.blit(self.image, (0, 0))
        else:
            self.boltAnimleft.blit(self.image, (0, 0))
        self.rect.y += self.yvel
        self.rect.x += self.xvel
        if (abs(self.startX - self.rect.x) > self.maxLengthLeft):
            self.xvel =-self.xvel  # если прошли максимальное растояние, то идеи в обратную сторону
            b = not b
        if (abs(self.startY - self.rect.y) > self.maxLengthUp):
            self.yvel = -self.yvel # если прошли максимальное растояние, то идеи в обратную сторону, вертикаль