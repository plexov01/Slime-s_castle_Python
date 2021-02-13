import pygame
from pygame import *
import sys
from functions import Font

widthW = 1920  # 1920
heightW = 1080  # 1080

screen = pygame.display.set_mode((widthW, heightW))  # Окно игры
PixelWhiteText = [0,Font('PixelWhite'), Font('PixelWhite', 2), Font('PixelWhite', 3), Font('PixelWhite', 4)] 
PixelBlackText = [0,Font('PixelBlack'), Font('PixelBlack', 2), Font('PixelBlack', 3), Font('PixelBlack', 4)]
#настройки
class Options:
    def __init__(self, volume,music, punkts1=[120, 140, u'Punkt1', (250, 250, 30), (250, 30, 250), 0]):
        self.punkts1 = punkts1
        self.volume = volume
        self.music = music
        self.punkts=[('Back',Rect(100,100,150,150)),('+',Rect(400,100,150,150)),('-',Rect(600,100,150,150))]
        self.NotPushAll=True
        self.Push=0

    def render(self, pover, font, num, NotPushAll):
        # for i in self.punkts:
        #     PixelBlackText[1].render(screen, i[0], i[1].topleft)
        for i in self.punkts:
            PixelBlackText[1].render(screen, i[0], i[1].topleft)
            if num == i[0]:
                PixelWhiteText[1].render(screen, i[0], i[1].topleft)
            # pover.blit(font.render(i[1], 1, (123,123,123)), (i[1].x, i[1].y))
            # else:
        if NotPushAll:
            PixelBlackText[1].render(screen, i[0], i[1].topleft)
                # PixelWhiteText[1].render(screen, i[1], (i[1].x, i[1].y))
                # pover.blit(font.render(i[0], 1, (0, 0, 0)), i[1].topleft)
        # for i in self.punkts:
        #     if num == i[1]:
        #         PixelWhiteText[1].render(screen, i[1], (i[1].x, i[1].y))
                # pover.blit(font.render(i[1], 1, (123,123,123)), (i[1].x, i[1].y))
            # else:
            #     pover.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def OptionsProcessing(self):
        done = True
        font_options = pygame.font.SysFont('ubuntu', 88)
        punkt1 = 0
        while done:
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            self.NotPushAll=False
            self.Push = 0
            for i in self.punkts:
                
                # Rect(mp[0], mp[1], 1, 1).fill((255,255,255))
                surf=Surface((150,150))
                surf.fill((123,123, 123))
                screen.blit(surf, i[1].topleft)
                # PixelBlackText[1].render(screen, i[0], i[1].topleft)
                # screen.blit(surf, Rect(mp[0], mp[1], 1, 1))
                if i[1].colliderect(Rect(mp[0],mp[1],1,1)):
                    self.Push+=1
                    punkt1 = i[0]
            if self.Push>0:
                self.NotPushAll=True
            self.render(screen, font_options, punkt1,self.NotPushAll)

            for c in pygame.event.get():
                if c.type == pygame.QUIT:
                    done = False
                    pygame.quit()
                    sys.exit()
                if c.type == pygame.KEYDOWN:
                    if c.key == pygame.K_ESCAPE:
                        done = False
                        pygame.quit()
                        sys.exit()
                    if c.key == pygame.K_UP:
                        if punkt1 > 0:
                            punkt -= 1
                    if c.key == pygame.K_DOWN:
                        if punkt1 < len(self.punkts)-1:
                            punkt1 += 1
                if c.type == pygame.MOUSEBUTTONDOWN:
                    if punkt1 == '+':
                        # print('+')
                        if self.volume > 1:
                            self.volume = 1
                        else:
                            self.volume += 0.1

                        self.music.set_volume(self.volume)

                    if punkt1 == 'Back':
                        # print('Back')
                        done = False
                        # Menu.MenuProcessing()
                    elif punkt1 == '-':
                        # print('-')
                        if self.volume < 0:
                            self.volume = 0
                        
                        else:
                            self.volume -= 0.1


                        self.music.set_volume(self.volume)

            pygame.display.flip()


#создаем настройки
punkts1 = [(200, 890, u'Back', (250, 250, 30), (250, 30, 250), 'Back'),
           (810, 490, u'+', (250, 250, 30), (250, 30, 250), '+'),
           (900, 490, u'-', (250, 250, 30), (250, 30, 250), '-')]
