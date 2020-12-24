from pygame import *
import pyganim
import os

FIRE_WIDTH = 48
FIRE_HEIGHT = 53
FIRE_COLOR = "#888888"
ANIMATION_FIRE = [('image/imgonline-com-ua-Resize-eC2EZdQ2gC0cKPSG.png'),
                            ('image/imgonline-com-ua-Resize-BUuXTWhth7MxFYnQ.png'),
                            ('image/imgonline-com-ua-Resize-2kgPT3F2rJ.png'),
                            ('image/imgonline-com-ua-Resize-nhbNhE0mbp.png'),
                            ('image/imgonline-com-ua-Resize-9Rf7E7GOOSNFrf.png'),
                            ('image/imgonline-com-ua-Resize-SxEDgLBaPgTtvp.png')]
class Fire(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((FIRE_WIDTH, FIRE_HEIGHT))
        self.image.fill(Color(FIRE_COLOR))
        self.rect = Rect(x, y, FIRE_WIDTH, FIRE_HEIGHT)
        self.image.set_colorkey(Color(FIRE_COLOR))
        self.startX = x # начальные координаты
        self.startY = y
        fireAnim=[]
        for anim in ANIMATION_FIRE:
            fireAnim.append((anim, 0.17))
        self.fireAnim = pyganim.PygAnimation(fireAnim)
        self.fireAnim.play()
    def update(self):
        self.image.fill(Color(FIRE_COLOR))
        self.fireAnim.blit(self.image, (0, 0))