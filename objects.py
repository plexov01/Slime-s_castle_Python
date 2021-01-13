import pygame
from pygame import *
from pygame import *
import pyganim
# AnPortalDelay=0.1
# AnPortal = ['animation/portal/portal1.png',
#             'animation/portal/portal2.png',
#             'animation/portal/portal3.png',
#             'animation/portal/portal4.png',
#             'animation/portal/portal5.png',
#             'animation/portal/portal6.png',
#             'animation/portal/portal7.png',
#             'animation/portal/portal8.png',
#             'animation/portal/portal9.png',
#             'animation/portal/portal10.png',
#             'animation/portal/portal11.png',
#             'animation/portal/portal12.png',
#             'animation/portal/portal13.png',
#             'animation/portal/portal14.png',
#             'animation/portal/portal15.png',
#             'animation/portal/portal16.png',
#             'animation/portal/portal17.png',
#             'animation/portal/portal18.png',
#             'animation/portal/portal19.png',
#             'animation/portal/portal20.png',
#             'animation/portal/portal21.png',
#             'animation/portal/portal22.png',
#             'animation/portal/portal23.png',
#             'animation/portal/portal24.png',
#             'animation/portal/portal25.png']
# AnExplotionDelay=0.1
# AnExpl = ['animation/explotion/expl1.png',
#           'animation/explotion/expl2.png',
#           'animation/explotion/expl3.png',
#           'animation/explotion/expl4.png',
#           'animation/explotion/expl5.png',
#           'animation/explotion/expl6.png',
#           'animation/explotion/expl7.png']

          


# class Portal(sprite.Sprite):
#     def __init__(self,x,y):
#         sprite.Sprite.__init__(self)
#         self.X=x
#         self.Y=y
#         self.image = Surface((192,192))
#         # self.image = Surface((image.load('animation/portal/portal1.png').get_width(),image.load('animation/portal/portal1.png').get_height()))
#         self.rect=self.image.get_rect()
#         self.rect.x=x
#         self.rect.y=y

#         def MakeFrameAnim(animWay, delay):
#             FrameAnim = []
#             for anim in animWay:
#                 FrameAnim.append((anim, delay))
#             ReadyAnim = pyganim.PygAnimation(FrameAnim)
#             return ReadyAnim
        
#         self.PAPortal=MakeFrameAnim(AnPortal,AnPortalDelay)
#         self.PAPortal.play()

#         # self.PAPortal=MakeFrameAnim(AnPortal,AnPortalDelay)
#         # self.PAPortal.play()

#         self.image.fill((0, 0, 0))
#         self.PAPortal.blit(self.image, (0, 0))


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
    
