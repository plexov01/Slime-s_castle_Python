from options import Options, punkts1
import pygame
from pygame import *
import sys
# from game import music

# music = mixer.Sound("music/background_music.ogg")
# music.play(-1)
# # #Громкость
# volume = 0  # 0.3
# music.set_volume(volume)

widthW = 1920  # 1000
heightW = 1080  # 1080

screen = pygame.display.set_mode((widthW, heightW))  # Окно игры

#меню
class Menu:
    def __init__(self, volume,music, punkts=[120, 140, u'Punkt', (250, 250, 30), (250, 30, 250), 0]):
        self.punkts = punkts
        self.volume = volume
        self.music = music

    def render(self, pover, font, num):
        for i in self.punkts:
            if num == i[5]:
                pover.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                pover.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def MenuProcessing(self):
        done = True
        font_menu = pygame.font.SysFont('ubuntu', 88)
        punkt = 0
        while done:
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0]+155 and mp[1] > i[1] and mp[1] < i[1]+90:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

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
                        if punkt > 0:
                            punkt -= 1
                    if c.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                            punkt += 1
                if c.type == pygame.MOUSEBUTTONDOWN and c.button == 1:
                    if punkt == 1:
                        done == False
                        CreatedOptions = Options(self.volume, self.music, punkts1)
                        CreatedOptions.OptionsProcessing()
                    if punkt == 0:
                        done = False
                    elif punkt == 2:
                        done = False
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()


#создаем меню
punkts = [(810, 390, u'Game', (250, 250, 30), (250, 30, 250), 0),
          (810, 490, u'Options', (250, 250, 30), (250, 30, 250), 1),
          (810, 590, u'Quit', (250, 250, 30), (250, 30, 250), 2)]
