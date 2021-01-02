import pygame
from pygame import *


widthW = 1920  # 1000
heightW = 1080  # 1080

screen = pygame.display.set_mode((widthW, heightW), SCALED|FULLSCREEN)  # Окно игры
#настройки
class Options:
    def __init__(self, volume,music, punkts1=[120, 140, u'Punkt1', (250, 250, 30), (250, 30, 250), 0]):
        self.punkts1 = punkts1
        self.volume = volume
        self.music = music

    def render(self, pover, font, num):
        for i in self.punkts1:
            if num == i[5]:
                pover.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                pover.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def OptionsProcessing(self):
        done = True
        font_options = pygame.font.SysFont('ubuntu', 88)
        punkt1 = 0
        while done:
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.punkts1:
                if mp[0] > i[0] and mp[0] < i[0]+155 and mp[1] > i[1] and mp[1] < i[1]+90:
                    punkt1 = i[5]
            self.render(screen, font_options, punkt1)
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
                    if punkt1 == 1:
                        if self.volume > 1:
                            self.volume = 1
                        else:
                            self.volume += 0.1

                        self.music.set_volume(self.volume)

                    if punkt1 == 0:
                        done = False
                        Menu.menu()
                    elif punkt1 == 2:

                        if self.volume < 0:
                            self.volume = 0
                        else:
                            self.volume -= 0.1

                        self.music.set_volume(self.volume)

            pygame.display.flip()


#создаем настройки
punkts1 = [(200, 890, u'Back', (250, 250, 30), (250, 30, 250), 0),
           (810, 490, u'+', (250, 250, 30), (250, 30, 250), 1),
           (900, 490, u'-', (250, 250, 30), (250, 30, 250), 2)]
