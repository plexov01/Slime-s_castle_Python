from pygame import *
# класс платформ
class Platform(sprite.Sprite):
    def  __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image=Surface((50,50))
        self.image.fill(Color("#123456"))
        self.rect=Rect(x,y,50,50)

class DieBlockLamp(Platform):
    def __init__(self,x,y):
        Platform.__init__(self, x, y)
        self.image = image.load("image\dieblock\dieblock.png")

class DieBlockLava(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)
        self.image = image.load("image\dieblock\lava.png")

class Teleport(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)
        self.image = image.load("image\steleport\stp.png")
    
    
