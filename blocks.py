from pygame import *
# класс платформ
class Platform(sprite.Sprite):
    def  __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image=Surface((50,50))
        self.image = image.load("image/imgonline-com-ua-Resize-b6eIAZ5vv0.png").convert_alpha()
        self.rect=Rect(x,y,50,50)

class DieBlockLava(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)
        self.image = image.load("image/dieblock/lava.png").convert_alpha()

class Teleport(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)
        self.image.fill(Color('#888888'))
        self.image.set_colorkey(Color('#888888'))
        self.image = image.load("image/steleport/stp.png").convert_alpha()
class Background():
    def __init__(self,x,y):
        self.image = image.load('image/wall_corner_front_left.png').convert_alpha()
        self.rect=Rect(x,y,50,50)
    
