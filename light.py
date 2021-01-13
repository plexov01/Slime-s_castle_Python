import pygame
from pygame import *
# Класс для создания эффекта освещённых участков
class Light():
    def __init__(self, WindowWidth, WindowHeight):
        # Создаю типы освещения
        self.WindowWidth = WindowWidth
        self.WindowHeight=WindowHeight
        self.filter=Surface((WindowWidth, WindowHeight))
        self.filter.fill(color.Color('#FFFFFF'))
        # for 
        self.lightType1 = image.load('effects/light/lightType1.png').convert_alpha()
        self.lightType2 = image.load('effects/light/lightType2.png').convert_alpha()
        self.lightType3 = image.load('effects/light/lightType3.png').convert_alpha()
        self.lightType4 = image.load('effects/light/lightType4.png').convert_alpha()

        self.lightType1R500 = image.load('effects/light/lightType1R500.png').convert_alpha()
        self.lightType1R1000 = transform.scale(self.lightType1, (2000, 2000))
        self.lightType1R1250 = transform.scale(self.lightType1, (2500, 2500))
        # self.lightType1R1500 = transform.scale(self.lightType1, (3000, 3000))

        # self.lightType2R500 = transform.scale(self.lightType2, (1000, 1000))
        self.lightType2R1000 = transform.scale(self.lightType2, (2000, 2000))
        # self.lightType2R1250 = transform.scale(self.lightType2, (2500, 2500))
        # self.lightType2R1500 = transform.scale(self.lightType2, (3000, 3000))

        # self.lightType3R500 = transform.scale(self.lightType3, (1000, 1000))
        # self.lightType3R1000 = transform.scale(self.lightType3, (2000, 2000))
        # self.lightType3R1250 = transform.scale(self.lightType3, (2500, 2500))
        # self.lightType3R1500 = transform.scale(self.lightType3, (3000, 3000))

        # self.lightType4R500 = transform.scale(self.lightType4, (1000, 1000))
        # self.lightType4R1000 = transform.scale(self.lightType4, (2000, 2000))
        # self.lightType4R1250 = transform.scale(self.lightType4, (2500, 2500))
        # self.lightType4R1500 = transform.scale(self.lightType4, (3000, 3000))

        # self.light=transform.scale(self.light,(1000,1000))
        # self.wigthLight=self.light.get_width()
        # self.heightLight=self.light.get_height()
        # type = ['1', '2', '3', '4', '',

        # ]
        
    def Clear(self):
        self.filter.fill(color.Color('#FFFFFF'))


    def MakeLight(self,type='norm',r='500'):

        self.wigthLight = self.lightType1R1000.get_width()
        self.heightLight = self.lightType1R1000.get_height()

        if type=='norm':
            self.filter.blit(self.lightType1R1000,(self.WindowWidth//2-self.wigthLight//2,self.WindowHeight//2-self.heightLight//2))
            return self.filter
        


# pygame.init()
# screen = pygame.display.set_mode((640, 480))
# light = pygame.image.load('circle5.png')
# light = pygame.transform.scale(
#     light, (light.get_width()*5, light.get_height()*5))
# while True:
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             break
#     else:
#         screen.fill(pygame.color.Color('#123456'))
#         # for x in range(0, 640, 20):
#         #     pygame.draw.line(screen, pygame.color.Color('Green'), (x, 0), (x, 480), 3)
#         filter = pygame.surface.Surface((640, 480))
#         filter.fill(pygame.color.Color('white'))
#         # filter.blit(light, map(lambda x: x-50, pygame.mouse.get_pos()))
#         filter.blit(light, (10, 10))
#         # , special_flags=BLEND_RGBA_SUB
#         screen.blit(filter, (0, 0), special_flags=BLEND_RGBA_SUB)
#         pygame.display.flip()
#         continue
#     break
