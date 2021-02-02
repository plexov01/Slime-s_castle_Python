import pygame
from pygame import *
from pygame import *
import pyganim
AnPortalDelay=0.1
AnPortal = ['animation/portal/portal1.bmp',
            'animation/portal/portal2.bmp',
            'animation/portal/portal3.bmp',
            'animation/portal/portal4.bmp',
            'animation/portal/portal5.bmp',
            'animation/portal/portal6.bmp',
            'animation/portal/portal7.bmp',
            'animation/portal/portal8.bmp',
            'animation/portal/portal9.bmp',
            'animation/portal/portal10.bmp',
            'animation/portal/portal11.bmp',
            'animation/portal/portal12.bmp',
            'animation/portal/portal13.bmp',
            'animation/portal/portal14.bmp',
            'animation/portal/portal15.bmp',
            'animation/portal/portal16.bmp',
            'animation/portal/portal17.bmp',
            'animation/portal/portal18.bmp',
            'animation/portal/portal19.bmp',
            'animation/portal/portal20.bmp',
            'animation/portal/portal21.bmp',
            'animation/portal/portal22.bmp',
            'animation/portal/portal23.bmp',
            'animation/portal/portal24.bmp',
            'animation/portal/portal25.bmp']
AnExplotionDelay=0.1
AnExpl = ['animation/explotion/expl1.png',
          'animation/explotion/expl2.png',
          'animation/explotion/expl3.png',
          'animation/explotion/expl4.png',
          'animation/explotion/expl5.png',
          'animation/explotion/expl6.png',
          'animation/explotion/expl7.png']

          


class Portal(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.X=x
        self.Y=y
        self.image = Surface((192,192)) #image.load('animation/portal/portal17.bmp')#
        # self.image = Surface((image.load('animation/portal/portal1.png').get_width(),image.load('animation/portal/portal1.png').get_height()))
        self.image.fill(Color(255,255,255))
        self.image.set_colorkey(Color("#FFFFFF"))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

        def MakeFrameAnim(animWay, delay):
            FrameAnim = []
            for anim in animWay:
                FrameAnim.append((anim, delay))
            ReadyAnim = pyganim.PygAnimation(FrameAnim)
            return ReadyAnim
        
        # self.PAPortal=MakeFrameAnim(AnPortal,AnPortalDelay)
        # self.PAPortal.play()

        self.PAPortal=MakeFrameAnim(AnPortal,AnPortalDelay)
        self.PAPortal.play()
    def update(self):
        # self.image.fill((0, 0, 0))
        # self.PAPortal.blit(self.image, (0, 0))
        self.image.fill(Color("#FFFFFF"))
        self.PAPortal.blit(self.image, (0, 0))


class Mushroom(sprite.Sprite):
    def __init__(self, x, y, path='image/mushroom2.png'):
        sprite.Sprite.__init__(self)
        self.image = image.load(path).convert_alpha()
        self.image.set_colorkey(Color("#000000"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# class BrownSprouted(sprite.Sprite):
#     def __init__(self, x, y, path='image/BrownSprouted.png'):
#         sprite.Sprite.__init__(self)
#         self.image = image.load(path).convert_alpha()
#         self.image.set_colorkey(Color("#FFFFFF"))
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y


# class Explotion(sprite.Sprite):
#     def __init__(self, x, y):
#         sprite.Sprite.__init__(self)
#         self.image = Surface((256, 256))
#         # self.image = Surface((image.load('animation/portal/portal1.png').get_width(),image.load('animation/portal/portal1.png').get_height()))
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y

#         def MakeFrameAnim(animWay, delay):
#             FrameAnim = []
#             for anim in animWay:
#                 FrameAnim.append((anim, delay))
#             ReadyAnim = pyganim.PygAnimation(FrameAnim)
#             return ReadyAnim
#         self.PAExpl=MakeFrameAnim(AnExpl,AnExplotionDelay)
#         self.PAExpl.play()

#         self.image.fill((25,25,255))
#         self.PAExpl.blit(self.image,(0,0))

# Анимация огня
FIRE_WIDTH = image.load('animation/fireplace/fireplace1.png').get_width()
FIRE_HEIGHT = image.load('animation/fireplace/fireplace1.png').get_height()
FIRE_COLOR = "#888888"
ANIMATION_FIRE = [
    ('animation/fireplace/fireplace1.png'),
    ('animation/fireplace/fireplace2.png'),
    ('animation/fireplace/fireplace3.png'),
    ('animation/fireplace/fireplace4.png'),
    ('animation/fireplace/fireplace5.png'),
    ('animation/fireplace/fireplace6.png')
]


class Fire(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((FIRE_WIDTH, FIRE_HEIGHT))
        self.image.fill(Color(FIRE_COLOR))
        self.rect = Rect(x+(50-FIRE_WIDTH)//2, y, FIRE_WIDTH, FIRE_HEIGHT)
        self.image.set_colorkey(Color(FIRE_COLOR))
        self.startX = x  # начальные координаты
        self.startY = y
        fireAnim = []
        for anim in ANIMATION_FIRE:
            fireAnim.append((anim, 0.1))
        self.fireAnim = pyganim.PygAnimation(fireAnim)
        self.fireAnim.play()

    def update(self):
        self.image.fill(Color(FIRE_COLOR))
        self.fireAnim.blit(self.image, (0, 0))
    
